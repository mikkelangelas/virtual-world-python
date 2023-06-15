from .Animal import Animal
from PyQt6.QtCore import *


class Human(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.str = 5
        self.init = 4
        self.cooldown = 0
        self.invincible = False
        self.label = 'H'
        self.color = "#e8c49e"

    def action(self, player_input):
        if player_input != 0:
            self.free_field()

            if player_input == Qt.Key.Key_Right and self.x < self.world.width - 1:
                self.x += 1
            elif player_input == Qt.Key.Key_Left and self.x > 0:
                self.x -= 1
            elif player_input == Qt.Key.Key_Down and self.y < self.world.height - 1:
                self.y += 1
            elif player_input == Qt.Key.Key_Up and self.y > 0:
                self.y -= 1

            self.check_collision()

            if self.cooldown > 0:
                self.cooldown -= 1
            if self.cooldown == 5:
                self.invincible = False

    def collision(self, other):
        if self.invincible is True:
            self.x, self.y = self.world.get_free_adj(self.x, self.y)
            self.world.send_alert(self.__str__() + " is invincible and evaded " + other.__str__())
        else:
            super().collision(other)

    def reproduce(self):
        pass

    def activate_skill(self):
        if self.cooldown == 0:
            self.cooldown = 10
            self.invincible = True

    def set_invincibility(self, cooldown, invincible):
        self.cooldown = cooldown
        self.invincible = invincible

    def __str__(self):
        return "Human"
