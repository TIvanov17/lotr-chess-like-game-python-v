from util.exceptions import message
from util.util_fighters import *


def place_fighters_menu(game_board, is_black):
    start_color_message = "Черните са на ход." if is_black else "Червените са на ход."
    print()
    print(start_color_message)
    make_choice = place_fighters_choices()

    if not is_choice_valid(make_choice):
        message()
        return

    print("На кой ред?")
    row = int(input())
    print("На коя колона?")
    col = int(input())

    return set_fighter_on_position(game_board, make_choice, row, col, is_black)


def place_fighters_choices():
    print("Разполагате със следните фигури:")
    print("1. Рицар")
    print("2. Джудже")
    print("3. Елф")
    make_choice = int(input())
    return make_choice


def is_choice_valid(choice):
    return choice == 1 or choice == 2 or choice == 3


def set_fighter_on_position(game_board, choice, row, col, is_black):
    color_type = Color.BLACK.value if is_black else Color.RED.value

    if choice == 1:
        knight = Knight(color_type, row, col)
        if is_row_or_col_wrong(knight):
            return message()

        knight.append_fighter_statement(is_black)
        game_board[row][col] = knight
        return game_board

    if choice == 2:
        dwarf = Dwarf(color_type, row, col)
        if is_row_or_col_wrong(dwarf):
            return message()

        game_board[row][col] = dwarf
        dwarf.append_fighter_statement(is_black)
        return game_board

    if choice == 3:
        elf = Elf(color_type, row, col)
        if is_row_or_col_wrong(elf):
            return message()

        game_board[row][col] = elf
        elf.append_fighter_statement(is_black)
        return game_board


def is_row_or_col_wrong(fighter):
    return fighter.row == -1 or fighter.col == -1

