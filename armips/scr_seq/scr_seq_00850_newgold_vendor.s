.nds
.thumb

.include "armips/include/scriptmacros.s"
.include "armips/include/vars.s"

// New Gold debug vendor for Cherrygrove City (script file 850).
// We reuse the harmless woman who originally runs script 8, so the whole
// feature remains source-controlled and does not require DSPRE event edits.
// Script file 850 is only ~0x900 bytes in vanilla HGSS; 0x2000 is reserved
// here as fixed patch space so repeated builds are idempotent.

ITEM_RARE_CANDY equ 50
VENDOR_SCRIPT_INDEX equ 8
VENDOR_CODE_OFFSET equ 0x2000

.open "build/a012/2_850", 0

// Script-definition entries are 4-byte relative pointers. Script 8 begins
// at table entry 8, i.e. byte offset 0x20.
.org VENDOR_SCRIPT_INDEX * 4
.word NewGold_CherrygroveVendor - . - 4

.org VENDOR_CODE_OFFSET
NewGold_CherrygroveVendor:
    lockall
    faceplayer
    npc_msg 25 // Password?

    // First digit: 0 / 1 / 2 / 3. Correct = 0.
    scrcmd_065 1, 1, 0, 1, VAR_SPECIAL_RESULT
    scrcmd_066 26, 0
    scrcmd_066 27, 1
    scrcmd_066 28, 2
    scrcmd_066 29, 3
    scrcmd_067
    compare_var_to_value VAR_SPECIAL_RESULT, 0
    goto_if 5, NewGold_VendorWrongPassword

    // Second digit: 2 / 4 / 6 / 8. Correct = 2 (slot 0).
    scrcmd_065 1, 1, 0, 1, VAR_SPECIAL_RESULT
    scrcmd_066 28, 0
    scrcmd_066 30, 1
    scrcmd_066 32, 2
    scrcmd_066 34, 3
    scrcmd_067
    compare_var_to_value VAR_SPECIAL_RESULT, 0
    goto_if 5, NewGold_VendorWrongPassword

    // Third digit: 1 / 3 / 5 / 7. Correct = 5 (slot 2).
    scrcmd_065 1, 1, 0, 1, VAR_SPECIAL_RESULT
    scrcmd_066 27, 0
    scrcmd_066 29, 1
    scrcmd_066 31, 2
    scrcmd_066 33, 3
    scrcmd_067
    compare_var_to_value VAR_SPECIAL_RESULT, 2
    goto_if 5, NewGold_VendorWrongPassword

    // Fourth digit: 0 / 1 / 8 / 9. Correct = 1 (slot 1).
    scrcmd_065 1, 1, 0, 1, VAR_SPECIAL_RESULT
    scrcmd_066 26, 0
    scrcmd_066 27, 1
    scrcmd_066 34, 2
    scrcmd_066 35, 3
    scrcmd_067
    compare_var_to_value VAR_SPECIAL_RESULT, 1
    goto_if 5, NewGold_VendorWrongPassword

    npc_msg 36 // Access granted.
    wait_button
    goto NewGold_VendorMenu

NewGold_VendorMenu:
    npc_msg 46 // Developer Shop / Rare Candy: $1 each.
    scrcmd_065 1, 1, 0, 1, VAR_SPECIAL_RESULT
    scrcmd_066 38, 0 // x1
    scrcmd_066 39, 1 // x10
    scrcmd_066 40, 2 // x50
    scrcmd_066 41, 3 // x99
    scrcmd_066 42, 4 // Exit
    scrcmd_067

    compare_var_to_value VAR_SPECIAL_RESULT, 0
    goto_if 1, NewGold_VendorBuy1
    compare_var_to_value VAR_SPECIAL_RESULT, 1
    goto_if 1, NewGold_VendorBuy10
    compare_var_to_value VAR_SPECIAL_RESULT, 2
    goto_if 1, NewGold_VendorBuy50
    compare_var_to_value VAR_SPECIAL_RESULT, 3
    goto_if 1, NewGold_VendorBuy99
    goto NewGold_VendorExit

NewGold_VendorBuy1:
    hasspaceforitem ITEM_RARE_CANDY, 1, VAR_SPECIAL_RESULT
    compare_var_to_value VAR_SPECIAL_RESULT, 1
    goto_if 5, NewGold_VendorNoSpace
    hasenoughmoneyimmediate VAR_SPECIAL_RESULT, 1
    compare_var_to_value VAR_SPECIAL_RESULT, 1
    goto_if 5, NewGold_VendorNoMoney
    submoneyimmediate 1
    giveitem ITEM_RARE_CANDY, 1, VAR_SPECIAL_RESULT
    npc_msg 43
    wait_button
    goto NewGold_VendorMenu

NewGold_VendorBuy10:
    hasspaceforitem ITEM_RARE_CANDY, 10, VAR_SPECIAL_RESULT
    compare_var_to_value VAR_SPECIAL_RESULT, 1
    goto_if 5, NewGold_VendorNoSpace
    hasenoughmoneyimmediate VAR_SPECIAL_RESULT, 10
    compare_var_to_value VAR_SPECIAL_RESULT, 1
    goto_if 5, NewGold_VendorNoMoney
    submoneyimmediate 10
    giveitem ITEM_RARE_CANDY, 10, VAR_SPECIAL_RESULT
    npc_msg 43
    wait_button
    goto NewGold_VendorMenu

NewGold_VendorBuy50:
    hasspaceforitem ITEM_RARE_CANDY, 50, VAR_SPECIAL_RESULT
    compare_var_to_value VAR_SPECIAL_RESULT, 1
    goto_if 5, NewGold_VendorNoSpace
    hasenoughmoneyimmediate VAR_SPECIAL_RESULT, 50
    compare_var_to_value VAR_SPECIAL_RESULT, 1
    goto_if 5, NewGold_VendorNoMoney
    submoneyimmediate 50
    giveitem ITEM_RARE_CANDY, 50, VAR_SPECIAL_RESULT
    npc_msg 43
    wait_button
    goto NewGold_VendorMenu

NewGold_VendorBuy99:
    hasspaceforitem ITEM_RARE_CANDY, 99, VAR_SPECIAL_RESULT
    compare_var_to_value VAR_SPECIAL_RESULT, 1
    goto_if 5, NewGold_VendorNoSpace
    hasenoughmoneyimmediate VAR_SPECIAL_RESULT, 99
    compare_var_to_value VAR_SPECIAL_RESULT, 1
    goto_if 5, NewGold_VendorNoMoney
    submoneyimmediate 99
    giveitem ITEM_RARE_CANDY, 99, VAR_SPECIAL_RESULT
    npc_msg 43
    wait_button
    goto NewGold_VendorMenu

NewGold_VendorNoMoney:
    npc_msg 44
    wait_button
    goto NewGold_VendorMenu

NewGold_VendorNoSpace:
    npc_msg 45
    wait_button
    goto NewGold_VendorMenu

NewGold_VendorWrongPassword:
    npc_msg 37
    wait_button
    goto NewGold_VendorExit

NewGold_VendorExit:
    closemsg
    releaseall
    end

.close
