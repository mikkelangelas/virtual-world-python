from .Plant import Plant


class Guarana(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 0

    def collision(self, other):
        other.str += 3
        super().collision(other)

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Guarana(x, y, self.world)
        else:
            return None

    def __str__(self):
        return "Guarana"

