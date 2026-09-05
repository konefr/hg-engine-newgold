#!/usr/bin/env python3
"""
Generate a HeartGold / HG-Engine trainer baseline log from data/Trainers.c.

Designed for the progression from the start of the game through Morty.
It reads YOUR local HG-Engine checkout, so the IDs and battle data in the
generated log match the exact revision you are working on.

Usage (from the hg-engine repository root):
    python3 hg_trainer_log_generator.py

Optional:
    python3 hg_trainer_log_generator.py --output docs/trainers_to_morty.md
    python3 hg_trainer_log_generator.py --include-raw
    python3 hg_trainer_log_generator.py --force

By default the generated log keeps all battle-relevant C data (trainer data
and party) but omits the long dialogue/text section. --include-raw also adds
the complete original trainer C block.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class TrainerRef:
    trainer_id: int
    expected_name: str
    role: str = "Trainer"
    note: str = ""


@dataclass(frozen=True)
class Section:
    title: str
    location_note: str
    trainers: tuple[TrainerRef, ...]


# Curated story/progression order from New Bark Town to Morty.
# Variants of the same rival battle are kept together.
# Optional/night/path-dependent battles are explicitly labelled.
SECTIONS: tuple[Section, ...] = (
    Section(
        "1. Primo incontro con Silver",
        "Route 29 / ritorno verso New Bark Town. Una sola delle tre varianti viene usata, in base allo starter del giocatore.",
        (
            TrainerRef(2, "Silver", "Rival variant", "Silver con Cyndaquil"),
            TrainerRef(3, "Silver", "Rival variant", "Silver con Totodile"),
            TrainerRef(265, "Silver", "Rival variant", "Silver con Chikorita"),
        ),
    ),
    Section(
        "2. Route 30",
        "Primi allenatori normali della progressione.",
        (
            TrainerRef(8, "Joey", "Youngster"),
            TrainerRef(47, "Mikey", "Youngster"),
            TrainerRef(249, "Don", "Bug Catcher"),
        ),
    ),
    Section(
        "3. Route 31",
        "",
        (
            TrainerRef(4, "Wade", "Bug Catcher"),
        ),
    ),
    Section(
        "4. Sprout Tower",
        "Ordine di avanzamento fino all'Elder.",
        (
            TrainerRef(51, "Nico", "Sage"),
            TrainerRef(43, "Chow", "Sage"),
            TrainerRef(52, "Edmond", "Sage"),
            TrainerRef(53, "Jin", "Sage"),
            TrainerRef(55, "Neal", "Sage"),
            TrainerRef(54, "Troy", "Sage"),
            TrainerRef(290, "Li", "Elder / miniboss candidate"),
        ),
    ),
    Section(
        "5. Violet Gym",
        "",
        (
            TrainerRef(50, "Abe", "Gym trainer"),
            TrainerRef(29, "Rod", "Gym trainer"),
            TrainerRef(20, "Falkner", "GYM LEADER"),
        ),
    ),
    Section(
        "6. Route 32",
        "Allenatori incontrabili lungo la progressione principale.",
        (
            TrainerRef(49, "Albert", "Youngster"),
            TrainerRef(27, "Liz", "Picnicker"),
            TrainerRef(26, "Roland", "Camper"),
            TrainerRef(60, "Henry", "Fisherman"),
            TrainerRef(18, "Justin", "Fisherman"),
            TrainerRef(57, "Ralph", "Fisherman"),
            TrainerRef(56, "Gordon", "Youngster"),
            TrainerRef(383, "Peter", "Bird Keeper"),
        ),
    ),
    Section(
        "7. Union Cave — percorso principale",
        "Esclusi gli allenatori delle aree accessibili solo tornando più tardi con Surf.",
        (
            TrainerRef(390, "Ray", "Firebreather"),
            TrainerRef(384, "Daniel", "Hiker"),
            TrainerRef(25, "Russel", "Hiker"),
            TrainerRef(319, "Bill", "Firebreather"),
            TrainerRef(23, "Larry", "Poké Maniac"),
        ),
    ),
    Section(
        "8. Route 33",
        "",
        (
            TrainerRef(61, "Anthony", "Hiker"),
        ),
    ),
    Section(
        "9. Slowpoke Well",
        "Team Rocket, fino a Proton.",
        (
            TrainerRef(101, "Grunt", "Team Rocket Grunt"),
            TrainerRef(13, "Grunt", "Team Rocket Grunt"),
            TrainerRef(12, "Grunt", "Team Rocket Grunt"),
            TrainerRef(486, "Proton", "ROCKET EXECUTIVE / miniboss"),
        ),
    ),
    Section(
        "10. Azalea Gym",
        "La disposizione del puzzle può rendere l'ordine di alcuni trainer non rigidamente lineare.",
        (
            TrainerRef(67, "Benny", "Gym trainer"),
            TrainerRef(10, "Amy & Mimi", "Gym trainer / double", "Nel trainer table esiste anche un duplicato/alias: verificare l'eventuale uso dell'ID [387] se si modifica lo script della mappa."),
            TrainerRef(68, "Al", "Gym trainer"),
            TrainerRef(69, "Josh", "Gym trainer"),
            TrainerRef(21, "Bugsy", "GYM LEADER"),
        ),
    ),
    Section(
        "11. Silver — Azalea Town",
        "Battaglia dopo Bugsy. Una sola variante viene usata in base allo starter.",
        (
            TrainerRef(1, "Silver", "Rival variant", "Linea Bayleef"),
            TrainerRef(266, "Silver", "Rival variant", "Linea Quilava"),
            TrainerRef(269, "Silver", "Rival variant", "Linea Croconaw"),
        ),
    ),
    Section(
        "12. Route 34",
        "",
        (
            TrainerRef(62, "Samuel", "Youngster"),
            TrainerRef(409, "Brandon", "Pokéfan"),
            TrainerRef(65, "Gina", "Picnicker"),
            TrainerRef(64, "Ian", "Youngster"),
            TrainerRef(6, "Keith", "Policeman", "NIGHT-ONLY"),
            TrainerRef(66, "Todd", "Camper"),
        ),
    ),
    Section(
        "13. Goldenrod Underground / Tunnel",
        "OPTIONAL prima di Whitney; ordine dipendente dall'ingresso e dal percorso.",
        (
            TrainerRef(392, "Donald", "Poké Maniac", "OPTIONAL"),
            TrainerRef(393, "Teru", "Super Nerd", "OPTIONAL"),
            TrainerRef(391, "Issac", "Poké Maniac", "OPTIONAL"),
            TrainerRef(233, "Eric", "Super Nerd", "OPTIONAL"),
        ),
    ),
    Section(
        "14. Goldenrod Gym",
        "",
        (
            TrainerRef(5, "Victoria", "Gym trainer"),
            TrainerRef(70, "Samantha", "Gym trainer"),
            TrainerRef(22, "Carrie", "Gym trainer"),
            TrainerRef(71, "Cathy", "Gym trainer"),
            TrainerRef(30, "Whitney", "GYM LEADER"),
        ),
    ),
    Section(
        "15. Route 35",
        "",
        (
            TrainerRef(77, "Kim", "Picnicker"),
            TrainerRef(75, "Elliot", "Camper"),
            TrainerRef(76, "Brooke", "Picnicker"),
            TrainerRef(74, "Ivan", "Camper"),
            TrainerRef(7, "Irwin", "Juggler"),
            TrainerRef(388, "Walt", "Firebreather"),
            TrainerRef(80, "Dirk", "Policeman", "NIGHT-ONLY"),
            TrainerRef(78, "Arnie", "Bug Catcher"),
            TrainerRef(72, "Bryan", "Bird Keeper"),
        ),
    ),
    Section(
        "16. National Park",
        "Path/exploration dependent; useful to considerare nella curva anche se alcuni possono essere evitati.",
        (
            TrainerRef(182, "Beverly", "Pokéfan", "OPTIONAL/PATH-DEPENDENT"),
            TrainerRef(181, "William", "Pokéfan", "OPTIONAL/PATH-DEPENDENT"),
            TrainerRef(178, "Jack", "School Kid", "OPTIONAL/PATH-DEPENDENT"),
            TrainerRef(184, "Krise", "Lass", "OPTIONAL/PATH-DEPENDENT"),
        ),
    ),
    Section(
        "17. Route 36",
        "",
        (
            TrainerRef(395, "Mark", "Psychic"),
            TrainerRef(24, "Alan", "School Kid"),
        ),
    ),
    Section(
        "18. Route 37",
        "",
        (
            TrainerRef(81, "Tori & Til", "Twins / double"),
            TrainerRef(679, "Callie", "Beauty / paired double"),
            TrainerRef(680, "Kassandra", "Beauty / paired double"),
            TrainerRef(386, "Greg", "Psychic"),
        ),
    ),
    Section(
        "19. Ecruteak Dance Theater",
        "Scontro Rocket collegato all'ottenimento di Surf.",
        (
            TrainerRef(63, "Mickey", "Team Rocket Grunt / miniboss candidate"),
        ),
    ),
    Section(
        "20. Burned Tower — Silver",
        "Battaglia prima di Morty. Una sola variante viene usata in base allo starter.",
        (
            TrainerRef(263, "Silver", "Rival variant", "Linea Bayleef"),
            TrainerRef(267, "Silver", "Rival variant", "Linea Quilava"),
            TrainerRef(270, "Silver", "Rival variant", "Linea Croconaw"),
        ),
    ),
    Section(
        "21. Ecruteak Gym",
        "",
        (
            TrainerRef(494, "Georgina", "Gym trainer"),
            TrainerRef(89, "Grace", "Gym trainer"),
            TrainerRef(493, "Edith", "Gym trainer"),
            TrainerRef(46, "Martha", "Gym trainer"),
            TrainerRef(31, "Morty", "GYM LEADER"),
        ),
    ),
)


def _run_git(args: list[str], cwd: Path) -> str:
    try:
        cp = subprocess.run(
            ["git", *args],
            cwd=cwd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return cp.stdout.strip()
    except Exception:
        return "unknown"


def _find_balanced_brace(text: str, open_pos: int) -> int:
    """Return index of matching } while ignoring braces inside strings/comments."""
    if text[open_pos] != "{":
        raise ValueError("open_pos must point to '{'")

    depth = 0
    i = open_pos
    in_string = False
    in_char = False
    escaped = False
    line_comment = False
    block_comment = False

    while i < len(text):
        c = text[i]
        n = text[i + 1] if i + 1 < len(text) else ""

        if line_comment:
            if c == "\n":
                line_comment = False
            i += 1
            continue

        if block_comment:
            if c == "*" and n == "/":
                block_comment = False
                i += 2
            else:
                i += 1
            continue

        if in_string:
            if escaped:
                escaped = False
            elif c == "\\":
                escaped = True
            elif c == '"':
                in_string = False
            i += 1
            continue

        if in_char:
            if escaped:
                escaped = False
            elif c == "\\":
                escaped = True
            elif c == "'":
                in_char = False
            i += 1
            continue

        if c == "/" and n == "/":
            line_comment = True
            i += 2
            continue
        if c == "/" and n == "*":
            block_comment = True
            i += 2
            continue
        if c == '"':
            in_string = True
            i += 1
            continue
        if c == "'":
            in_char = True
            i += 1
            continue

        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i

        i += 1

    raise ValueError("Unbalanced braces")


def extract_trainer_block(source: str, trainer_id: int) -> str:
    # Require the trainer ID at the start of a table entry line.
    pat = re.compile(rf"(?m)^[ \t]*\[{trainer_id}\][ \t]*=[ \t]*\{{")
    m = pat.search(source)
    if not m:
        raise KeyError(f"Trainer ID [{trainer_id}] not found")

    line_start = source.rfind("\n", 0, m.start()) + 1
    open_pos = source.find("{", m.start(), m.end())
    close_pos = _find_balanced_brace(source, open_pos)

    # Include trailing comma if present.
    end = close_pos + 1
    while end < len(source) and source[end] in " \t":
        end += 1
    if end < len(source) and source[end] == ",":
        end += 1

    return source[line_start:end]


def remove_named_subblock(block: str, field_name: str) -> str:
    """Remove a top-level `.field_name = { ... },` block."""
    pat = re.compile(rf"(?m)^[ \t]*\.{re.escape(field_name)}[ \t]*=[ \t]*\{{")
    m = pat.search(block)
    if not m:
        return block

    line_start = block.rfind("\n", 0, m.start()) + 1
    open_pos = block.find("{", m.start(), m.end())
    close_pos = _find_balanced_brace(block, open_pos)
    end = close_pos + 1
    while end < len(block) and block[end] in " \t":
        end += 1
    if end < len(block) and block[end] == ",":
        end += 1
    if end < len(block) and block[end] == "\n":
        end += 1
    return block[:line_start] + block[end:]


def field_value(block: str, field: str) -> Optional[str]:
    m = re.search(rf"(?m)^[ \t]*\.{re.escape(field)}[ \t]*=[ \t]*(.+?)[ \t]*,[ \t]*$", block)
    return m.group(1).strip() if m else None


def trainer_name(block: str) -> str:
    m = re.search(r'(?m)^[ \t]*\.name[ \t]*=[ \t]*"([^"]*)"', block)
    return m.group(1) if m else "?"


def party_summary(block: str) -> tuple[list[str], Optional[int]]:
    """
    Return simple per-Pokémon summaries, preserving only fields useful at a glance.
    Exact battle C data remains embedded separately in the log.
    """
    # Isolate party block.
    m = re.search(r"(?m)^[ \t]*\.party[ \t]*=[ \t]*\{", block)
    if not m:
        return [], None

    open_pos = block.find("{", m.start(), m.end())
    close_pos = _find_balanced_brace(block, open_pos)
    party = block[open_pos + 1 : close_pos]

    # Parse direct child {...} Pokémon blocks.
    mons: list[str] = []
    levels: list[int] = []
    i = 0
    while i < len(party):
        if party[i] == "{":
            end = _find_balanced_brace(party, i)
            mon = party[i : end + 1]
            level_m = re.search(r"\.level\s*=\s*(\d+)", mon)
            species_m = re.search(r"\.species\s*=\s*([A-Z0-9_]+)", mon)
            ivs_m = re.search(r"\.ivs\s*=\s*([^,\n]+)", mon)
            ability_m = re.search(r"\.abilitySlot\s*=\s*([^,\n]+)", mon)
            item_m = re.search(r"\.item\s*=\s*([^,\n]+)", mon)
            moves_m = re.search(r"\.moves\s*=\s*\{([^}]*)\}", mon, flags=re.S)
            nature_m = re.search(r"\.nature\s*=\s*([^,\n]+)", mon)
            evs_m = re.search(r"\.evs\s*=\s*\{([^}]*)\}", mon, flags=re.S)

            bits = []
            if species_m:
                species = species_m.group(1).replace("SPECIES_", "")
                bits.append(species)
            if level_m:
                lv = int(level_m.group(1))
                levels.append(lv)
                bits.append(f"Lv.{lv}")
            if item_m:
                bits.append(f"item={item_m.group(1).strip()}")
            if ability_m:
                bits.append(f"ability={ability_m.group(1).strip()}")
            if ivs_m:
                bits.append(f"IVs={ivs_m.group(1).strip()}")
            if nature_m:
                bits.append(f"nature={nature_m.group(1).strip()}")
            if evs_m:
                evs = " ".join(evs_m.group(1).split())
                bits.append(f"EVs={evs}")
            if moves_m:
                moves = " ".join(moves_m.group(1).split())
                bits.append(f"moves={moves}")
            mons.append(" · ".join(bits) if bits else "(party entry)")
            i = end + 1
        else:
            i += 1

    return mons, (max(levels) if levels else None)


def c_fence(text: str) -> str:
    return "```c\n" + text.rstrip() + "\n```"


def make_log(repo: Path, source_path: Path, include_raw: bool) -> str:
    source = source_path.read_text(encoding="utf-8")
    commit = _run_git(["rev-parse", "--short", "HEAD"], repo)
    branch = _run_git(["branch", "--show-current"], repo)
    status = _run_git(["status", "--porcelain"], repo)
    dirty = "YES" if status else "NO"
    generated = _dt.datetime.now().astimezone().isoformat(timespec="seconds")

    out: list[str] = []
    out.append("# HeartGold Modern — Trainer baseline: inizio → Morty")
    out.append("")
    out.append("> **Scopo:** baseline tecnica per progettare level curve, squadre, setup e difficoltà.")
    out.append("> Gli ID **[###]** sono la chiave stabile da usare nel changelog personale.")
    out.append("> Il file è generato dal `data/Trainers.c` locale: quindi riflette la tua esatta revisione HG-Engine.")
    out.append("")
    out.append("## Snapshot")
    out.append("")
    out.append(f"- Git branch: `{branch}`")
    out.append(f"- Git commit: `{commit}`")
    out.append(f"- Working tree dirty al momento della generazione: **{dirty}**")
    out.append(f"- Sorgente: `{source_path.relative_to(repo) if source_path.is_relative_to(repo) else source_path}`")
    out.append(f"- Generato: `{generated}`")
    out.append("")
    out.append("## Convenzioni")
    out.append("")
    out.append("- **Ace** = livello massimo presente nel party del trainer.")
    out.append("- Le varianti di Silver sono raggruppate nello stesso punto della progressione.")
    out.append("- `OPTIONAL`, `NIGHT-ONLY` e `PATH-DEPENDENT` sono marcati esplicitamente.")
    out.append("- Sono esclusi rematch e trainer di aree che richiedono backtracking tardivo (es. sezioni Surf-only di Union Cave).")
    out.append("- La sezione **Battle data (exact C)** conserva i dati di combattimento esattamente come sono nel tuo `Trainers.c`, ma omette i dialoghi `.text` per rendere il log leggibile.")
    if include_raw:
        out.append("- `--include-raw` è attivo: sotto ogni trainer compare anche l'intero blocco C originale, dialoghi inclusi.")
    out.append("")
    out.append("---")
    out.append("")

    missing: list[int] = []
    warnings: list[str] = []

    for section in SECTIONS:
        out.append(f"## {section.title}")
        out.append("")
        if section.location_note:
            out.append(section.location_note)
            out.append("")

        for tref in section.trainers:
            try:
                block = extract_trainer_block(source, tref.trainer_id)
            except Exception as exc:
                missing.append(tref.trainer_id)
                out.append(f"### [{tref.trainer_id}] {tref.expected_name} — ⚠ NOT FOUND")
                out.append("")
                out.append(f"`{exc}`")
                out.append("")
                continue

            actual_name = trainer_name(block)
            if tref.expected_name.lower() not in actual_name.lower() and actual_name.lower() not in tref.expected_name.lower():
                warnings.append(f"[{tref.trainer_id}] expected '{tref.expected_name}', got '{actual_name}'")

            trainer_type = field_value(block, "trainerType") or "?"
            trainer_class = field_value(block, "trainerClass") or "?"
            items = field_value(block, "items") or "?"
            ai_flags = field_value(block, "aiFlags") or "?"
            battle_type = field_value(block, "battleType") or "?"
            party, ace = party_summary(block)

            out.append(f"### [{tref.trainer_id}] {actual_name}")
            out.append("")
            out.append(f"- **Progression role:** {tref.role}")
            if tref.note:
                out.append(f"- **Nota:** {tref.note}")
            out.append(f"- **Trainer class:** `{trainer_class}`")
            out.append(f"- **Trainer data type:** `{trainer_type}`")
            out.append(f"- **Battle type:** `{battle_type}`")
            out.append(f"- **Trainer items:** `{items}`")
            out.append(f"- **AI flags:** `{ai_flags}`")
            out.append(f"- **Ace / max level:** `{ace if ace is not None else '?'}'")
            out[-1] = out[-1][:-1]  # remove helper quote
            if party:
                out.append("- **Party at a glance:**")
                for mon in party:
                    out.append(f"  - {mon}")
            else:
                out.append("- **Party at a glance:** _(not parsed)_")
            out.append("")
            out.append("#### Battle data — exact C")
            out.append("")
            battle_block = remove_named_subblock(block, "text")
            out.append(c_fence(battle_block))
            out.append("")
            if include_raw:
                out.append("<details>")
                out.append("<summary>Complete original C block (including text/dialogue)</summary>")
                out.append("")
                out.append(c_fence(block))
                out.append("")
                out.append("</details>")
                out.append("")

            out.append("#### HeartGold Modern — worklog")
            out.append("")
            out.append("- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss")
            out.append("- **Target level / ace:**")
            out.append("- **Nuovo party / setup:**")
            out.append("- **AI / held items / ability / IV-EV changes:**")
            out.append("- **Razionale di design:**")
            out.append("- **Test status:** ☐ non testato ☐ compila ☐ testato in-game")
            out.append("- **Note:**")
            out.append("")
            out.append("---")
            out.append("")

    out.append("## Generator diagnostics")
    out.append("")
    if missing:
        out.append(f"- Missing trainer IDs: {', '.join(f'[{x}]' for x in missing)}")
    else:
        out.append("- Missing trainer IDs: none")
    if warnings:
        out.append("- Name warnings:")
        for w in warnings:
            out.append(f"  - {w}")
    else:
        out.append("- Name warnings: none")
    out.append("")
    out.append("> Se HG-Engine viene aggiornato, rigenera questo file e confrontalo con Git invece di correggere manualmente la baseline.")
    out.append("")

    return "\n".join(out)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--repo", default=".", help="HG-Engine repo root (default: current directory)")
    p.add_argument("--source", default="data/Trainers.c", help="Trainer source path relative to repo")
    p.add_argument("--output", default="trainer_baseline_start_to_morty.md")
    p.add_argument("--include-raw", action="store_true", help="Also include full C trainer blocks, including dialogue")
    p.add_argument("--force", action="store_true", help="Overwrite output if it already exists")
    args = p.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    source = (repo / args.source).resolve()
    output = Path(args.output).expanduser()
    if not output.is_absolute():
        output = repo / output

    if not source.exists():
        print(f"ERROR: source not found: {source}", file=sys.stderr)
        print("Run this script from the hg-engine repository root.", file=sys.stderr)
        return 2

    if output.exists() and not args.force:
        print(f"ERROR: output already exists: {output}", file=sys.stderr)
        print("Use --force or choose another --output path.", file=sys.stderr)
        return 3

    log = make_log(repo, source, args.include_raw)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(log, encoding="utf-8")
    print(f"Wrote: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
