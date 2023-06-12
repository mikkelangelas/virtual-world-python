from .Plant import Plant
from Animals.Cybersheep import Cybersheep


class Heracleum(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 10
        self.label = 'h'
        self.color = "#C9d9b1"
        self.is_targeted = False

    def collision(self, other):
        if isinstance(other, Cybersheep):
            self.die()
            other.target = None
            self.world.send_alert(self.__str__() + " was eaten by " + other.__str__())
        else:
            other.die()
            self.world.send_alert(other.__str__() + " was posioned by " + self.__str__())

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Heracleum(x, y, self.world)
        else:
            return None

    def __str__(self):
        return "Heracleum"

