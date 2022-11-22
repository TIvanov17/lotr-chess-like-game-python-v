from game_classes.fighter import Fighter
from game_classes.obstacles import Wall, Obstacle, Barricade
from util.util_fighters import count_fighters, return_needed_collection, random_generator

GAME_BOARD_ROW = 7
GAME_BOARD_COL = 9
PASSABLE_SYMBOL = '{:>4}'.format(".")
TEMPORARILY_SYMBOL = '{:>4}'.format("X")


game_board = [[None for row in range(GAME_BOARD_COL)] for col in range(GAME_BOARD_ROW)]


def place_obstacles(local_game_board):
    number_of_obstacles = random_generator(1, 5)

    print("NUMBER OF OBSTACLES: ", number_of_obstacles)

    while number_of_obstacles != 0:
        rand_row = random_generator(2, 4)
        rand_col = random_generator(0, 8)
        if not is_game_board_element_none(local_game_board, rand_row, rand_col):
            continue
        else:
            local_game_board[rand_row][rand_col] = \
                place_wall_or_barricade(number_of_obstacles, rand_row, rand_col)

        number_of_obstacles -= 1


def is_game_board_element_none(local_game_board, row, col):
    return local_game_board[row][col] is None


def place_wall_or_barricade(num_of_obstacles, row, col):
    rand_num = random_generator(0, 1)
    if rand_num == 0 or num_of_obstacles == 1:
        wall = Wall(row, col)
        return wall

    barricade = Barricade(row, col)
    barricade.append_barricade()
    return barricade


def return_game_board():
    return game_board


def render_empty_game_board_objects(is_black_turn):
    current_collection = return_needed_collection(is_black_turn)

    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            current_game_object = game_board[row][col]

            if _is_in_temporarily_range(current_game_object, row, is_black_turn) and \
                    not count_fighters(current_collection):
                print(TEMPORARILY_SYMBOL, end=" ")
                continue
            if current_game_object is None:
                print(PASSABLE_SYMBOL, end=" ")
                continue
            if isinstance(current_game_object, Fighter):
                current_game_object.print_symbol()
                continue
            if isinstance(current_game_object, Obstacle):
                current_game_object.print_symbol()
                continue

        print()

    print()


def _is_in_temporarily_range(current_game_object, row, is_black_turn):
    return (row in range(2) and not is_black_turn and current_game_object is None) or \
           (row in range(5, 7, 1) and is_black_turn and current_game_object is None)
