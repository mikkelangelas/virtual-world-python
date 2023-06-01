from .Plant import Plant
from Animals.Cybersheep import Cybersheep


class Heracleum(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 10

    def collision(self, other):
        if isinstance(other, Cybersheep):
            super().collision(other)
        else:
            other.die()

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Heracleum(x, y, self.world)
        else:
            return None

    def __str__(self):
        return "Heracleum"

