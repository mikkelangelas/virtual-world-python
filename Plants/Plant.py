from abc import ABC
from Organism import Organism
import random


class Plant(Organism, ABC):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = None
        self.init = 0
        self.world = world

    def action(self):
        r = random.randint(1, 100)
        if r == 1:
            self.world.organisms.append(self.reproduce())

    def collision(self, other):
        self.die()
