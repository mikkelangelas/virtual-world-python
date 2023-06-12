from .Plant import Plant


class Nightshade(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 99
        self.label = 'n'
        self.color = "#1f3a6e"

    def collision(self, other):
        other.die()
        super().collision(other)

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Nightshade(x, y, self.world)
        else:
            return None

    def __str__(self):
        return "Nightshade"

