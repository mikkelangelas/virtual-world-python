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
            new_o = self.reproduce()
            if new_o is not None and self.age != 0:
                self.world.organisms.append(new_o)
                self.world.increase_occupied()
                self.world.send_alert("New " + self.__str__() + " grew")

    def collision(self, other):
        self.die()
        self.world.send_alert(self.__str__() + " was eaten by " + other.__str__())
