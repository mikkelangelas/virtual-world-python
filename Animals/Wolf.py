from .Animal import Animal


class Wolf(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 9
        self.init = 5
        self.label = 'w'
        self.color = "#777f77"

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Wolf(x, y, self.world)
        else:
            return None

    def __str__(self):
        return "Wolf"