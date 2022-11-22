import enum
from abc import ABC, abstractmethod

from game_classes.obstacles import Obstacle
import random


class Color(enum.Enum):
    BLACK = "B"
    RED = "R"


def is_new_position_available(game_board, new_row, new_col):
    element = game_board[new_row][new_col]
    return element is None


def is_road_with_obstacles(game_board, start_row, end_row, start_col, end_col):
    for row_i in range(start_row, end_row):
        for col_i in range(start_col, end_col):
            if isinstance(game_board[row_i][col_i], Obstacle):
                return True

    return False


class Fighter(ABC):

    def __init__(self, color, row, col, health):
        self.color = color
        self.row = row
        self.col = col
        self.is_fighter_alive = True
        self.health = health

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, row):

        is_black_row_wrong = (self.color == 'B' and (row < 5 or row > 6))
        is_red_row_correct = (self.color == 'R' and (row < 0 or row > 1))

        if is_black_row_wrong or is_red_row_correct:
            self.__row = -1
        else:
            self.__row = row

    @property
    def col(self):
        return self.__col

    @col.setter
    def col(self, col):
        is_col_wrong = (col < 0 or col > 8)
        if is_col_wrong:
            self.__col = -1
        else:
            self.__col = col

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def is_fighter_alive(self):
        return self.__is_fighter_alive

    @is_fighter_alive.setter
    def is_fighter_alive(self, is_fighter_alive):
        self.__is_fighter_alive = is_fighter_alive

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    def print_symbol(self):
        print('{:>4}'.format((self.color + self.get_symbol())), end=" ")

    @abstractmethod  # MUST implement
    def get_symbol(self):
        pass

    def is_move_possible(self, game_board, new_row, new_col):
        is_equal_row_or_col = self.row == new_row or self.col == new_col

        is_distance_true = abs(self.row - new_row) <= self.get_speed() and \
                           abs(self.col - new_col) <= self.get_speed()

        return is_equal_row_or_col and is_distance_true

    def is_road_obstacle_free(self, game_board, new_row, new_col):
        is_new_position_available_var = is_new_position_available(game_board, new_row, new_col)
        is_road_clear = not self.is_there_obstacles_on_road(game_board, new_row, new_col)
        return is_new_position_available_var and is_road_clear

    def is_there_obstacles_on_road(self, game_board, new_row, new_col):
        if self.row == new_row and new_col > self.col:
            return is_road_with_obstacles(game_board, self.row, self.row + 1, self.col, new_col)
        if self.row == new_row and new_col < self.col:
            return is_road_with_obstacles(game_board, self.row, self.row + 1, new_col, self.col)
        if self.col == new_col and new_row > self.row:
            return is_road_with_obstacles(game_board, self.row, new_row, self.col, self.col + 1)
        if self.col == new_col and new_row < self.row:
            return is_road_with_obstacles(game_board, new_row, self.row, self.col, self.col + 1)

        return False

    @abstractmethod  # MUST implement
    def get_speed(self):
        pass

    def move(self, new_row, new_col):
        self.__row = new_row
        self.__col = new_col

    def is_attack_possible(self, opp_fighter):
        is_equal_row_or_col = self.row == opp_fighter.row or self.col == opp_fighter.col
        is_distance_true = False

        if is_equal_row_or_col:
            row_distance = 0 if self.row == opp_fighter.row else self.get_distance()
            col_distance = self.get_distance() if self.row == opp_fighter.row else 0

            is_distance_true = abs(self.row - opp_fighter.row) == row_distance and \
                               abs(self.col - opp_fighter.col) == col_distance

        return is_equal_row_or_col and is_distance_true

    @abstractmethod
    def get_distance(self):
        pass

    def make_attack(self, opp_fighter):
        dice_sum = random.randint(3, 15)
        damage = self.get_attack() - opp_fighter.armor
        if dice_sum == opp_fighter.health:
            print("Dice sum", dice_sum, "= health", opp_fighter.health)
            print("Атаката е неуспешна!")
            return
        if dice_sum == 3:
            print("Извършена бе полу-атака!")
            damage /= 2

        opp_fighter.health -= damage

    @abstractmethod  # MUST implement
    def get_attack(self):
        pass

    def append_fighter_statement(self, is_black):
        if is_black:
            _black_fighters_collection.append(self.get_object())
        else:
            _red_fighters_collection.append(self.get_object())

    @abstractmethod
    def get_object(self):
        pass

    def heal_fighter(self):
        dice = random.randint(1, 6)
        self.health += dice
        if self.health > self.get_health_border():
            self.health = self.get_health_border()
        print("Излекувани сте с:", dice, ", здраве:", self.health)

    @abstractmethod
    def get_health_border(self):
        pass


_black_fighters_collection = []
_red_fighters_collection = []


def return_black_fighters_collection():
    return _black_fighters_collection


def return_red_fighters_collection():
    return _red_fighters_collection
