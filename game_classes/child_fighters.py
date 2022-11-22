from abc import ABC

from game_classes.fighter import Fighter


class Knight(Fighter, ABC):
    attack = 8
    armor = 3
    distance = 1
    speed = 1
    symbol = "%"
    health_border = 15

    def __init__(self, row, col, color):
        # TO inheritance
        # super(Knight, self).__init__(row, col)
        # Fighter.__init__(self, row, col)

        super().__init__(row, col, color, 15)
        # self.health = 15

    def get_symbol(self):
        return self.symbol

    def get_speed(self):
        return self.speed

    def is_attack_possible(self, opp_fighter):
        is_equal_row_or_col = self.row == opp_fighter.row or self.col == opp_fighter.col
        is_distance_true = abs(self.row - opp_fighter.row) <= self.distance and \
                           abs(self.col - opp_fighter.col) <= self.distance

        return is_equal_row_or_col and is_distance_true

    def get_attack(self):
        return self.attack

    def get_distance(self):
        return self.distance

    def get_object(self):
        return Knight(self.color, self.row, self.col)

    def get_health_border(self):
        return self.health_border


class Elf(Fighter, ABC):
    attack = 5
    armor = 1
    distance = 3
    speed = 3
    symbol = "&"
    health_border = 10

    def __init__(self, row, col, color):
        super().__init__(row, col, color, 10)
        # self.health = 10

    def get_symbol(self):
        return self.symbol

    def is_move_possible(self, game_board, new_row, new_col):
        is_row_horse_movement = abs(self.row - new_row) <= 2 and abs(self.col - new_col) <= 1
        is_col_horse_movement = abs(self.row - new_row) <= 1 and abs(self.col - new_col) <= 2

        return (super().is_move_possible(game_board, new_row, new_col)) or \
               is_row_horse_movement or is_col_horse_movement

    def get_speed(self):
        return self.speed

    def get_attack(self):
        return self.attack

    def get_distance(self):
        return self.distance

    def get_object(self):
        return Elf(self.color, self.row, self.col)

    def get_health_border(self):
        return self.health_border

class Dwarf(Fighter, ABC):
    attack = 6
    armor = 2
    distance = 2
    speed = 2
    symbol = "@"
    health_border = 12

    def __init__(self, row, col, color):
        super().__init__(row, col, color, 12)
        # self.health = 12

    def get_symbol(self):
        return self.symbol

    def get_speed(self):
        return self.speed

    def get_attack(self):
        return self.attack

    def get_distance(self):
        return self.distance

    def get_object(self):
        return Dwarf(self.color, self.row, self.col)

    def get_health_border(self):
        return self.health_border