from game_classes.fighter import Fighter
from game_classes.obstacles import return_obstacles_collection
from util.util_fighters import *


def make_attack_menu(local_game_board, is_black, attack_decision):
    opponent_collection = return_needed_collection(not is_black) \
        if attack_decision == 1 else return_obstacles_collection()

    """
    print("Това са всички ваши налични фигури, моля изберете:")
    print_all_alive_fighters(current_collection)
    my_fighter_index = int(input())
    """
    current_collection = return_needed_collection(is_black)
    my_fighter_index = get_current_fighters_choice(current_collection)

    is_barricade_attacked = attack_decision_message(attack_decision, opponent_collection)
    opp_fighter_index = int(input())

    my_fighter = current_collection[my_fighter_index - 1]
    opp_fighter = opponent_collection[opp_fighter_index - 1]

    attack_fighter(local_game_board, my_fighter, opp_fighter, is_barricade_attacked)

    if isinstance(opp_fighter, Fighter):
        if is_fighter_dead(opp_fighter.health):
            remove_fighter_game_board(local_game_board, opp_fighter)


def attack_decision_message(attack_decision, opponent_collection):
    if attack_decision == 1:
        print("Това са всички противникови фигури, изберете коя да атакувате:")
        print_all_alive_fighters(opponent_collection)
        return False
    if attack_decision == 2:
        print("Това са всички барикади, изберете коя да атакувате:")
        print_barricade_collection(opponent_collection)
        return True

    return False


def attack_fighter(local_game_board, my_fighter, opp_fighter, is_barricade_attacked):
    if my_fighter.is_attack_possible(opp_fighter) and not is_barricade_attacked:
        my_fighter.make_attack(opp_fighter)
        print("Оставащо здраве: ", opp_fighter.health)
        return
    if my_fighter.is_attack_possible(opp_fighter) and is_barricade_attacked:
        local_game_board[opp_fighter.row][opp_fighter.col] = None
        opp_fighter.is_obstacle_broken = True
        return

    print("Атаката не е възможна!")
    return


def is_fighter_dead(health):
    return health <= 0


def remove_fighter_game_board(local_game_board, opp_fighter):
    local_game_board[opp_fighter.row][opp_fighter.col] = None
    opp_fighter.is_fighter_alive = False
