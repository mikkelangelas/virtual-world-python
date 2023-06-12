from .Animal import Animal


class Cybersheep(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 11
        self.init = 4
        self.label = 'c'
        self.color = "#57d7be"
        self.target = None

    def action(self):
        self.free_field()
        if self.target is None:
            self.set_target()

        if self.target is None:
            super().action()
        else:
            if self.target.x < self.x:
                self.x -= 1
            elif self.target.x > self.x:
                self.x += 1
            elif self.target.y < self.y:
                self.y -= 1
            elif self.target.y > self.y:
                self.y += 1

        self.check_collision()

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Cybersheep(x, y, self.world)
        else:
            return None

    def set_target(self):
        h = self.world.get_heracleum(self)

        if h is not None:
            self.target = h
            h.is_targeted = True

    def __str__(self):
        return "Cybersheep"
