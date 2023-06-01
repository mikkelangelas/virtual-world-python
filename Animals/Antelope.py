from .Animal import Animal
import random


class Antelope(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 4
        self.init = 4

    def action(self):
        self.last_x = self.x
        self.last_y = self.y
        r = random.randint(0, 3)
        if r == 0 and self.x < self.world.width - 2:
            self.x += 2
        elif r == 1 and self.x > 1:
            self.x -= 2
        elif r == 2 and self.y < self.world.height - 2:
            self.y += 2
        elif r == 3 and self.y > 1:
            self.y -= 2

    def collision(self, other):
        r = random.randint(0, 1)
        if r == 1 and type(self) != type(other):
            self.action()

        else:
            super().collision(other)

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Antelope(x, y, self.world)
        else:
            return None

    def __str__(self):
        return "Antelope"
