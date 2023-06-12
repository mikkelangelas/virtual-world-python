from .Plant import Plant


class Dandelion(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 0
        self.label = 'd'
        self.color = "#Eccc29"

    def action(self):
        for i in range(3):
            super().action()

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Dandelion(x, y, self.world)
        else:
            return None

    def __str__(self):
        return "Dandelion"
