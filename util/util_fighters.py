from game_classes.child_fighters import *
from game_classes.fighter import *
import random


def count_fighters(placed_color_collection):
    count_knights = 0
    count_dwarves = 0
    count_elves = 0

    for current_fighter in placed_color_collection:
        if isinstance(current_fighter, Knight):
            count_knights = count_knights + 1
        if isinstance(current_fighter, Dwarf):
            count_dwarves = count_dwarves + 1
        if isinstance(current_fighter, Elf):
            count_elves = count_elves + 1

    return is_all_fighters_placed(count_knights, count_dwarves, count_elves)


def print_barricade_collection(barricade_collection):
    for current_barricade in barricade_collection:
        if not current_barricade.is_obstacle_broken:
            current_index = barricade_collection.index(current_barricade) + 1
            print(current_index, "Барикада (", current_barricade.row, ",", current_barricade.col, ");  ", end="")
    print()


def get_current_fighters_choice(current_collection):
    print("Това са всички ваши налични фигури, моля изберете:")
    print_all_alive_fighters(current_collection)
    choose_fighter = int(input())
    return choose_fighter


def print_all_alive_fighters(current_color_collection):

    for current_fighter in current_color_collection:
        current_index = current_color_collection.index(current_fighter) + 1

        if isinstance(current_fighter, Knight) and current_fighter.is_fighter_alive:
            print()
            print(current_index, "Рицар (", current_fighter.row, ",", current_fighter.col, ")", end="")

        if isinstance(current_fighter, Dwarf) and current_fighter.is_fighter_alive:
            print()
            print(current_index, "Джудже (", current_fighter.row, ",", current_fighter.col, ")", end="")

        if isinstance(current_fighter, Elf) and current_fighter.is_fighter_alive:
            print()
            print(current_index, "Елф (", current_fighter.row, ",", current_fighter.col, ")", end="")

    print()


def return_needed_collection(is_black_to_move):
    if is_black_to_move:
        return return_black_fighters_collection()
    if not is_black_to_move:
        return return_red_fighters_collection()


def is_all_fighters_placed(knights, dwarves, elves):
    return knights == 0 and dwarves == 1 and elves == 0


def random_generator(min_num, max_num):
    return random.randint(min_num, max_num)
