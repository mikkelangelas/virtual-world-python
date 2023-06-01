from abc import ABC, abstractmethod
from Organism import Organism
import random


class Animal(Organism, ABC):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = None
        self.init = None

    def action(self):
        self.last_x = self.x
        self.last_y = self.y
        r = random.randint(0, 3)
        if r == 0 and self.x < self.world.width - 1:
            self.x += 1
        elif r == 1 and self.x > 0:
            self.x -= 1
        elif r == 2 and self.y < self.world.height - 1:
            self.y += 1
        elif r == 3 and self.y > 0:
            self.y -= 1

    def collision(self, other):
        if type(self) == type(other):
            self.reproduce()
        else:
            if self.str > other.str:
                other.die()
            elif other.str > self.str:
                self.die()