from .Animal import Animal


class Sheep(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 4
        self.init = 4

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Sheep(x, y, self.world)
        else:
            return None

    def __str__(self):
        return "Sheep"
