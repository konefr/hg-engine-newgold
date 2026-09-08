#include "config.h"
#include "debug.h"
#include "types.h"

#include "constants/ability.h"
#include "constants/file.h"
#include "constants/game.h"
#include "constants/generated/learnsets.h"
#include "constants/hold_item_effects.h"
#include "constants/item.h"
#include "constants/moves.h"
#include "constants/species.h"
#include "constants/weather_numbers.h"

#include "bag.h"
#include "battle.h"
#include "message.h"
#include "pokemon.h"
#include "rtc.h"
#include "save.h"
#include "script.h"

void SetupAndStartTotemBattle(TaskManager *taskManager, u16 species, u8 level, u32 *winFlag, BOOL shiny);

/**
 *  @brief script command to give an egg adapted to set the hidden ability
 *
 *  @param ctx script context structure
 *  @return FALSE
 */

#define DEV_EV_PRESET_RESET              2000
#define DEV_EV_PRESET_PHYSICAL           2001
#define DEV_EV_PRESET_SPECIAL            2002
#define DEV_EV_PRESET_PHYS_TANK          2003
#define DEV_EV_PRESET_SP_TANK            2004
#define DEV_EV_PRESET_BALANCED           2005
#define DEV_EV_PRESET_BULK_PHYSICAL      2006
#define DEV_EV_PRESET_BULK_SPECIAL       2007
#define DEV_EV_PRESET_MIXED_TANK         2008
#define DEV_EV_PRESET_FAST_BULK_PHYS     2009
#define DEV_EV_PRESET_FAST_BULK_SPECIAL  2010
#define DEV_EV_PRESET_FAST_BULK     2011


BOOL ScrCmd_GiveEgg(SCRIPTCONTEXT *ctx)
{
    FieldSystem *fsys = ctx->fsys;
    void *profile = Sav2_PlayerData_GetProfileAddr(fsys->savedata);

    // Read both script arguments first.
    u16 species = ScriptGetVar(ctx);
    u16 offset = ScriptGetVar(ctx);

    // Developer-only EV presets.
        // Values 2000-2011 are deliberately invalid Pokémon species IDs.
    if (species >= DEV_EV_PRESET_RESET &&
        species <= DEV_EV_PRESET_FAST_BULK)
    {
        struct Party *party = SaveData_GetPlayerPartyPtr(fsys->savedata);

        if (party->count == 0) {
            return FALSE;
        }

        // Developer EV editor always affects the first Pokémon in the party.
        struct PartyPokemon *pokemon = Party_GetMonByIndex(party, 0);

        if (pokemon == NULL ||
            GetMonData(pokemon, MON_DATA_IS_EGG, NULL))
        {
            return FALSE;
        }

        // Order:
        // HP, Attack, Defense, Speed, Special Attack, Special Defense
        u8 evs[6] = {0, 0, 0, 0, 0, 0};

        switch (species) {
        case DEV_EV_PRESET_PHYSICAL:
            // 252 Atk / 252 Spe / 4 HP
            evs[0] = 4;
            evs[1] = 252;
            evs[3] = 252;
            break;

        case DEV_EV_PRESET_SPECIAL:
            // 252 SpA / 252 Spe / 4 HP
            evs[0] = 4;
            evs[3] = 252;
            evs[4] = 252;
            break;

        case DEV_EV_PRESET_PHYS_TANK:
            // 252 HP / 252 Def / 4 SpDef
            evs[0] = 252;
            evs[2] = 252;
            evs[5] = 4;
            break;

        case DEV_EV_PRESET_SP_TANK:
            // 252 HP / 252 SpDef / 4 Def
            evs[0] = 252;
            evs[2] = 4;
            evs[5] = 252;
            break;

        case DEV_EV_PRESET_BALANCED:
            // 504 total EVs
            evs[0] = 84;
            evs[1] = 84;
            evs[2] = 84;
            evs[3] = 84;
            evs[4] = 84;
            evs[5] = 84;
            break;

        case DEV_EV_PRESET_BULK_PHYSICAL:
            // 252 HP / 252 Atk / 4 Spe
            evs[0] = 252;
            evs[1] = 252;
            evs[3] = 4;
            break;

        case DEV_EV_PRESET_BULK_SPECIAL:
            // 252 HP / 252 SpA / 4 Spe
            evs[0] = 252;
            evs[3] = 4;
            evs[4] = 252;
            break;

        case DEV_EV_PRESET_MIXED_TANK:
            // 252 HP / 128 Def / 128 SpDef
            evs[0] = 252;
            evs[2] = 128;
            evs[5] = 128;
            break;

        case DEV_EV_PRESET_FAST_BULK_SPECIAL:
            // 128 HP / 128 Sp.Def  / 252 Spe
            evs[0] = 128;
            evs[3] = 252; // speed
            evs[5] = 128;
            break;

        case DEV_EV_PRESET_FAST_BULK_PHYS:
            // 128 HP / 128 Def  / 252 Spe
            evs[0] = 128;
            evs[2] = 128;
            evs[3] = 252;
            break;

        case DEV_EV_PRESET_FAST_BULK:
            // 252 HP / 252 Spe
            evs[0] = 252;
            evs[3] = 252;
            break;


        case DEV_EV_PRESET_RESET:
        default:
            // Already all zero.
            break;
        }

        for (u8 i = 0; i < 6; i++) {
            SetMonData(pokemon, MON_DATA_HP_EV + i, &evs[i]);
        }

        RecalcPartyPokemonStats(pokemon);

        return FALSE;
    }

    // Normal GiveEgg behaviour starts here.
    u32 form = (species & 0xF800) >> 11;
    species = species & 0x7FF;

    struct Party *party = SaveData_GetPlayerPartyPtr(fsys->savedata);
    u8 partyCount = party->count;

    if (partyCount < 6) {
        struct PartyPokemon *pokemon = AllocMonZeroed(11);
        ZeroMonData(pokemon);
        int val = sub_02017FE4(1, offset);

        SetEggStats(pokemon, species, 1, profile, 3, val);

        SetMonData(pokemon, MON_DATA_FORM, &form);

        ClearMonMoves(pokemon);
        InitBoxMonMoveset(&pokemon->box);

        if (CheckScriptFlag(HIDDEN_ABILITIES_FLAG) == 1)
        {
            SET_MON_HIDDEN_ABILITY_BIT(pokemon)
            ResetPartyPokemonAbility(pokemon);
            ClearScriptFlag(HIDDEN_ABILITIES_FLAG);
        }

        PokeParty_Add(party, pokemon);
        sys_FreeMemoryEz(pokemon);
    }

    return FALSE;
}


/**
 *  @brief script command to give the togepi egg
 *
 *  @param ctx script context structure
 *  @return FALSE
 */
BOOL ScrCmd_GiveTogepiEgg(SCRIPTCONTEXT *ctx)
{
    s32 i;
    u8 pp;
    u16 moveData;
    struct PartyPokemon *togepi;
    void *profile;
    struct Party *party;
    FieldSystem *fsys = ctx->fsys;

    profile = Sav2_PlayerData_GetProfileAddr(fsys->savedata);
    party = SaveData_GetPlayerPartyPtr(fsys->savedata);

    if (party->count >= 6) {
        return FALSE;
    }

    togepi = AllocMonZeroed(11);
    ZeroMonData(togepi);

    SetEggStats(togepi, SPECIES_TOGEPI, 1, profile, 3, sub_02017FE4(1, 13));

    // SetMonData(togepi, MON_DATA_FORM, &form); // add form capability

    // ClearMonMoves(pokemon);
    // InitBoxMonMoveset(&pokemon->box);

    for (i = 0; i < 4; i++) {
        if (!GetMonData(togepi, MON_DATA_MOVE1 + i, 0)) {
            break;
        }
    }

    if (i == 4) {
        i = 3;
    }

    moveData = MOVE_EXTRASENSORY; // add extrasensory to the togepi
    SetMonData(togepi, MON_DATA_MOVE1 + i, &moveData);

    pp = GetMonData(togepi, MON_DATA_MOVE1MAXPP + i, 0);
    SetMonData(togepi, MON_DATA_MOVE1PP + i, &pp);

    if (CheckScriptFlag(HIDDEN_ABILITIES_FLAG) == 1) // add HA capability
    {
        SET_MON_HIDDEN_ABILITY_BIT(togepi)
        ResetPartyPokemonAbility(togepi);
        ClearScriptFlag(HIDDEN_ABILITIES_FLAG);
    }

    PokeParty_Add(party, togepi);

    sys_FreeMemoryEz(togepi);

    SaveMisc_SetTogepiPersonalityGender(Sav2_Misc_get(fsys->savedata), GetMonData(togepi, MON_DATA_PERSONALITY, 0), GetMonData(togepi, MON_DATA_GENDER, 0));

    return FALSE;
}

BOOL ScrCmd_DaycareSanitizeMon(SCRIPTCONTEXT *ctx)
{
    struct PartyPokemon *partyMon;

    FieldSystem *fieldSystem = ctx->fsys;
    u16 party_slot = ScriptGetVar(ctx);
    u16 *ret_ptr = ScriptGetVarPointer(ctx);
    void *party = SaveData_GetPlayerPartyPtr(fieldSystem->savedata);
    partyMon = Party_GetMonByIndex(party, party_slot);

    *ret_ptr = 0;

    if (party_slot == 0xFF) {
        return FALSE;
    }

    u32 held_item = GetMonData(partyMon, MON_DATA_HELD_ITEM, NULL);
    if (held_item == ITEM_GRISEOUS_ORB) {
        BAG_DATA *bag = Sav2_Bag_get(fieldSystem->savedata);
        if (!Bag_AddItem(bag, ITEM_GRISEOUS_ORB, 1, 11)) {
            *ret_ptr = 0xFF;
            return FALSE;
        }

        u32 no_item = ITEM_NONE;
        SetMonData(partyMon, MON_DATA_HELD_ITEM, &no_item);
    }

    s32 form = GetMonData(partyMon, MON_DATA_FORM, NULL);
    if (form > 0) {
        u32 species = GetMonData(partyMon, MON_DATA_SPECIES, NULL);
        switch (species) {
        case SPECIES_GIRATINA:
            PokeParaGiratinaFormChange(partyMon);
            break;
        case SPECIES_ROTOM:
            Mon_UpdateRotomForm(partyMon, 0, 0);
            break;
        case SPECIES_SHAYMIN:
            Mon_UpdateShayminForm(partyMon, 0);
            break;
        }
    }

    // Get the other mon in the Daycare
    Daycare *daycare = Save_Daycare_Get(SaveBlock2_get());
    struct BoxPokemon *daycareMon;

    daycareMon = Daycare_GetBoxMonI(daycare, 0);

    // Only perform custom logic if there is already a deposited mon
    if (GetBoxMonData(daycareMon, MON_DATA_SPECIES, NULL) != SPECIES_NONE) {
        u32 inheriterMoves[4];
        u32 donorMoves[4];
        u16 temp_egg_moves[MAX_EGG_MOVES];
        u16 baby_egg_moves[MAX_EGG_MOVES];
        u8 potentialOverrideMoveSlot;
        u8 numEggMoves;
        u32 newMove;
        u32 pp;
        // u8 buf[64];

        // Begin custom logic for Mirror Herb
        if (GetMonData(partyMon, MON_DATA_HELD_ITEM, NULL) == ITEM_MIRROR_HERB || GetMonData(partyMon, MON_DATA_SPECIES, NULL) == GetBoxMonData(daycareMon, MON_DATA_SPECIES, NULL)) {
            // sprintf(buf, "Party mon logic.\n");
            // debugsyscall(buf);

            // Check if there is an empty moveslot
            for (potentialOverrideMoveSlot = 0; potentialOverrideMoveSlot < 4; potentialOverrideMoveSlot++) {
                if (GetMonData(partyMon, MON_DATA_MOVE1 + potentialOverrideMoveSlot, NULL) == MOVE_NONE) {
                    break;
                }
            }

            // sprintf(buf, "potentialOverrideMoveSlot: %d.\n", potentialOverrideMoveSlot);
            // debugsyscall(buf);

            for (u8 i = 0; i < 4; i++) {
                inheriterMoves[i] = GetMonData(partyMon, MON_DATA_MOVE1 + i, NULL);
                // sprintf(buf, "inheriterMoves %d: %d.\n", i, inheriterMoves[i]);
                // debugsyscall(buf);
            }

            if (potentialOverrideMoveSlot != 4) {
                numEggMoves = LoadEggMoves(partyMon, temp_egg_moves);

                u32 numAvailableToInheritMoves = 0;
                for (u8 i = 0; i < numEggMoves; i++) {
                    if (temp_egg_moves[i] != inheriterMoves[0] && temp_egg_moves[i] != inheriterMoves[1] && temp_egg_moves[i] != inheriterMoves[2] && temp_egg_moves[i] != inheriterMoves[3]) {
                        baby_egg_moves[numAvailableToInheritMoves] = temp_egg_moves[i];

                        // sprintf(buf, "baby_egg_moves %d: %d.\n", numAvailableToInheritMoves, baby_egg_moves[numAvailableToInheritMoves]);
                        // debugsyscall(buf);

                        numAvailableToInheritMoves++;
                    }
                }

                donorMoves[0] = GetBoxMonData(daycareMon, MON_DATA_MOVE1, NULL);
                donorMoves[1] = GetBoxMonData(daycareMon, MON_DATA_MOVE2, NULL);
                donorMoves[2] = GetBoxMonData(daycareMon, MON_DATA_MOVE3, NULL);
                donorMoves[3] = GetBoxMonData(daycareMon, MON_DATA_MOVE4, NULL);

                for (u8 i = 0; i < 4; i++) {
                    for (u8 j = 0; j < numAvailableToInheritMoves; j++) {
                        if (donorMoves[i] == baby_egg_moves[j]) {
                            newMove = baby_egg_moves[j];
                            SetMonData(partyMon, MON_DATA_MOVE1 + potentialOverrideMoveSlot, &newMove);
                            pp = GetMonData(partyMon, MON_DATA_MOVE1MAXPP + potentialOverrideMoveSlot, NULL);
                            SetMonData(partyMon, MON_DATA_MOVE1PP + potentialOverrideMoveSlot, &pp);
                            potentialOverrideMoveSlot++;
                            if (potentialOverrideMoveSlot >= 4) {
                                break;
                            }
                        }
                    }
                    if (potentialOverrideMoveSlot >= 4) {
                        break;
                    }
                }
            }
        }

        if (GetBoxMonData(daycareMon, MON_DATA_HELD_ITEM, NULL) == ITEM_MIRROR_HERB || GetMonData(partyMon, MON_DATA_SPECIES, NULL) == GetBoxMonData(daycareMon, MON_DATA_SPECIES, NULL)) {
            // sprintf(buf, "Party mon logic.\n");
            // debugsyscall(buf);

            // Check if there is an empty moveslot
            for (potentialOverrideMoveSlot = 0; potentialOverrideMoveSlot < 4; potentialOverrideMoveSlot++) {
                if (GetBoxMonData(daycareMon, MON_DATA_MOVE1 + potentialOverrideMoveSlot, NULL) == MOVE_NONE) {
                    break;
                }
            }

            // sprintf(buf, "potentialOverrideMoveSlot: %d.\n", potentialOverrideMoveSlot);
            // debugsyscall(buf);

            for (u8 i = 0; i < 4; i++) {
                inheriterMoves[i] = GetMonData(partyMon, MON_DATA_MOVE1 + i, NULL);
                // sprintf(buf, "inheriterMoves %d: %d.\n", i, inheriterMoves[i]);
                // debugsyscall(buf);
            }

            if (potentialOverrideMoveSlot != 4) {
                numEggMoves = LoadEggMoves((struct PartyPokemon *)daycareMon, baby_egg_moves);

                u32 numAvailableToInheritMoves = 0;
                for (u8 i = 0; i < numEggMoves; i++) {
                    if (temp_egg_moves[i] != inheriterMoves[0] && temp_egg_moves[i] != inheriterMoves[1] && temp_egg_moves[i] != inheriterMoves[2] && temp_egg_moves[i] != inheriterMoves[3]) {
                        baby_egg_moves[numAvailableToInheritMoves] = temp_egg_moves[i];

                        // sprintf(buf, "baby_egg_moves %d: %d.\n", numAvailableToInheritMoves, baby_egg_moves[numAvailableToInheritMoves]);
                        // debugsyscall(buf);

                        numAvailableToInheritMoves++;
                    }
                }

                donorMoves[0] = GetMonData(partyMon, MON_DATA_MOVE1, NULL);
                donorMoves[1] = GetMonData(partyMon, MON_DATA_MOVE2, NULL);
                donorMoves[2] = GetMonData(partyMon, MON_DATA_MOVE3, NULL);
                donorMoves[3] = GetMonData(partyMon, MON_DATA_MOVE4, NULL);

                for (u8 i = 0; i < 4; i++) {
                    for (u8 j = 0; j < numAvailableToInheritMoves; j++) {
                        if (donorMoves[i] == baby_egg_moves[j]) {
                            newMove = baby_egg_moves[j];
                            SetBoxMonData(daycareMon, MON_DATA_MOVE1 + potentialOverrideMoveSlot, &newMove);
                            pp = GetBoxMonData(daycareMon, MON_DATA_MOVE1MAXPP + potentialOverrideMoveSlot, NULL);
                            SetBoxMonData(daycareMon, MON_DATA_MOVE1PP + potentialOverrideMoveSlot, &pp);
                            potentialOverrideMoveSlot++;
                            if (potentialOverrideMoveSlot >= 4) {
                                break;
                            }
                        }
                    }
                    if (potentialOverrideMoveSlot >= 4) {
                        break;
                    }
                }
            }
        }
    }
    return FALSE;
}

BOOL ScrCmd_WildBattle(SCRIPTCONTEXT *ctx)
{
    u32 *winFlag = FieldSysGetAttrAddr(ctx->fsys, 24); // SCRIPTENV_BATTLE_WIN_FLAG = 24
    u16 species = ScriptGetVar(ctx);
    u16 level = ScriptGetVar(ctx);
    u8 shiny = ScriptReadByte(ctx);
    // Set this var to 1 in DSPRE just prior to starting a forced wild battle to turn it into a Totem battle.
    if (GetScriptVar(0x800B)) {
        SetupAndStartTotemBattle(ctx->taskman, species, level, winFlag, shiny);
    } else {
        SetupAndStartWildBattle(ctx->taskman, species, level, winFlag, TRUE, shiny);
    }
    return TRUE;
}

void SetupAndStartTotemBattle(TaskManager *taskManager, u16 species, u8 level, u32 *winFlag, BOOL shiny)
{
    FieldSystem *fieldSystem = taskManager->fieldSystem;
    struct BattleSetup *setup = BattleSetup_New(HEAPID_WORLD, BATTLE_TYPE_TOTEM);
    BattleSetup_InitFromFieldSystem(setup, fieldSystem);
    ov02_02247F30(fieldSystem, species, level, shiny, setup);

    // Uncomment this line if you want to manually adjust specific elements according to Totem Species.
    // struct PartyPokemon *totem = Party_GetMonByIndex(setup->party[BATTLER_ENEMY], 0);

    switch (species) {
        // You can use the case below as a template:
        /*case SPECIES_GYARADOS:
            // Ability:
            u16 data_1 = ABILITY_MOXIE;
            SetMonData(totem, MON_DATA_ABILITY, &data_1);

            // Item:
            data_1 = ITEM_WACAN_BERRY;
            SetMonData(totem, MON_DATA_HELD_ITEM, &data_1);

            // Move slot 1:
            data_1 = MOVE_AQUA_TAIL;
            SetMonData(totem, MON_DATA_MOVE1, &data_1);
            data_1 = GetMoveMaxPP(data_1, 0);
            SetMonData(totem, MON_DATA_MOVE1PP, &data_1);
            data_1 = 0;
            SetMonData(totem, MON_DATA_MOVE1PPUP, &data_1);

            // Move slot 2:
            data_1 = MOVE_ICE_FANG;
            SetMonData(totem, MON_DATA_MOVE2, &data_1);
            data_1 = GetMoveMaxPP(data_1, 0);
            SetMonData(totem, MON_DATA_MOVE2PP, &data_1);
            data_1 = 0;
            SetMonData(totem, MON_DATA_MOVE2PPUP, &data_1);

            // Move slot 3:
            data_1 = MOVE_CRUNCH;
            SetMonData(totem, MON_DATA_MOVE3, &data_1);
            data_1 = GetMoveMaxPP(data_1, 0);
            SetMonData(totem, MON_DATA_MOVE3PP, &data_1);
            data_1 = 0;
            SetMonData(totem, MON_DATA_MOVE3PPUP, &data_1);

            // Move slot 4:
            data_1 = MOVE_DRAGON_DANCE;
            SetMonData(totem, MON_DATA_MOVE4, &data_1);
            data_1 = GetMoveMaxPP(data_1, 0);
            SetMonData(totem, MON_DATA_MOVE4PP, &data_1);
            data_1 = 0;
            SetMonData(totem, MON_DATA_MOVE4PPUP, &data_1);
            break;

            // IVs:
            data_1 = 20;
            SetMonData(totem, MON_DATA_HP_IV, &data_1);
            SetMonData(totem, MON_DATA_ATK_IV, &data_1);
            SetMonData(totem, MON_DATA_DEF_IV, &data_1);
            SetMonData(totem, MON_DATA_SPEED_IV, &data_1);
            SetMonData(totem, MON_DATA_SPATK_IV, &data_1);
            SetMonData(totem, MON_DATA_SPDEF_IV, &data_1);

            // Nature:
            data_1 = NATURE_ADAMANT;
            u32 pid_1 = GetMonData(totem, MON_DATA_PERSONALITY, NULL);
            u8 currentNature_1 = pid_1 % 25;
            pid_1 = pid_1 + data_1 - currentNature_1;
            SetMonData(totem, MON_DATA_PERSONALITY, &pid_1);
            break;*/

    default:
        break;
    }

    GameStats_Inc(Save_GameStats_Get(fieldSystem->savedata), GAME_STAT_WILD_ENCOUNTERS);

    CallTask_StartEncounter(taskManager, setup, BattleSetup_GetWildTransitionEffect(setup), BattleSetup_GetWildBattleMusic(setup), winFlag);
}
