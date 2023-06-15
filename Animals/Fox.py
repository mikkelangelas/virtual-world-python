from .Animal import Animal
import random


class Fox(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 3
        self.init = 7
        self.label = 'f'
        self.color = "#Cb7523"

    def action(self):
        self.free_field()
        r = random.randint(0, 3)

        if r == 0 and self.x < self.world.width - 1:
            if self.world.is_free(self.x + 1, self.y) or self.world.get_organism_by_pos(self.x + 1, self.y).str < self.str:
                self.confirm_move(self.x + 1, self.y)
        elif r == 1 and self.x > 0:
            if self.world.is_free(self.x - 1, self.y) or self.world.get_organism_by_pos(self.x - 1, self.y).str < self.str:
                self.confirm_move(self.x - 1, self.y)
        elif r == 2 and self.y < self.world.height - 1:
            if self.world.is_free(self.x, self.y + 1) or self.world.get_organism_by_pos(self.x, self.y + 1).str < self.str:
                self.confirm_move(self.x, self.y + 1)
        elif r == 3 and self.y > 0:
            if self.world.is_free(self.x, self.y - 1) or self.world.get_organism_by_pos(self.x, self.y - 1).str < self.str:
                self.confirm_move(self.x, self.y - 1)

        self.check_collision()

    def reproduce(self):
        x, y = self.world.get_free_adj(self.x, self.y)
        if x is not None and y is not None:
            return Fox(x, y, self.world)
        else:
            return None

    def confirm_move(self, x, y):
        self.last_x = self.x
        self.last_y = self.y
        self.x = x
        self.y = y

    def __str__(self):
        return "Fox"
