from abc import ABC, abstractmethod
from Organism import Organism
import random


class Animal(Organism, ABC):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = None
        self.init = None

    def action(self):
        self.free_field()
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

        self.check_collision()

    def collision(self, other):
        if type(self) == type(other):
            other.return_to_last()
            new_o = self.reproduce()
            if new_o is not None:
                self.world.organisms.append(new_o)
                self.world.increase_occupied()
                self.world.send_alert("New " + self.__str__() + " was born")
        else:
            if self.str > other.str:
                other.die()
                self.world.send_alert(other.__str__() + " was killed by " + self.__str__())
            elif other.str > self.str:
                self.die()
                self.world.send_alert(self.__str__() + " was killed by " + other.__str__())

    def free_field(self):
        self.world.window.grid.get_grid(self.x, self.y).free_occupation()
