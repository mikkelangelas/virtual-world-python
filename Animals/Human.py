from .Animal import Animal


class Human(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 5
        self.init = 4
        self.cooldown = 5
        self.invincible = False

    def action(self, player_input):
        if player_input == 1 and self.x < self.world.width - 1:
            self.x += 1
        elif player_input == 2 and self.x > 0:
            self.x -= 1
        elif player_input == 3 and self.y < self.world.height - 1:
            self.y += 1
        elif player_input == 4 and self.y > 0:
            self.y -= 1

    def reproduce(self):
        pass

    def activate_skill(self):
        if self.cooldown == 5:
            self.invincible = True

    def __str__(self):
        return "Human"
