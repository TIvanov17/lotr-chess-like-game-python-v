
class NotRightToAttackValue(Exception):
    pass


def is_attack_decision_correct(f_argument, s_argument):
    try:
        fighter_or_barricade = choose_to_attack_fighter_or_barricade()
        if not _is_value_right(fighter_or_barricade, f_argument, s_argument):
            raise NotRightToAttackValue
        else:
            return fighter_or_barricade
    except NotRightToAttackValue:
        message()
        return -1


def choose_to_attack_fighter_or_barricade():
    print("Изберете какво да атакувате:")
    print("1. Фигура")
    print("2. Барикада")
    fighter_or_barricade = int(input())
    return fighter_or_barricade


def _is_value_right(value, f_argument, s_argument):
    return value != f_argument or value != s_argument


def message():
    print("Wrong input!")


