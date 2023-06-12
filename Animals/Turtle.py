from .Animal import Animal
import random


class Turtle(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 2
        self.init = 1
        self.label = 't'
        self.color = "#325a34"

    def action(self):
        r = random.randint(1, 4)
        if r == 1:
            super().action()

    def collision(self, other):
        if other.str < 5 and type(self) != type(other):
            other.return_to_last()
            self.world.send_alert(self.__str__() + " deflected an attack from " + other.__str__())
        else:
            super().collision(other)

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Turtle(x, y, self.world)
        else:
            return None

    def __str__(self):
        return "Turtle"
