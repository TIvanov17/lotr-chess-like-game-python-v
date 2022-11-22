from util.util_fighters import *


def move_fighters_menu(local_game_board, is_black):
    """
    current_collection = return_needed_collection(is_black_to_move)
    print("Това са всички ваши налични фигури, моля изберете:")
    print_all_alive_fighters(current_collection)
    choose_fighter_to_move = int(input())
    """
    current_collection = return_needed_collection(is_black)
    choose_fighter_to_move = get_current_fighters_choice(current_collection)

    print("На кой ред?")
    new_row = int(input())
    print("На коя колона?")
    new_col = int(input())

    move(local_game_board, current_collection, choose_fighter_to_move - 1, new_row, new_col)


def move(local_game_board, current_collection, fighter_number, new_row, new_col):
    try:
        selected_fighter = current_collection[fighter_number]
    except IndexError:
        print("This fighter index do not exist!")
        return

    prev_row = selected_fighter.row
    prev_col = selected_fighter.col

    should_move_fighter = selected_fighter.is_move_possible(local_game_board, new_row, new_col) and \
                          selected_fighter.is_road_obstacle_free(local_game_board, new_row, new_col)

    if should_move_fighter:
        selected_fighter.move(new_row, new_col)
        update_game_board(local_game_board, selected_fighter, new_row, new_col, prev_row, prev_col)
    else:
        print("Придвижване не е възможно!")


def update_game_board(local_game_board, selected_fighter, new_row, new_col, prev_row, prev_col):
    local_game_board[prev_row][prev_col] = None
    local_game_board[new_row][new_col] = selected_fighter
