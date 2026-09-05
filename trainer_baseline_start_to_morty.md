# HeartGold Modern — Trainer baseline: inizio → Morty

> **Scopo:** baseline tecnica per progettare level curve, squadre, setup e difficoltà.
> Gli ID **[###]** sono la chiave stabile da usare nel changelog personale.
> Il file è generato dal `data/Trainers.c` locale: quindi riflette la tua esatta revisione HG-Engine.

## Snapshot

- Git branch: `heartgold-modern`
- Git commit: `f6d878a53`
- Working tree dirty al momento della generazione: **YES**
- Sorgente: `data/Trainers.c`
- Generato: `2026-09-04T15:31:53+02:00`

## Convenzioni

- **Ace** = livello massimo presente nel party del trainer.
- Le varianti di Silver sono raggruppate nello stesso punto della progressione.
- `OPTIONAL`, `NIGHT-ONLY` e `PATH-DEPENDENT` sono marcati esplicitamente.
- Sono esclusi rematch e trainer di aree che richiedono backtracking tardivo (es. sezioni Surf-only di Union Cave).
- La sezione **Battle data (exact C)** conserva i dati di combattimento esattamente come sono nel tuo `Trainers.c`, ma omette i dialoghi `.text` per rendere il log leggibile.

---

## 1. Primo incontro con Silver

Route 29 / ritorno verso New Bark Town. Una sola delle tre varianti viene usata, in base allo starter del giocatore.

### [2] Silver

- **Progression role:** Rival variant
- **Nota:** Silver con Cyndaquil
- **Trainer class:** `TRAINERCLASS_RIVAL`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `5
- **Party at a glance:**
  - CYNDAQUIL · Lv.5 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [2] = {
        .name = "Silver",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_RIVAL,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 5,
                .species = SPECIES_CYNDAQUIL,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:**  ☐ rebalance 
- **Target level / ace:** 7
- **Nuovo party / setup:** same
- **AI / held items / ability / IV-EV changes:** potion IVs: 40
- **Razionale di design:** increade difficulty
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [3] Silver

- **Progression role:** Rival variant
- **Nota:** Silver con Totodile
- **Trainer class:** `TRAINERCLASS_RIVAL`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `5
- **Party at a glance:**
  - TOTODILE · Lv.5 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [3] = {
        .name = "Silver",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_RIVAL,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 5,
                .species = SPECIES_TOTODILE,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ rebalance 
- **Target level / ace:** 7
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:** Potion IVs 40
- **Razionale di design:** increased difficulty
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [265] Silver

- **Progression role:** Rival variant
- **Nota:** Silver con Chikorita
- **Trainer class:** `TRAINERCLASS_RIVAL`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `5
- **Party at a glance:**
  - CHIKORITA · Lv.5 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [265] = {
        .name = "Silver",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_RIVAL,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 5,
                .species = SPECIES_CHIKORITA,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:**  ☐ rebalance 
- **Target level / ace:** 7
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:** potion IVs 40
- **Razionale di design:** increased difficulty
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 2. Route 30

Primi allenatori normali della progressione.

### [8] Joey

- **Progression role:** Youngster
- **Trainer class:** `TRAINERCLASS_YOUNGSTER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `4
- **Party at a glance:**
  - RATTATA · Lv.4 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [8] = {
        .name = "Joey",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_YOUNGSTER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 4,
                .species = SPECIES_RATTATA,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep X rebalance ☐ redesign ☐ miniboss
- **Target level / ace:** 5
- **Nuovo party / setup:** 2GEN
- **AI / held items / ability / IV-EV changes:** IVS 20
- **Razionale di design:** I-D
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [47] Pippo Franco

- **Progression role:** Youngster
- **Trainer class:** `TRAINERCLASS_YOUNGSTER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_SUPER_POTION, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `6
- **Party at a glance:**
  - PIDGEY · Lv.6 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - RATTATA · Lv.6 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [47] = {
        .name = "Pippo Franco",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_YOUNGSTER,
            .items = { ITEM_SUPER_POTION, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 6,
                .species = SPECIES_PIDGEY,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 6,
                .species = SPECIES_RATTATA,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep X rebalance ☐ redesign ☐ miniboss
- **Target level / ace:** 6
- **Nuovo party / setup:** 2GEN
- **AI / held items / ability / IV-EV changes:** IVS20
- **Razionale di design:** ID + MEME
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [249] Don

- **Progression role:** Bug Catcher
- **Trainer class:** `TRAINERCLASS_BUG_CATCHER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `6
- **Party at a glance:**
  - CATERPIE · Lv.6 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=100
  - CATERPIE · Lv.6 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=150

#### Battle data — exact C

```c
    [249] = {
        .name = "Don",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_BUG_CATCHER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 6,
                .species = SPECIES_CATERPIE,
                .ballSeal = 0,
            },
            {
                .ivs = 150,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 6,
                .species = SPECIES_CATERPIE,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep X rebalance ☐ redesign ☐ miniboss
- **Target level / ace:** 6
- **Nuovo party / setup:** 2GEN
- **AI / held items / ability / IV-EV changes:** IVS 100 150
- **Razionale di design:** ID 
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 3. Route 31

### [4] Wade

- **Progression role:** Bug Catcher
- **Trainer class:** `TRAINERCLASS_BUG_CATCHER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `7
- **Party at a glance:**
  - CATERPIE · Lv.6 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=150
  - CASCOON · Lv.6 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - KAKUNA · Lv.7 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - CATERPIE · Lv.2 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [4] = {
        .name = "Wade",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_BUG_CATCHER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 150,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 6,
                .species = SPECIES_CATERPIE,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 6,
                .species = SPECIES_CASCOON,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 7,
                .species = SPECIES_KAKUNA,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 2,
                .species = SPECIES_CATERPIE,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep X rebalance ☐ redesign ☐ miniboss
- **Target level / ace:** 
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 4. Sprout Tower

Ordine di avanzamento fino all'Elder.

### [51] Nico

- **Progression role:** Sage
- **Trainer class:** `TRAINERCLASS_SAGE`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `3
- **Party at a glance:**
  - BELLSPROUT · Lv.3 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - BELLSPROUT · Lv.3 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - BELLSPROUT · Lv.3 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [51] = {
        .name = "Nico",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_SAGE,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 3,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 3,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 3,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep X rebalance ☐ redesign ☐ miniboss
- **Target level / ace:** 6
- **Nuovo party / setup:** 
- **AI / held items / ability / IV-EV changes:** IVS 50-100
- **Razionale di design:** ID 
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [43] Chow

- **Progression role:** Sage
- **Trainer class:** `TRAINERCLASS_SAGE`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `3
- **Party at a glance:**
  - BELLSPROUT · Lv.3 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - BELLSPROUT · Lv.3 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - BELLSPROUT · Lv.3 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [43] = {
        .name = "Chow",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_SAGE,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 3,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 3,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 3,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep X rebalance ☐ redesign ☐ miniboss
- **Target level / ace:** 6
- **Nuovo party / setup:** 
- **AI / held items / ability / IV-EV changes:** Oran berry, potion, IVS 50-60
- **Razionale di design:** ID
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [52] Edmond

- **Progression role:** Sage
- **Trainer class:** `TRAINERCLASS_SAGE`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `3
- **Party at a glance:**
  - BELLSPROUT · Lv.3 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - BELLSPROUT · Lv.3 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - BELLSPROUT · Lv.3 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [52] = {
        .name = "Edmond",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_SAGE,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 3,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 3,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 3,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep X rebalance ☐ redesign ☐ miniboss
- **Target level / ace:** 7
- **Nuovo party / setup:** 4 bellsprout nvece che 3
- **AI / held items / ability / IV-EV changes:** IVS, oranberry, potion
- **Razionale di design:** ID
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [53] Jin

- **Progression role:** Sage
- **Trainer class:** `TRAINERCLASS_SAGE`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `6
- **Party at a glance:**
  - BELLSPROUT · Lv.6 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [53] = {
        .name = "Jin",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_SAGE,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 6,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep X rebalance ☐ redesign ☐ miniboss
- **Target level / ace:** 9
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:** IVS 100 + starf_berry +GLUTTONY
- **Razionale di design:** ID + sorpresa
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [55] Neal

- **Progression role:** Sage
- **Trainer class:** `TRAINERCLASS_SAGE`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `6
- **Party at a glance:**
  - BELLSPROUT · Lv.6 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [55] = {
        .name = "Neal",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_SAGE,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 6,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep X rebalance ☐ redesign ☐ miniboss
- **Target level / ace:** 9
- **Nuovo party / setup:** 
- **AI / held items / ability / IV-EV changes:** SALAC BERRY + GLUTTONY, IVS 100
- **Razionale di design:** ID
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [54] Troy

- **Progression role:** Sage
- **Trainer class:** `TRAINERCLASS_SAGE`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `7
- **Party at a glance:**
  - BELLSPROUT · Lv.7 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - HOOTHOOT · Lv.7 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [54] = {
        .name = "Troy",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_SAGE,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 7,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 7,
                .species = SPECIES_HOOTHOOT,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep X rebalance ☐ redesign ☐ miniboss
- **Target level / ace:** 9
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:** NATU + BELLSPROUT, IVS 100
- **Razionale di design:** ID
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [290] Li

- **Progression role:** Elder / miniboss candidate
- **Trainer class:** `TRAINERCLASS_ELDER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `10
- **Party at a glance:**
  - BELLSPROUT · Lv.7 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - BELLSPROUT · Lv.7 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - HOOTHOOT · Lv.10 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [290] = {
        .name = "Li",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_ELDER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 7,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 7,
                .species = SPECIES_BELLSPROUT,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 10,
                .species = SPECIES_HOOTHOOT,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign X miniboss
- **Target level / ace:** 10
- **Nuovo party / setup:** added meditite
- **AI / held items / ability / IV-EV changes:** ivs 50-100, gluttny + berries, 
- **Razionale di design:** level cap miniboss
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 5. Violet Gym

### [50] Abe

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_BIRD_KEEPER_GS`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `12
- **Party at a glance:**
  - SPEAROW · Lv.11 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=50
  - NATU · Lv.11 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=100
  - FARFETCHD · Lv.12 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=100

#### Battle data — exact C

```c
    [50] = {
        .name = "Abe",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_BIRD_KEEPER_GS,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 50,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 11,
                .species = SPECIES_SPEAROW,
                .ballSeal = 0,
            },
              {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 11,
                .species = SPECIES_NATU,
                .ballSeal = 0,
            },
            {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_FARFETCHD,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep x rebalance ☐ redesign ☐ miniboss
- **Target level / ace:** 11
- **Nuovo party / setup:** johto partu
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**  ID
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [29] Rod

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_BIRD_KEEPER_GS`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `12
- **Party at a glance:**
  - HOOTHOOT · Lv.10 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30
  - SPEAROW · Lv.12 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30
  - HOPPIP · Lv.10 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=200

#### Battle data — exact C

```c
    [29] = {
        .name = "Rod",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_BIRD_KEEPER_GS,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 10,
                .species = SPECIES_HOOTHOOT,
                .ballSeal = 0,
            },
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_SPEAROW,
                .ballSeal = 0,
            },
            {
                .ivs = 200,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 10,
                .species = SPECIES_HOPPIP,
                .ballSeal = 0,
            }
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance X redesign ☐ miniboss
- **Target level / ace:** 12
- **Nuovo party / setup:** added corviknight test
- **AI / held items / ability / IV-EV changes:** sleep powder + wide lens hoppip
- **Razionale di design:** ID + test
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [20] Falkner

- **Progression role:** GYM LEADER
- **Trainer class:** `TRAINERCLASS_LEADER_FALKNER`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES | TRAINER_DATA_TYPE_ITEMS`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS`
- **Ace / max level:** `13
- **Party at a glance:**
  - HOOTHOOT · Lv.11 · item=ITEM_NONE · ability=TRAINER_POKEMON_ABILITY_1 · IVs=100 · moves=MOVE_PECK, MOVE_REFLECT, MOVE_TACKLE, MOVE_CONFUSION
  - DODUO · Lv.12 · item=ITEM_NONE · ability=TRAINER_POKEMON_ABILITY_1 · IVs=120 · moves=MOVE_TAILWIND, MOVE_GROWL , MOVE_QUICK_ATTACK, MOVE_PLUCK
  - MURKROW · Lv.12 · item=ITEM_NONE · ability=TRAINER_POKEMON_ABILITY_1 · IVs=120 · moves=MOVE_PECK, MOVE_ASTONISH , MOVE_WING_ATTACK, MOVE_CONFUSE_RAY
  - FARFETCHD · Lv.13 · item=ITEM_NONE · ability=TRAINER_POKEMON_ABILITY_1 · IVs=150 · moves=MOVE_PECK, MOVE_LEER , MOVE_AERIAL_ACE, MOVE_STEEL_WING

#### Battle data — exact C

```c
    [20] = {
        .name = "Falkner",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES | TRAINER_DATA_TYPE_ITEMS,
            .trainerClass = TRAINERCLASS_LEADER_FALKNER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 11,
                .species = SPECIES_HOOTHOOT,
                .item = ITEM_NONE,
                .moves = { MOVE_PECK, MOVE_REFLECT, MOVE_TACKLE, MOVE_CONFUSION },
                .ballSeal = 0,
            },
            {
                .ivs = 120,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_DODUO,
                .item = ITEM_NONE,
                .moves = { MOVE_TAILWIND, MOVE_GROWL , MOVE_QUICK_ATTACK, MOVE_PLUCK },
                .ballSeal = 0,
            },
            {
                .ivs = 120,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_MURKROW,
                .item = ITEM_NONE,
                .moves = { MOVE_PECK, MOVE_ASTONISH , MOVE_WING_ATTACK, MOVE_CONFUSE_RAY },
                .ballSeal = 0,
            },
            {
                .ivs = 150,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 13,
                .species = SPECIES_FARFETCHD,
                .item = ITEM_NONE,
                .moves = { MOVE_PECK, MOVE_LEER , MOVE_AERIAL_ACE, MOVE_STEEL_WING },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign X miniboss
- **Target level / ace:** 13
- **Nuovo party / setup:** 5 PARTY, COMPETITIVE LIKE
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:** BOSS TOUGH
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 6. Route 32

Allenatori incontrabili lungo la progressione principale.

### [49] Albert

- **Progression role:** Youngster
- **Trainer class:** `TRAINERCLASS_YOUNGSTER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `8
- **Party at a glance:**
  - RATTATA · Lv.6 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - ZUBAT · Lv.8 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [49] = {
        .name = "Albert",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_YOUNGSTER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 6,
                .species = SPECIES_RATTATA,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 8,
                .species = SPECIES_ZUBAT,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [27] Liz

- **Progression role:** Picnicker
- **Trainer class:** `TRAINERCLASS_PICNICKER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `8
- **Party at a glance:**
  - NIDORAN_F · Lv.8 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [27] = {
        .name = "Liz",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_PICNICKER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 8,
                .species = SPECIES_NIDORAN_F,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [26] Roland

- **Progression role:** Camper
- **Trainer class:** `TRAINERCLASS_CAMPER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `9
- **Party at a glance:**
  - NIDORAN_M · Lv.9 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [26] = {
        .name = "Roland",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_CAMPER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 9,
                .species = SPECIES_NIDORAN_M,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [60] Henry

- **Progression role:** Fisherman
- **Trainer class:** `TRAINERCLASS_FISHERMAN`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `8
- **Party at a glance:**
  - POLIWAG · Lv.8 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - POLIWAG · Lv.8 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [60] = {
        .name = "Henry",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_FISHERMAN,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 8,
                .species = SPECIES_POLIWAG,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 8,
                .species = SPECIES_POLIWAG,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [18] Justin

- **Progression role:** Fisherman
- **Trainer class:** `TRAINERCLASS_FISHERMAN`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `15
- **Party at a glance:**
  - MAGIKARP · Lv.5 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - MAGIKARP · Lv.5 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - MAGIKARP · Lv.15 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - MAGIKARP · Lv.5 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [18] = {
        .name = "Justin",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_FISHERMAN,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 5,
                .species = SPECIES_MAGIKARP,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 5,
                .species = SPECIES_MAGIKARP,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 15,
                .species = SPECIES_MAGIKARP,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 5,
                .species = SPECIES_MAGIKARP,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [57] Ralph

- **Progression role:** Fisherman
- **Trainer class:** `TRAINERCLASS_FISHERMAN`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `10
- **Party at a glance:**
  - GOLDEEN · Lv.10 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [57] = {
        .name = "Ralph",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_FISHERMAN,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 10,
                .species = SPECIES_GOLDEEN,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [56] Gordon

- **Progression role:** Youngster
- **Trainer class:** `TRAINERCLASS_YOUNGSTER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `10
- **Party at a glance:**
  - WOOPER · Lv.10 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [56] = {
        .name = "Gordon",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_YOUNGSTER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 10,
                .species = SPECIES_WOOPER,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [383] Peter

- **Progression role:** Bird Keeper
- **Trainer class:** `TRAINERCLASS_BIRD_KEEPER_GS`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `8
- **Party at a glance:**
  - PIDGEY · Lv.6 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=50
  - PIDGEY · Lv.6 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=50
  - SPEAROW · Lv.8 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=50

#### Battle data — exact C

```c
    [383] = {
        .name = "Peter",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_BIRD_KEEPER_GS,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 50,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 6,
                .species = SPECIES_PIDGEY,
                .ballSeal = 0,
            },
            {
                .ivs = 50,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 6,
                .species = SPECIES_PIDGEY,
                .ballSeal = 0,
            },
            {
                .ivs = 50,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 8,
                .species = SPECIES_SPEAROW,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 7. Union Cave — percorso principale

Esclusi gli allenatori delle aree accessibili solo tornando più tardi con Surf.

### [390] Ray

- **Progression role:** Firebreather
- **Trainer class:** `TRAINERCLASS_FIREBREATHER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `9
- **Party at a glance:**
  - VULPIX · Lv.9 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [390] = {
        .name = "Ray",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_FIREBREATHER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 9,
                .species = SPECIES_VULPIX,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [384] Daniel

- **Progression role:** Hiker
- **Trainer class:** `TRAINERCLASS_HIKER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `11
- **Party at a glance:**
  - ONIX · Lv.11 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [384] = {
        .name = "Daniel",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_HIKER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 11,
                .species = SPECIES_ONIX,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [25] Russel

- **Progression role:** Hiker
- **Trainer class:** `TRAINERCLASS_HIKER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `8
- **Party at a glance:**
  - GEODUDE · Lv.4 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0
  - GEODUDE · Lv.6 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0
  - GEODUDE · Lv.8 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [25] = {
        .name = "Russel",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_HIKER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 4,
                .species = SPECIES_GEODUDE,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 6,
                .species = SPECIES_GEODUDE,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 8,
                .species = SPECIES_GEODUDE,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [319] Bill

- **Progression role:** Firebreather
- **Trainer class:** `TRAINERCLASS_FIREBREATHER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `6
- **Party at a glance:**
  - KOFFING · Lv.6 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - KOFFING · Lv.6 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [319] = {
        .name = "Bill",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_FIREBREATHER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 6,
                .species = SPECIES_KOFFING,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 6,
                .species = SPECIES_KOFFING,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [23] Larry

- **Progression role:** Poké Maniac
- **Trainer class:** `TRAINERCLASS_POKE_MANIAC`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `11
- **Party at a glance:**
  - SLOWPOKE · Lv.11 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [23] = {
        .name = "Larry",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_POKE_MANIAC,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 11,
                .species = SPECIES_SLOWPOKE,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 8. Route 33

### [61] Anthony

- **Progression role:** Hiker
- **Trainer class:** `TRAINERCLASS_HIKER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `11
- **Party at a glance:**
  - GEODUDE · Lv.11 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - MACHOP · Lv.11 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [61] = {
        .name = "Anthony",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_HIKER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 11,
                .species = SPECIES_GEODUDE,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 11,
                .species = SPECIES_MACHOP,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 9. Slowpoke Well

Team Rocket, fino a Proton.

### [101] Grunt

- **Progression role:** Team Rocket Grunt
- **Trainer class:** `TRAINERCLASS_TEAM_ROCKET`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `9
- **Party at a glance:**
  - RATTATA · Lv.9 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=30
  - RATTATA · Lv.9 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=30

#### Battle data — exact C

```c
    [101] = {
        .name = "Grunt",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_TEAM_ROCKET,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 9,
                .species = SPECIES_RATTATA,
                .ballSeal = 0,
            },
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 9,
                .species = SPECIES_RATTATA,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [13] Grunt

- **Progression role:** Team Rocket Grunt
- **Trainer class:** `TRAINERCLASS_TEAM_ROCKET_F`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `11
- **Party at a glance:**
  - ZUBAT · Lv.9 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30
  - EKANS · Lv.11 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30

#### Battle data — exact C

```c
    [13] = {
        .name = "Grunt",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_TEAM_ROCKET_F,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 9,
                .species = SPECIES_ZUBAT,
                .ballSeal = 0,
            },
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 11,
                .species = SPECIES_EKANS,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [12] Grunt

- **Progression role:** Team Rocket Grunt
- **Trainer class:** `TRAINERCLASS_TEAM_ROCKET`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `9
- **Party at a glance:**
  - RATTATA · Lv.7 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=30
  - ZUBAT · Lv.9 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30
  - ZUBAT · Lv.9 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30

#### Battle data — exact C

```c
    [12] = {
        .name = "Grunt",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_TEAM_ROCKET,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 7,
                .species = SPECIES_RATTATA,
                .ballSeal = 0,
            },
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 9,
                .species = SPECIES_ZUBAT,
                .ballSeal = 0,
            },
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 9,
                .species = SPECIES_ZUBAT,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [486] Proton

- **Progression role:** ROCKET EXECUTIVE / miniboss
- **Trainer class:** `TRAINERCLASS_EXECUTIVE_PROTON`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `12
- **Party at a glance:**
  - ZUBAT · Lv.8 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=100
  - KOFFING · Lv.12 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=100

#### Battle data — exact C

```c
    [486] = {
        .name = "Proton",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_EXECUTIVE_PROTON,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 8,
                .species = SPECIES_ZUBAT,
                .ballSeal = 0,
            },
            {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_KOFFING,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 10. Azalea Gym

La disposizione del puzzle può rendere l'ordine di alcuni trainer non rigidamente lineare.

### [67] Benny

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_BUG_CATCHER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `12
- **Party at a glance:**
  - WEEDLE · Lv.7 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - KAKUNA · Lv.9 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - BEEDRILL · Lv.12 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10

#### Battle data — exact C

```c
    [67] = {
        .name = "Benny",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_BUG_CATCHER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 7,
                .species = SPECIES_WEEDLE,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 9,
                .species = SPECIES_KAKUNA,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_BEEDRILL,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [10] Amy & Mimi

- **Progression role:** Gym trainer / double
- **Nota:** Nel trainer table esiste anche un duplicato/alias: verificare l'eventuale uso dell'ID [387] se si modifica lo script della mappa.
- **Trainer class:** `TRAINERCLASS_TWINS`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `DOUBLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `10
- **Party at a glance:**
  - SPINARAK · Lv.10 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=10
  - LEDYBA · Lv.10 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=10

#### Battle data — exact C

```c
    [10] = {
        .name = "Amy & Mimi",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_TWINS,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = DOUBLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 10,
                .species = SPECIES_SPINARAK,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 10,
                .species = SPECIES_LEDYBA,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [68] Al

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_BUG_CATCHER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `12
- **Party at a glance:**
  - CATERPIE · Lv.12 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - WEEDLE · Lv.12 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10

#### Battle data — exact C

```c
    [68] = {
        .name = "Al",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_BUG_CATCHER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_CATERPIE,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_WEEDLE,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [69] Josh

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_BUG_CATCHER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `13
- **Party at a glance:**
  - PARAS · Lv.13 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10

#### Battle data — exact C

```c
    [69] = {
        .name = "Josh",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_BUG_CATCHER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 13,
                .species = SPECIES_PARAS,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [21] Bugsy

- **Progression role:** GYM LEADER
- **Trainer class:** `TRAINERCLASS_LEADER_BUGSY`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES | TRAINER_DATA_TYPE_ITEMS`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_SUPER_POTION, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `17
- **Party at a glance:**
  - SCYTHER · Lv.17 · item=ITEM_SITRUS_BERRY · ability=TRAINER_POKEMON_ABILITY_2 · IVs=80 · moves=MOVE_QUICK_ATTACK, MOVE_LEER, MOVE_U_TURN, MOVE_FOCUS_ENERGY
  - KAKUNA · Lv.15 · item=ITEM_NONE · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_POISON_STING, MOVE_NONE, MOVE_NONE, MOVE_NONE
  - METAPOD · Lv.15 · item=ITEM_NONE · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_TACKLE, MOVE_NONE, MOVE_NONE, MOVE_NONE

#### Battle data — exact C

```c
    [21] = {
        .name = "Bugsy",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES | TRAINER_DATA_TYPE_ITEMS,
            .trainerClass = TRAINERCLASS_LEADER_BUGSY,
            .items = { ITEM_SUPER_POTION, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 17,
                .species = SPECIES_SCYTHER,
                .item = ITEM_SITRUS_BERRY,
                .moves = { MOVE_QUICK_ATTACK, MOVE_LEER, MOVE_U_TURN, MOVE_FOCUS_ENERGY },
                .ballSeal = 0,
            },
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 15,
                .species = SPECIES_KAKUNA,
                .item = ITEM_NONE,
                .moves = { MOVE_POISON_STING, MOVE_NONE, MOVE_NONE, MOVE_NONE },
                .ballSeal = 0,
            },
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 15,
                .species = SPECIES_METAPOD,
                .item = ITEM_NONE,
                .moves = { MOVE_TACKLE, MOVE_NONE, MOVE_NONE, MOVE_NONE },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 11. Silver — Azalea Town

Battaglia dopo Bugsy. Una sola variante viene usata in base allo starter.

### [1] Silver

- **Progression role:** Rival variant
- **Nota:** Linea Bayleef
- **Trainer class:** `TRAINERCLASS_RIVAL`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `18
- **Party at a glance:**
  - GASTLY · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30
  - ZUBAT · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30
  - BAYLEEF · Lv.18 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30

#### Battle data — exact C

```c
    [1] = {
        .name = "Silver",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_RIVAL,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_GASTLY,
                .ballSeal = 0,
            },
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_ZUBAT,
                .ballSeal = 0,
            },
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 18,
                .species = SPECIES_BAYLEEF,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [266] Silver

- **Progression role:** Rival variant
- **Nota:** Linea Quilava
- **Trainer class:** `TRAINERCLASS_RIVAL`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `18
- **Party at a glance:**
  - GASTLY · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30
  - ZUBAT · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30
  - QUILAVA · Lv.18 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30

#### Battle data — exact C

```c
    [266] = {
        .name = "Silver",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_RIVAL,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_GASTLY,
                .ballSeal = 0,
            },
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_ZUBAT,
                .ballSeal = 0,
            },
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 18,
                .species = SPECIES_QUILAVA,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [269] Silver

- **Progression role:** Rival variant
- **Nota:** Linea Croconaw
- **Trainer class:** `TRAINERCLASS_RIVAL`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `18
- **Party at a glance:**
  - GASTLY · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30
  - ZUBAT · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30
  - CROCONAW · Lv.18 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30

#### Battle data — exact C

```c
    [269] = {
        .name = "Silver",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_RIVAL,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_GASTLY,
                .ballSeal = 0,
            },
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_ZUBAT,
                .ballSeal = 0,
            },
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 18,
                .species = SPECIES_CROCONAW,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 12. Route 34

### [62] Samuel

- **Progression role:** Youngster
- **Trainer class:** `TRAINERCLASS_YOUNGSTER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `10
- **Party at a glance:**
  - RATTATA · Lv.7 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0
  - SANDSHREW · Lv.10 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - SPEAROW · Lv.8 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - SPEAROW · Lv.8 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [62] = {
        .name = "Samuel",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_YOUNGSTER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 7,
                .species = SPECIES_RATTATA,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 10,
                .species = SPECIES_SANDSHREW,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 8,
                .species = SPECIES_SPEAROW,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 8,
                .species = SPECIES_SPEAROW,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [409] Brandon

- **Progression role:** Pokéfan
- **Trainer class:** `TRAINERCLASS_POKEFAN_M`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `13
- **Party at a glance:**
  - SNUBBULL · Lv.13 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - MAREEP · Lv.13 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [409] = {
        .name = "Brandon",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_POKEFAN_M,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 13,
                .species = SPECIES_SNUBBULL,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 13,
                .species = SPECIES_MAREEP,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [65] Gina

- **Progression role:** Picnicker
- **Trainer class:** `TRAINERCLASS_PICNICKER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `12
- **Party at a glance:**
  - HOPPIP · Lv.9 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - HOPPIP · Lv.9 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - BULBASAUR · Lv.12 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [65] = {
        .name = "Gina",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_PICNICKER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 9,
                .species = SPECIES_HOPPIP,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 9,
                .species = SPECIES_HOPPIP,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_BULBASAUR,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [64] Ian

- **Progression role:** Youngster
- **Trainer class:** `TRAINERCLASS_YOUNGSTER`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `12
- **Party at a glance:**
  - MANKEY · Lv.10 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_FOCUS_ENERGY, MOVE_SCRATCH, MOVE_LOW_KICK, MOVE_LEER
  - DIGLETT · Lv.12 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_ASTONISH, MOVE_GROWL, MOVE_SCRATCH, MOVE_SAND_ATTACK

#### Battle data — exact C

```c
    [64] = {
        .name = "Ian",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_YOUNGSTER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 10,
                .species = SPECIES_MANKEY,
                .moves = { MOVE_FOCUS_ENERGY, MOVE_SCRATCH, MOVE_LOW_KICK, MOVE_LEER },
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_DIGLETT,
                .moves = { MOVE_ASTONISH, MOVE_GROWL, MOVE_SCRATCH, MOVE_SAND_ATTACK },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [6] Keith

- **Progression role:** Policeman
- **Nota:** NIGHT-ONLY
- **Trainer class:** `TRAINERCLASS_POLICEMAN`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `17
- **Party at a glance:**
  - GROWLITHE · Lv.17 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [6] = {
        .name = "Keith",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_POLICEMAN,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 17,
                .species = SPECIES_GROWLITHE,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [66] Todd

- **Progression role:** Camper
- **Trainer class:** `TRAINERCLASS_CAMPER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `14
- **Party at a glance:**
  - PSYDUCK · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [66] = {
        .name = "Todd",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_CAMPER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_PSYDUCK,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 13. Goldenrod Underground / Tunnel

OPTIONAL prima di Whitney; ordine dipendente dall'ingresso e dal percorso.

### [392] Donald

- **Progression role:** Poké Maniac
- **Nota:** OPTIONAL
- **Trainer class:** `TRAINERCLASS_POKE_MANIAC`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `11
- **Party at a glance:**
  - SLOWPOKE · Lv.11 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0
  - SLOWPOKE · Lv.11 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [392] = {
        .name = "Donald",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_POKE_MANIAC,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 11,
                .species = SPECIES_SLOWPOKE,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 11,
                .species = SPECIES_SLOWPOKE,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [393] Teru

- **Progression role:** Super Nerd
- **Nota:** OPTIONAL
- **Trainer class:** `TRAINERCLASS_SUPER_NERD`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `11
- **Party at a glance:**
  - MAGNEMITE · Lv.7 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - VOLTORB · Lv.11 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - MAGNEMITE · Lv.7 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0
  - MAGNEMITE · Lv.9 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [393] = {
        .name = "Teru",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_SUPER_NERD,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 7,
                .species = SPECIES_MAGNEMITE,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 11,
                .species = SPECIES_VOLTORB,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 7,
                .species = SPECIES_MAGNEMITE,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 9,
                .species = SPECIES_MAGNEMITE,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [391] Issac

- **Progression role:** Poké Maniac
- **Nota:** OPTIONAL
- **Trainer class:** `TRAINERCLASS_POKE_MANIAC`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `12
- **Party at a glance:**
  - LICKITUNG · Lv.12 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_LICK, MOVE_SUPERSONIC, MOVE_CUT, MOVE_NONE

#### Battle data — exact C

```c
    [391] = {
        .name = "Issac",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_POKE_MANIAC,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_LICKITUNG,
                .moves = { MOVE_LICK, MOVE_SUPERSONIC, MOVE_CUT, MOVE_NONE },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [233] Eric

- **Progression role:** Super Nerd
- **Nota:** OPTIONAL
- **Trainer class:** `TRAINERCLASS_SUPER_NERD`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `11
- **Party at a glance:**
  - GRIMER · Lv.11 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - GRIMER · Lv.11 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [233] = {
        .name = "Eric",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_SUPER_NERD,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 11,
                .species = SPECIES_GRIMER,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 11,
                .species = SPECIES_GRIMER,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 14. Goldenrod Gym

### [5] Victoria

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_BEAUTY`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `16
- **Party at a glance:**
  - SENTRET · Lv.9 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=10
  - SENTRET · Lv.13 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=10
  - SENTRET · Lv.16 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=10

#### Battle data — exact C

```c
    [5] = {
        .name = "Victoria",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_BEAUTY,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 9,
                .species = SPECIES_SENTRET,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 13,
                .species = SPECIES_SENTRET,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 16,
                .species = SPECIES_SENTRET,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [70] Samantha

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_BEAUTY`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `16
- **Party at a glance:**
  - MEOWTH · Lv.16 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=10 · moves=MOVE_SCRATCH, MOVE_GROWL, MOVE_BITE, MOVE_PAY_DAY
  - MEOWTH · Lv.16 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=10 · moves=MOVE_SCRATCH, MOVE_GROWL, MOVE_BITE, MOVE_SLASH

#### Battle data — exact C

```c
    [70] = {
        .name = "Samantha",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_BEAUTY,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 16,
                .species = SPECIES_MEOWTH,
                .moves = { MOVE_SCRATCH, MOVE_GROWL, MOVE_BITE, MOVE_PAY_DAY },
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 16,
                .species = SPECIES_MEOWTH,
                .moves = { MOVE_SCRATCH, MOVE_GROWL, MOVE_BITE, MOVE_SLASH },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [22] Carrie

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_LASS`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `17
- **Party at a glance:**
  - SNUBBULL · Lv.17 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10 · moves=MOVE_SCARY_FACE, MOVE_CHARM, MOVE_BITE, MOVE_LICK

#### Battle data — exact C

```c
    [22] = {
        .name = "Carrie",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_LASS,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 17,
                .species = SPECIES_SNUBBULL,
                .moves = { MOVE_SCARY_FACE, MOVE_CHARM, MOVE_BITE, MOVE_LICK },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [71] Cathy

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_LASS`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `15
- **Party at a glance:**
  - JIGGLYPUFF · Lv.15 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - JIGGLYPUFF · Lv.15 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - JIGGLYPUFF · Lv.15 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10

#### Battle data — exact C

```c
    [71] = {
        .name = "Cathy",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_LASS,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 15,
                .species = SPECIES_JIGGLYPUFF,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 15,
                .species = SPECIES_JIGGLYPUFF,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 15,
                .species = SPECIES_JIGGLYPUFF,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [30] Whitney

- **Progression role:** GYM LEADER
- **Trainer class:** `TRAINERCLASS_LEADER_WHITNEY`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES | TRAINER_DATA_TYPE_ITEMS`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_SUPER_POTION, ITEM_SUPER_POTION, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `19
- **Party at a glance:**
  - CLEFAIRY · Lv.17 · item=ITEM_NONE · ability=TRAINER_POKEMON_ABILITY_1 · IVs=100 · moves=MOVE_DOUBLE_SLAP, MOVE_MIMIC, MOVE_ENCORE, MOVE_METRONOME
  - MILTANK · Lv.19 · item=ITEM_LUM_BERRY · ability=TRAINER_POKEMON_ABILITY_2 · IVs=100 · moves=MOVE_ROLLOUT, MOVE_ATTRACT, MOVE_STOMP, MOVE_MILK_DRINK

#### Battle data — exact C

```c
    [30] = {
        .name = "Whitney",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES | TRAINER_DATA_TYPE_ITEMS,
            .trainerClass = TRAINERCLASS_LEADER_WHITNEY,
            .items = { ITEM_SUPER_POTION, ITEM_SUPER_POTION, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 17,
                .species = SPECIES_CLEFAIRY,
                .item = ITEM_NONE,
                .moves = { MOVE_DOUBLE_SLAP, MOVE_MIMIC, MOVE_ENCORE, MOVE_METRONOME },
                .ballSeal = 0,
            },
            {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 19,
                .species = SPECIES_MILTANK,
                .item = ITEM_LUM_BERRY,
                .moves = { MOVE_ROLLOUT, MOVE_ATTRACT, MOVE_STOMP, MOVE_MILK_DRINK },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 15. Route 35

### [77] Kim

- **Progression role:** Picnicker
- **Trainer class:** `TRAINERCLASS_PICNICKER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `15
- **Party at a glance:**
  - VULPIX · Lv.15 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [77] = {
        .name = "Kim",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_PICNICKER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 15,
                .species = SPECIES_VULPIX,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [75] Elliot

- **Progression role:** Camper
- **Trainer class:** `TRAINERCLASS_CAMPER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `15
- **Party at a glance:**
  - SANDSHREW · Lv.13 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - MARILL · Lv.15 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [75] = {
        .name = "Elliot",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_CAMPER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 13,
                .species = SPECIES_SANDSHREW,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 15,
                .species = SPECIES_MARILL,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [76] Brooke

- **Progression role:** Picnicker
- **Trainer class:** `TRAINERCLASS_PICNICKER`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `16
- **Party at a glance:**
  - PIKACHU · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_THUNDER_SHOCK, MOVE_GROWL, MOVE_QUICK_ATTACK, MOVE_DOUBLE_TEAM

#### Battle data — exact C

```c
    [76] = {
        .name = "Brooke",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_PICNICKER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_PIKACHU,
                .moves = { MOVE_THUNDER_SHOCK, MOVE_GROWL, MOVE_QUICK_ATTACK, MOVE_DOUBLE_TEAM },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [74] Ivan

- **Progression role:** Camper
- **Trainer class:** `TRAINERCLASS_CAMPER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `14
- **Party at a glance:**
  - DIGLETT · Lv.10 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - ZUBAT · Lv.10 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - DIGLETT · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [74] = {
        .name = "Ivan",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_CAMPER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 10,
                .species = SPECIES_DIGLETT,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 10,
                .species = SPECIES_ZUBAT,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_DIGLETT,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [7] Irwin

- **Progression role:** Juggler
- **Trainer class:** `TRAINERCLASS_JUGGLER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `14
- **Party at a glance:**
  - VOLTORB · Lv.2 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - VOLTORB · Lv.6 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0
  - VOLTORB · Lv.10 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - VOLTORB · Lv.14 · ability=TRAINER_POKEMON_ABILITY_2 · IVs=0

#### Battle data — exact C

```c
    [7] = {
        .name = "Irwin",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_JUGGLER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 2,
                .species = SPECIES_VOLTORB,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 6,
                .species = SPECIES_VOLTORB,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 10,
                .species = SPECIES_VOLTORB,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_2,
                .level = 14,
                .species = SPECIES_VOLTORB,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [388] Walt

- **Progression role:** Firebreather
- **Trainer class:** `TRAINERCLASS_FIREBREATHER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `16
- **Party at a glance:**
  - MAGMAR · Lv.11 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - MAGMAR · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [388] = {
        .name = "Walt",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_FIREBREATHER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 11,
                .species = SPECIES_MAGMAR,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_MAGMAR,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [80] Dirk

- **Progression role:** Policeman
- **Nota:** NIGHT-ONLY
- **Trainer class:** `TRAINERCLASS_POLICEMAN`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `14
- **Party at a glance:**
  - GROWLITHE · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - GROWLITHE · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [80] = {
        .name = "Dirk",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_POLICEMAN,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_GROWLITHE,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_GROWLITHE,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [78] Arnie

- **Progression role:** Bug Catcher
- **Trainer class:** `TRAINERCLASS_BUG_CATCHER`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `15
- **Party at a glance:**
  - VENONAT · Lv.15 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [78] = {
        .name = "Arnie",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_BUG_CATCHER,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 15,
                .species = SPECIES_VENONAT,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [72] Bryan

- **Progression role:** Bird Keeper
- **Trainer class:** `TRAINERCLASS_BIRD_KEEPER_GS`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `14
- **Party at a glance:**
  - PIDGEY · Lv.12 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=50
  - PIDGEOTTO · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=50

#### Battle data — exact C

```c
    [72] = {
        .name = "Bryan",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_BIRD_KEEPER_GS,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 50,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_PIDGEY,
                .ballSeal = 0,
            },
            {
                .ivs = 50,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_PIDGEOTTO,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 16. National Park

Path/exploration dependent; useful to considerare nella curva anche se alcuni possono essere evitati.

### [182] Beverly

- **Progression role:** Pokéfan
- **Nota:** OPTIONAL/PATH-DEPENDENT
- **Trainer class:** `TRAINERCLASS_POKEFAN`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `16
- **Party at a glance:**
  - SNUBBULL · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [182] = {
        .name = "Beverly",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_POKEFAN,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_SNUBBULL,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [181] William

- **Progression role:** Pokéfan
- **Nota:** OPTIONAL/PATH-DEPENDENT
- **Trainer class:** `TRAINERCLASS_POKEFAN_M`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `16
- **Party at a glance:**
  - RAICHU · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [181] = {
        .name = "William",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_POKEFAN_M,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_RAICHU,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [178] Jack

- **Progression role:** School Kid
- **Nota:** OPTIONAL/PATH-DEPENDENT
- **Trainer class:** `TRAINERCLASS_SCHOOL_KID_M`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `15
- **Party at a glance:**
  - ODDISH · Lv.12 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - VOLTORB · Lv.15 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [178] = {
        .name = "Jack",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_SCHOOL_KID_M,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 12,
                .species = SPECIES_ODDISH,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 15,
                .species = SPECIES_VOLTORB,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [184] Krise

- **Progression role:** Lass
- **Nota:** OPTIONAL/PATH-DEPENDENT
- **Trainer class:** `TRAINERCLASS_LASS`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `17
- **Party at a glance:**
  - ODDISH · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - CUBONE · Lv.17 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [184] = {
        .name = "Krise",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_LASS,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_ODDISH,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 17,
                .species = SPECIES_CUBONE,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 17. Route 36

### [395] Mark

- **Progression role:** Psychic
- **Trainer class:** `TRAINERCLASS_PSYCHIC_M`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `16
- **Party at a glance:**
  - ABRA · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_TELEPORT, MOVE_FLASH, MOVE_NONE, MOVE_NONE
  - ABRA · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_TELEPORT, MOVE_FLASH, MOVE_NONE, MOVE_NONE
  - KADABRA · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_TELEPORT, MOVE_KINESIS, MOVE_CONFUSION, MOVE_NONE

#### Battle data — exact C

```c
    [395] = {
        .name = "Mark",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_PSYCHIC_M,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_ABRA,
                .moves = { MOVE_TELEPORT, MOVE_FLASH, MOVE_NONE, MOVE_NONE },
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_ABRA,
                .moves = { MOVE_TELEPORT, MOVE_FLASH, MOVE_NONE, MOVE_NONE },
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_KADABRA,
                .moves = { MOVE_TELEPORT, MOVE_KINESIS, MOVE_CONFUSION, MOVE_NONE },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [24] Alan

- **Progression role:** School Kid
- **Trainer class:** `TRAINERCLASS_SCHOOL_KID_M`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `17
- **Party at a glance:**
  - TANGELA · Lv.17 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [24] = {
        .name = "Alan",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_SCHOOL_KID_M,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 17,
                .species = SPECIES_TANGELA,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 18. Route 37

### [81] Tori & Til

- **Progression role:** Twins / double
- **Trainer class:** `TRAINERCLASS_TWINS`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `DOUBLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `16
- **Party at a glance:**
  - MARILL · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0
  - MAREEP · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0

#### Battle data — exact C

```c
    [81] = {
        .name = "Tori & Til",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_TWINS,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = DOUBLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_MARILL,
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_MAREEP,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [679] Callie

- **Progression role:** Beauty / paired double
- **Trainer class:** `TRAINERCLASS_BEAUTY`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `16
- **Party at a glance:**
  - CLEFABLE · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_GROWL, MOVE_ENCORE, MOVE_DOUBLE_SLAP, MOVE_METRONOME
  - WIGGLYTUFF · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_SING, MOVE_DEFENSE_CURL, MOVE_POUND, MOVE_DISABLE

#### Battle data — exact C

```c
    [679] = {
        .name = "Callie",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_BEAUTY,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_CLEFABLE,
                .moves = { MOVE_GROWL, MOVE_ENCORE, MOVE_DOUBLE_SLAP, MOVE_METRONOME },
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_WIGGLYTUFF,
                .moves = { MOVE_SING, MOVE_DEFENSE_CURL, MOVE_POUND, MOVE_DISABLE },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [680] Kassandra

- **Progression role:** Beauty / paired double
- **Trainer class:** `TRAINERCLASS_BEAUTY`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `16
- **Party at a glance:**
  - WIGGLYTUFF · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_SING, MOVE_DEFENSE_CURL, MOVE_POUND, MOVE_DISABLE
  - CLEFABLE · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_GROWL, MOVE_ENCORE, MOVE_DOUBLE_SLAP, MOVE_METRONOME

#### Battle data — exact C

```c
    [680] = {
        .name = "Kassandra",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_BEAUTY,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_WIGGLYTUFF,
                .moves = { MOVE_SING, MOVE_DEFENSE_CURL, MOVE_POUND, MOVE_DISABLE },
                .ballSeal = 0,
            },
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_CLEFABLE,
                .moves = { MOVE_GROWL, MOVE_ENCORE, MOVE_DOUBLE_SLAP, MOVE_METRONOME },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [386] Greg

- **Progression role:** Psychic
- **Trainer class:** `TRAINERCLASS_PSYCHIC_M`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `17
- **Party at a glance:**
  - DROWZEE · Lv.17 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=0 · moves=MOVE_HYPNOSIS, MOVE_DISABLE, MOVE_DREAM_EATER, MOVE_NONE

#### Battle data — exact C

```c
    [386] = {
        .name = "Greg",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_PSYCHIC_M,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 0,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 17,
                .species = SPECIES_DROWZEE,
                .moves = { MOVE_HYPNOSIS, MOVE_DISABLE, MOVE_DREAM_EATER, MOVE_NONE },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 19. Ecruteak Dance Theater

Scontro Rocket collegato all'ottenimento di Surf.

### [63] Mickey

- **Progression role:** Team Rocket Grunt / miniboss candidate
- **Trainer class:** `TRAINERCLASS_TEAM_ROCKET`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE`
- **Ace / max level:** `14
- **Party at a glance:**
  - KOFFING · Lv.14 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=30

#### Battle data — exact C

```c
    [63] = {
        .name = "Mickey",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_TEAM_ROCKET,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 30,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 14,
                .species = SPECIES_KOFFING,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 20. Burned Tower — Silver

Battaglia prima di Morty. Una sola variante viene usata in base allo starter.

### [263] Silver

- **Progression role:** Rival variant
- **Nota:** Linea Bayleef
- **Trainer class:** `TRAINERCLASS_RIVAL`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `22
- **Party at a glance:**
  - GASTLY · Lv.20 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_LICK, MOVE_CONFUSE_RAY, MOVE_MEAN_LOOK, MOVE_CURSE
  - MAGNEMITE · Lv.18 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_THUNDER_WAVE, MOVE_THUNDER_SHOCK, MOVE_SUPERSONIC, MOVE_SONIC_BOOM
  - ZUBAT · Lv.20 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_ASTONISH, MOVE_SUPERSONIC, MOVE_BITE, MOVE_WING_ATTACK
  - BAYLEEF · Lv.22 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_SYNTHESIS, MOVE_REFLECT, MOVE_MAGICAL_LEAF, MOVE_POISON_POWDER

#### Battle data — exact C

```c
    [263] = {
        .name = "Silver",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_RIVAL,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 20,
                .species = SPECIES_GASTLY,
                .moves = { MOVE_LICK, MOVE_CONFUSE_RAY, MOVE_MEAN_LOOK, MOVE_CURSE },
                .ballSeal = 0,
            },
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 18,
                .species = SPECIES_MAGNEMITE,
                .moves = { MOVE_THUNDER_WAVE, MOVE_THUNDER_SHOCK, MOVE_SUPERSONIC, MOVE_SONIC_BOOM },
                .ballSeal = 0,
            },
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 20,
                .species = SPECIES_ZUBAT,
                .moves = { MOVE_ASTONISH, MOVE_SUPERSONIC, MOVE_BITE, MOVE_WING_ATTACK },
                .ballSeal = 0,
            },
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 22,
                .species = SPECIES_BAYLEEF,
                .moves = { MOVE_SYNTHESIS, MOVE_REFLECT, MOVE_MAGICAL_LEAF, MOVE_POISON_POWDER },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [267] Silver

- **Progression role:** Rival variant
- **Nota:** Linea Quilava
- **Trainer class:** `TRAINERCLASS_RIVAL`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `22
- **Party at a glance:**
  - GASTLY · Lv.20 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_LICK, MOVE_CONFUSE_RAY, MOVE_MEAN_LOOK, MOVE_CURSE
  - MAGNEMITE · Lv.18 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_THUNDER_WAVE, MOVE_THUNDER_SHOCK, MOVE_SUPERSONIC, MOVE_SONIC_BOOM
  - ZUBAT · Lv.20 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_ASTONISH, MOVE_SUPERSONIC, MOVE_BITE, MOVE_WING_ATTACK
  - QUILAVA · Lv.22 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_FLAME_WHEEL, MOVE_SMOKESCREEN, MOVE_EMBER, MOVE_QUICK_ATTACK

#### Battle data — exact C

```c
    [267] = {
        .name = "Silver",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_RIVAL,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 20,
                .species = SPECIES_GASTLY,
                .moves = { MOVE_LICK, MOVE_CONFUSE_RAY, MOVE_MEAN_LOOK, MOVE_CURSE },
                .ballSeal = 0,
            },
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 18,
                .species = SPECIES_MAGNEMITE,
                .moves = { MOVE_THUNDER_WAVE, MOVE_THUNDER_SHOCK, MOVE_SUPERSONIC, MOVE_SONIC_BOOM },
                .ballSeal = 0,
            },
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 20,
                .species = SPECIES_ZUBAT,
                .moves = { MOVE_ASTONISH, MOVE_SUPERSONIC, MOVE_BITE, MOVE_WING_ATTACK },
                .ballSeal = 0,
            },
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 22,
                .species = SPECIES_QUILAVA,
                .moves = { MOVE_FLAME_WHEEL, MOVE_SMOKESCREEN, MOVE_EMBER, MOVE_QUICK_ATTACK },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [270] Silver

- **Progression role:** Rival variant
- **Nota:** Linea Croconaw
- **Trainer class:** `TRAINERCLASS_RIVAL`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE`
- **Ace / max level:** `22
- **Party at a glance:**
  - GASTLY · Lv.20 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_LICK, MOVE_CONFUSE_RAY, MOVE_MEAN_LOOK, MOVE_CURSE
  - MAGNEMITE · Lv.18 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_THUNDER_WAVE, MOVE_THUNDER_SHOCK, MOVE_SUPERSONIC, MOVE_SONIC_BOOM
  - ZUBAT · Lv.20 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_ASTONISH, MOVE_SUPERSONIC, MOVE_BITE, MOVE_WING_ATTACK
  - CROCONAW · Lv.22 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=80 · moves=MOVE_SCARY_FACE, MOVE_ICE_FANG, MOVE_WATER_GUN, MOVE_BITE

#### Battle data — exact C

```c
    [270] = {
        .name = "Silver",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES,
            .trainerClass = TRAINERCLASS_RIVAL,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_PRIORITIZE_DAMAGE,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 20,
                .species = SPECIES_GASTLY,
                .moves = { MOVE_LICK, MOVE_CONFUSE_RAY, MOVE_MEAN_LOOK, MOVE_CURSE },
                .ballSeal = 0,
            },
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 18,
                .species = SPECIES_MAGNEMITE,
                .moves = { MOVE_THUNDER_WAVE, MOVE_THUNDER_SHOCK, MOVE_SUPERSONIC, MOVE_SONIC_BOOM },
                .ballSeal = 0,
            },
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 20,
                .species = SPECIES_ZUBAT,
                .moves = { MOVE_ASTONISH, MOVE_SUPERSONIC, MOVE_BITE, MOVE_WING_ATTACK },
                .ballSeal = 0,
            },
            {
                .ivs = 80,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 22,
                .species = SPECIES_CROCONAW,
                .moves = { MOVE_SCARY_FACE, MOVE_ICE_FANG, MOVE_WATER_GUN, MOVE_BITE },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## 21. Ecruteak Gym

### [494] Georgina

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_MEDIUM`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `16
- **Party at a glance:**
  - GASTLY · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - GASTLY · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - GASTLY · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - GASTLY · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - GASTLY · Lv.16 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10

#### Battle data — exact C

```c
    [494] = {
        .name = "Georgina",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_MEDIUM,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_GASTLY,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_GASTLY,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_GASTLY,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_GASTLY,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 16,
                .species = SPECIES_GASTLY,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [89] Grace

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_MEDIUM`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `20
- **Party at a glance:**
  - HAUNTER · Lv.20 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - HAUNTER · Lv.20 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10

#### Battle data — exact C

```c
    [89] = {
        .name = "Grace",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_MEDIUM,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 20,
                .species = SPECIES_HAUNTER,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 20,
                .species = SPECIES_HAUNTER,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [493] Edith

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_MEDIUM`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `22
- **Party at a glance:**
  - HAUNTER · Lv.22 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10

#### Battle data — exact C

```c
    [493] = {
        .name = "Edith",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_MEDIUM,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 22,
                .species = SPECIES_HAUNTER,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [46] Martha

- **Progression role:** Gym trainer
- **Trainer class:** `TRAINERCLASS_MEDIUM`
- **Trainer data type:** `TRAINER_DATA_TYPE_NOTHING`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS`
- **Ace / max level:** `20
- **Party at a glance:**
  - GASTLY · Lv.18 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - HAUNTER · Lv.20 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10
  - GASTLY · Lv.20 · ability=TRAINER_POKEMON_ABILITY_1 · IVs=10

#### Battle data — exact C

```c
    [46] = {
        .name = "Martha",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_NOTHING,
            .trainerClass = TRAINERCLASS_MEDIUM,
            .items = { ITEM_NONE, ITEM_NONE, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 18,
                .species = SPECIES_GASTLY,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 20,
                .species = SPECIES_HAUNTER,
                .ballSeal = 0,
            },
            {
                .ivs = 10,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 20,
                .species = SPECIES_GASTLY,
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

### [31] Morty

- **Progression role:** GYM LEADER
- **Trainer class:** `TRAINERCLASS_LEADER_MORTY`
- **Trainer data type:** `TRAINER_DATA_TYPE_MOVES | TRAINER_DATA_TYPE_ITEMS`
- **Battle type:** `SINGLE_BATTLE`
- **Trainer items:** `{ ITEM_HYPER_POTION, ITEM_HYPER_POTION, ITEM_NONE, ITEM_NONE }`
- **AI flags:** `F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS`
- **Ace / max level:** `25
- **Party at a glance:**
  - GASTLY · Lv.21 · item=ITEM_NONE · ability=TRAINER_POKEMON_ABILITY_1 · IVs=100 · moves=MOVE_LICK, MOVE_SPITE, MOVE_MEAN_LOOK, MOVE_CURSE
  - HAUNTER · Lv.21 · item=ITEM_NONE · ability=TRAINER_POKEMON_ABILITY_1 · IVs=100 · moves=MOVE_HYPNOSIS, MOVE_DREAM_EATER, MOVE_CURSE, MOVE_NIGHTMARE
  - GENGAR · Lv.25 · item=ITEM_SITRUS_BERRY · ability=TRAINER_POKEMON_ABILITY_1 · IVs=100 · moves=MOVE_HYPNOSIS, MOVE_SHADOW_BALL, MOVE_MEAN_LOOK, MOVE_SUCKER_PUNCH
  - HAUNTER · Lv.23 · item=ITEM_NONE · ability=TRAINER_POKEMON_ABILITY_1 · IVs=100 · moves=MOVE_CURSE, MOVE_MEAN_LOOK, MOVE_SUCKER_PUNCH, MOVE_NIGHT_SHADE

#### Battle data — exact C

```c
    [31] = {
        .name = "Morty",
        .data = {
            .trainerType = TRAINER_DATA_TYPE_MOVES | TRAINER_DATA_TYPE_ITEMS,
            .trainerClass = TRAINERCLASS_LEADER_MORTY,
            .items = { ITEM_HYPER_POTION, ITEM_HYPER_POTION, ITEM_NONE, ITEM_NONE },
            .aiFlags = F_PRIORITIZE_SUPER_EFFECTIVE | F_EVALUATE_ATTACKS | F_EXPERT_ATTACKS,
            .battleType = SINGLE_BATTLE,
        },
        .party = {
            {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 21,
                .species = SPECIES_GASTLY,
                .item = ITEM_NONE,
                .moves = { MOVE_LICK, MOVE_SPITE, MOVE_MEAN_LOOK, MOVE_CURSE },
                .ballSeal = 0,
            },
            {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 21,
                .species = SPECIES_HAUNTER,
                .item = ITEM_NONE,
                .moves = { MOVE_HYPNOSIS, MOVE_DREAM_EATER, MOVE_CURSE, MOVE_NIGHTMARE },
                .ballSeal = 0,
            },
            {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 25,
                .species = SPECIES_GENGAR,
                .item = ITEM_SITRUS_BERRY,
                .moves = { MOVE_HYPNOSIS, MOVE_SHADOW_BALL, MOVE_MEAN_LOOK, MOVE_SUCKER_PUNCH },
                .ballSeal = 0,
            },
            {
                .ivs = 100,
                .abilitySlot = TRAINER_POKEMON_ABILITY_1,
                .level = 23,
                .species = SPECIES_HAUNTER,
                .item = ITEM_NONE,
                .moves = { MOVE_CURSE, MOVE_MEAN_LOOK, MOVE_SUCKER_PUNCH, MOVE_NIGHT_SHADE },
                .ballSeal = 0,
            },
        },
    },
```

#### HeartGold Modern — worklog

- **Decisione:** ☐ keep ☐ rebalance ☐ redesign ☐ miniboss
- **Target level / ace:**
- **Nuovo party / setup:**
- **AI / held items / ability / IV-EV changes:**
- **Razionale di design:**
- **Test status:** ☐ non testato ☐ compila ☐ testato in-game
- **Note:**

---

## Generator diagnostics

- Missing trainer IDs: none
- Name warnings:
  - [47] expected 'Mikey', got 'Pippo Franco'

> Se HG-Engine viene aggiornato, rigenera questo file e confrontalo con Git invece di correggere manualmente la baseline.
