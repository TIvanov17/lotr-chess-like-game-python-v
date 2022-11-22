from util.util_fighters import return_needed_collection, get_current_fighters_choice


def heal_fighter(is_black):
    current_collection = return_needed_collection(is_black)
    current_fighter_index_coll = get_current_fighters_choice(current_collection)

    current_fighter = current_collection[current_fighter_index_coll-1]
    current_fighter.heal_fighter()
