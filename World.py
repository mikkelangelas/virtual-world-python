from Animals.Human import Human
from Animals.Wolf import Wolf
from Animals.Sheep import Sheep
from Animals.Fox import Fox
from Animals.Turtle import Turtle
from Animals.Antelope import Antelope
from Animals.Cybersheep import Cybersheep
from Plants.Grass import Grass
from Plants.Dandelion import Dandelion
from Plants.Guarana import Guarana
from Plants.Nightshade import Nightshade
from Plants.Heracleum import Heracleum

import random


class World:
    def __init__(self, width, height, window):
        self.width = width
        self.height = height
        self.size = width*height
        self.window = window
        self.occupied = 1
        self.organisms = [Human(0, 0, self)]

        init_size = self.size//4
        # not borken anymore
        for _ in range(init_size):
            r = random.randint(1, 12)
            rx = random.randint(0, self.width - 1)
            ry = random.randint(0, self.height - 1)
            if r == 1:
                self.organisms.append(Wolf(rx, ry, self))
            elif r == 2:
                self.organisms.append(Sheep(rx, ry, self))
            elif r == 3:
                self.organisms.append(Fox(rx, ry, self))
            elif r == 4:
                self.organisms.append(Turtle(rx, ry, self))
            elif r == 5:
                self.organisms.append(Antelope(rx, ry, self))
            elif r == 6:
                self.organisms.append(Cybersheep(rx, ry, self))
            elif r == 7:
                self.organisms.append(Grass(rx, ry, self))
            elif r == 8:
                self.organisms.append(Dandelion(rx, ry, self))
            elif r == 9:
                self.organisms.append(Guarana(rx, ry, self))
            elif r == 10:
                self.organisms.append(Nightshade(rx, ry, self))
            elif r == 11:
                self.organisms.append(Heracleum(rx, ry, self))

            self.occupied += 1

    def turn(self, player_input=0):
        self.sort_by_init()
        for o in self.organisms:
            if isinstance(o, Human):
                o.action(player_input)
            else:
                o.action()

    def sort_by_init(self):
        self.organisms.sort(key=lambda o: (o.init, o.age), reverse=True)

    def is_free(self, x, y):
        for o in self.organisms:
            if o.x == x and o.y == y:
                return False
        return True

    def get_free_adj(self, x, y):
        new_x = x
        new_y = y
        if x < self.width - 1 and self.is_free(x + 1, y):
            new_x = x + 1
        elif x > 0 and self.is_free(x - 1, y):
            new_x = x - 1
        elif y < self.height - 1 and self.is_free(x, y + 1):
            new_y = y + 1
        elif y > 0 and self.is_free(x, y - 1):
            new_y = y - 1

        if new_x != x or new_y != y:
            return new_x, new_y
        else:
            return None, None

    def send_alert(self, text):
        self.window.alerts.add_alert(text)

    def get_human(self):
        for o in self.organisms:
            if isinstance(o, Human):
                return o

        return None

    def save_state(self):
        handle = open("state.txt", "w")
        handle.write(self.width)
        handle.write(self.height)
        handle.write(str(self.occupied))
        for o in self.organisms:
            handle.write(str(o.str))
            handle.write(str(o.init))
            handle.write(str(o.x))
            handle.write(str(o.y))
            handle.write(str(o.dead))


    def load_state(self):
        handle = open("state.txt", "r")
