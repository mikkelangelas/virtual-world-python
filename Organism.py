from abc import ABC, abstractmethod


class Organism(ABC):
    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        self.last_x = x
        self.last_y = y
        self.age = 0
        self.world = world
        self.dead = False

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, other):
        pass

    @abstractmethod
    def reproduce(self):
        pass

    def return_to_last(self):
        self.x = self.last_x
        self.y = self.last_y

    def die(self):
        self.dead = True
