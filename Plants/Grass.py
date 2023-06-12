from .Plant import Plant


class Grass(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 0
        self.label = ','
        self.color = "#49cb17"

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Grass(x, y, self.world)
        else:
            return None

    def __str__(self):
        return "Grass"
