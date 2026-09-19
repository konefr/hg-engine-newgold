.nds
.thumb

.include "armips/include/scriptmacros.s"
.include "armips/include/vars.s"

// New Gold - Bug-Catching Contest reward patch
//
// scr_seq_0151 is not decompiled in hg-engine. Patch the extracted binary
// directly instead of replacing the whole script.
//
// Vanilla at 0x354:
//   JudgeBugContest VAR_TEMP_x4000, VAR_TEMP_x4001, VAR_TEMP_x4002
// Vanilla resumes at 0x35C with GetPlayerCoords.
//
// JudgeBugContest returns:
//   VAR_TEMP_x4000 = placement (0 first, 1 second, 2 third, 3 other)
//   VAR_TEMP_x4001 = prize item
//   VAR_TEMP_x4002 = caught species
//
// We preserve the vanilla judging logic and overwrite only VAR_TEMP_x4001.

// Item IDs from include/constants/item.h.
ITEM_SUN_STONE       equ 80
ITEM_MOON_STONE      equ 81
ITEM_FIRE_STONE      equ 82
ITEM_THUNDER_STONE   equ 83
ITEM_WATER_STONE     equ 84
ITEM_LEAF_STONE      equ 85
ITEM_SHINY_STONE     equ 107
ITEM_DUSK_STONE      equ 108
ITEM_DAWN_STONE      equ 109
ITEM_DEEP_SEA_TOOTH  equ 226
ITEM_DEEP_SEA_SCALE  equ 227
ITEM_DRAGON_SCALE    equ 235
ITEM_UP_GRADE        equ 252
ITEM_PROTECTOR       equ 321
ITEM_ELECTIRIZER     equ 322
ITEM_MAGMARIZER      equ 323
ITEM_DUBIOUS_DISC    equ 324
ITEM_REAPER_CLOTH    equ 325
ITEM_RAZOR_CLAW      equ 326
ITEM_PRISM_SCALE     equ 537
ITEM_ICE_STONE       equ 849
ITEM_LINKING_CORD    equ 1611
ITEM_PEAT_BLOCK      equ 1692

.open "build/a012/2_151", 0

// Replace the original 8-byte JudgeBugContest command with a trampoline.
// goto is 6 bytes; the final halfword is unreachable padding.
.orga 0x354
    goto NewGold_BugContestHook
    .halfword 0

// Original file ends at 0x848. Append the New Gold hook and prize routine.
.orga 0x848

NewGold_BugContestHook:
    JudgeBugContest VAR_TEMP_x4000, VAR_TEMP_x4001, VAR_TEMP_x4002
    call NewGold_BugContestPrize
    goto 0x35C

NewGold_BugContestPrize:
    compare VAR_TEMP_x4000, 0
    goto_if_eq BugPrize_First

    compare VAR_TEMP_x4000, 1
    goto_if_eq BugPrize_Second

    compare VAR_TEMP_x4000, 2
    goto_if_eq BugPrize_Third

    goto BugPrize_Consolation

// 1st place: rare/special evolution items, 20% each.
BugPrize_First:
    random VAR_SPECIAL_RESULT, 5
    compare VAR_SPECIAL_RESULT, 0
    goto_if_eq BugPrize_ReaperCloth
    compare VAR_SPECIAL_RESULT, 1
    goto_if_eq BugPrize_Electirizer
    compare VAR_SPECIAL_RESULT, 2
    goto_if_eq BugPrize_Magmarizer
    compare VAR_SPECIAL_RESULT, 3
    goto_if_eq BugPrize_DubiousDisc

    setvar VAR_TEMP_x4001, ITEM_PEAT_BLOCK
    return

BugPrize_ReaperCloth:
    setvar VAR_TEMP_x4001, ITEM_REAPER_CLOTH
    return

BugPrize_Electirizer:
    setvar VAR_TEMP_x4001, ITEM_ELECTIRIZER
    return

BugPrize_Magmarizer:
    setvar VAR_TEMP_x4001, ITEM_MAGMARIZER
    return

BugPrize_DubiousDisc:
    setvar VAR_TEMP_x4001, ITEM_DUBIOUS_DISC
    return

// 2nd place: broad rare evolution-item pool, 10% each.
BugPrize_Second:
    random VAR_SPECIAL_RESULT, 10
    compare VAR_SPECIAL_RESULT, 0
    goto_if_eq BugPrize_ShinyStone
    compare VAR_SPECIAL_RESULT, 1
    goto_if_eq BugPrize_DuskStone
    compare VAR_SPECIAL_RESULT, 2
    goto_if_eq BugPrize_DawnStone
    compare VAR_SPECIAL_RESULT, 3
    goto_if_eq BugPrize_RazorClaw
    compare VAR_SPECIAL_RESULT, 4
    goto_if_eq BugPrize_DragonScale
    compare VAR_SPECIAL_RESULT, 5
    goto_if_eq BugPrize_PrismScale
    compare VAR_SPECIAL_RESULT, 6
    goto_if_eq BugPrize_UpGrade
    compare VAR_SPECIAL_RESULT, 7
    goto_if_eq BugPrize_DeepSeaTooth
    compare VAR_SPECIAL_RESULT, 8
    goto_if_eq BugPrize_DeepSeaScale

    setvar VAR_TEMP_x4001, ITEM_PROTECTOR
    return

BugPrize_ShinyStone:
    setvar VAR_TEMP_x4001, ITEM_SHINY_STONE
    return

BugPrize_DuskStone:
    setvar VAR_TEMP_x4001, ITEM_DUSK_STONE
    return

BugPrize_DawnStone:
    setvar VAR_TEMP_x4001, ITEM_DAWN_STONE
    return

BugPrize_RazorClaw:
    setvar VAR_TEMP_x4001, ITEM_RAZOR_CLAW
    return

BugPrize_DragonScale:
    setvar VAR_TEMP_x4001, ITEM_DRAGON_SCALE
    return

BugPrize_PrismScale:
    setvar VAR_TEMP_x4001, ITEM_PRISM_SCALE
    return

BugPrize_UpGrade:
    setvar VAR_TEMP_x4001, ITEM_UP_GRADE
    return

BugPrize_DeepSeaTooth:
    setvar VAR_TEMP_x4001, ITEM_DEEP_SEA_TOOTH
    return

BugPrize_DeepSeaScale:
    setvar VAR_TEMP_x4001, ITEM_DEEP_SEA_SCALE
    return

// 3rd place: guaranteed trade-evolution alternative.
BugPrize_Third:
    setvar VAR_TEMP_x4001, ITEM_LINKING_CORD
    return

// Outside the podium: one standard evolution stone, 1/7 each.
BugPrize_Consolation:
    random VAR_SPECIAL_RESULT, 7
    compare VAR_SPECIAL_RESULT, 0
    goto_if_eq BugPrize_SunStone
    compare VAR_SPECIAL_RESULT, 1
    goto_if_eq BugPrize_MoonStone
    compare VAR_SPECIAL_RESULT, 2
    goto_if_eq BugPrize_FireStone
    compare VAR_SPECIAL_RESULT, 3
    goto_if_eq BugPrize_ThunderStone
    compare VAR_SPECIAL_RESULT, 4
    goto_if_eq BugPrize_WaterStone
    compare VAR_SPECIAL_RESULT, 5
    goto_if_eq BugPrize_LeafStone

    setvar VAR_TEMP_x4001, ITEM_ICE_STONE
    return

BugPrize_SunStone:
    setvar VAR_TEMP_x4001, ITEM_SUN_STONE
    return

BugPrize_MoonStone:
    setvar VAR_TEMP_x4001, ITEM_MOON_STONE
    return

BugPrize_FireStone:
    setvar VAR_TEMP_x4001, ITEM_FIRE_STONE
    return

BugPrize_ThunderStone:
    setvar VAR_TEMP_x4001, ITEM_THUNDER_STONE
    return

BugPrize_WaterStone:
    setvar VAR_TEMP_x4001, ITEM_WATER_STONE
    return

BugPrize_LeafStone:
    setvar VAR_TEMP_x4001, ITEM_LEAF_STONE
    return

.close
