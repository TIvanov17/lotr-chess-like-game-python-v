from tech_for_fighters import move, attack
from tech_for_fighters.heal import heal_fighter
from tech_for_fighters.place_fighters import *
from util.exceptions import is_attack_decision_correct, message
from util.game_board_render import *
from util.util_fighters import *

isFightersPlaced = False
isGameEnd = False


def main():
    print("НАЧАЛО НА ИГРАТА")
    place_fighters()
    place_obstacles(return_game_board())
    real_game_action()


def place_fighters():
    while not isFightersPlaced:

        if count_fighters(return_black_fighters_collection()) and count_fighters(return_red_fighters_collection()):
            render_empty_game_board_objects(False)
            print("Всички фигури са поставени, време е за същинската част!")
            print()
            break

        render_empty_game_board_objects(True)
        place_fighters_menu(return_game_board(), True)

        render_empty_game_board_objects(False)
        place_fighters_menu(return_game_board(), False)


def real_game_action():
    render_empty_game_board_objects(False)
    while not isGameEnd:
        action_number = color_real_game_action(True)
        if is_there_second_action(action_number):
            print("Имате право на 2-ро действие!")
            color_real_game_action(True)

        action_number = color_real_game_action(False)
        if is_there_second_action(action_number):
            print("Имате право на 2-ро действие!")
            color_real_game_action(False)


def color_real_game_action(is_black):
    output_message = "Черните са на ход." if is_black else "Червените са на ход."
    print(output_message)
    action_number = choose_action(is_black)
    render_empty_game_board_objects(is_black)
    return action_number


def choose_action(is_black):
    print("1. Придвижване на фигура")
    print("2. Атакуване на противникова фигура")
    print("3. Излекуване на фигура")

    action_number = int(input())
    if action_number == 1:
        move.move_fighters_menu(return_game_board(), is_black)
        return -1
    if action_number == 2:
        attack_decision = is_attack_decision_correct(1, 2)
        if attack_decision == -1:
            return -1
        attack.make_attack_menu(return_game_board(), is_black, attack_decision)
        return -1
    if action_number == 3:
        heal_fighter(is_black)
        return action_number
    else:
        message()


def is_there_second_action(action_number):
    rand_num = random_generator(1, 6)
    return rand_num % 2 != 0 and action_number == 3


if __name__ == "__main__":
    main()
