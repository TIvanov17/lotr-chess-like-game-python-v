from abc import ABC, abstractmethod


class Obstacle(ABC):

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_obstacle_broken = False

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, row):
        self.__row = row

    @property
    def col(self):
        return self.__col

    @col.setter
    def col(self, col):
        self.__col = col

    @property
    def is_obstacle_broken(self):
        return self.__is_obstacle_broken

    @is_obstacle_broken.setter
    def is_obstacle_broken(self, is_obstacle_broken):
        self.__is_obstacle_broken = is_obstacle_broken

    def print_symbol(self):
        print('{:>4}'.format(self.get_symbol()), end=" ")

    @abstractmethod
    def get_symbol(self):
        pass


class Wall(Obstacle):

    def __init__(self, row, col):
        super().__init__(row, col)
        self.symbol = "#"

    def get_symbol(self):
        return self.symbol


class Barricade(Obstacle):

    def __init__(self, row, col):
        super().__init__(row, col)
        self.symbol = "$"

    def get_symbol(self):
        return self.symbol

    def append_barricade(self):
        _obstacles_collection.append(Barricade(self.row, self.col))


_obstacles_collection = []


def return_obstacles_collection():
    return _obstacles_collection
