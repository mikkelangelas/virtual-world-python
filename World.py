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
import math


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
            r = random.randint(1, 11)
            while True:
                rx = random.randint(1, self.width - 1)
                ry = random.randint(1, self.height - 1)

                if self.is_free(rx, ry):
                    break

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

    def update_world(self):
        for o in self.organisms:
            if o.dead is False:
                self.window.grid.get_grid(o.x, o.y).set_occupation(o)

        self.window.controls.update_skill_status()

    def turn(self, player_input=0):
        self.sort_by_init()
        self.window.alerts.wipe_alerts()

        for o in self.organisms:
            if o.dead is False:
                if isinstance(o, Human):
                    o.action(player_input)
                else:
                    o.action()

        self.dispose_of_deceased()
        self.update_world()

    def sort_by_init(self):
        self.organisms.sort(key=lambda o: (o.init, o.age), reverse=True)

    def dispose_of_deceased(self):
        for o in self.organisms:
            if o.dead is True:
                self.organisms.remove(o)

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

    def get_organism_by_pos(self, x, y):
        for o in self.organisms:
            if o.x == x and o.y == y:
                return o

        return None

    def send_alert(self, text):
        self.window.alerts.add_alert(text)

    def get_human(self):
        for o in self.organisms:
            if isinstance(o, Human):
                return o

        return None

    def increase_occupied(self):
        self.occupied += 1

    def decrease_occupied(self):
        self.occupied -= 1

    def get_heracleum(self, s):
        h = None

        for o in self.organisms:
            if isinstance(o, Heracleum) and o.is_targeted is False:
                if h is None or math.sqrt(pow(s.x - o.x, 2) + pow(s.y - o.y, 2)) < math.sqrt(pow(s.x - h.x, 2) + pow(s.y - h.y, 2)):
                    h = o

        return h

    def spawn_organism(self, organism_type, x, y):
        if organism_type == "Wolf":
            self.organisms.append(Wolf(x, y, self))
        elif organism_type == "Turtle":
            self.organisms.append(Turtle(x, y, self))
        elif organism_type == "Sheep":
            self.organisms.append(Sheep(x, y, self))
        elif organism_type == "Fox":
            self.organisms.append(Fox(x, y, self))
        elif organism_type == "Cybersheep":
            self.organisms.append(Cybersheep(x, y, self))
        elif organism_type == "Antelope":
            self.organisms.append(Antelope(x, y, self))
        elif organism_type == "Grass":
            self.organisms.append(Grass(x, y, self))
        elif organism_type == "Dandelion":
            self.organisms.append(Dandelion(x, y, self))
        elif organism_type == "Guarana":
            self.organisms.append(Guarana(x, y, self))
        elif organism_type == "Nightshade":
            self.organisms.append(Nightshade(x, y, self))
        elif organism_type == "Heracleum":
            self.organisms.append(Heracleum(x, y, self))

        self.increase_occupied()

    def save_state(self):
        handle = open("state.txt", "w")
        handle.write(str(self.width) + '\n')
        handle.write(str(self.height) + '\n')
        handle.write(str(self.occupied) + '\n')
        for o in self.organisms:
            handle.write(o.__str__() + '\n')
            handle.write(str(getattr(o, "str")) + '\n')
            handle.write(str(getattr(o, "x")) + '\n')
            handle.write(str(getattr(o, "y")) + '\n')
            if isinstance(o, Human):
                handle.write(str(getattr(o, "cooldown")) + '\n')
                handle.write(str(getattr(o, "invincible")) + '\n')

        handle.close()

    def load_state(self):
        handle = open("state.txt", "r")
        self.width = int(handle.readline())
        self.height = int(handle.readline())
        self.size = self.width * self.height
        self.occupied = int(handle.readline())
        self.organisms.clear()
        for _ in range(self.occupied):
            new_o = None
            o_type = handle.readline().rstrip('\n')
            o_str = int(handle.readline())
            o_x = int(handle.readline())
            o_y = int(handle.readline())
            if o_type == "Human":
                o_cooldown = int(handle.readline())
                o_invincible = bool(handle.readline())
                new_o = Human(o_x, o_y, self)
                setattr(new_o, "cooldown", o_cooldown)
                setattr(new_o, "invincible", o_invincible)
            elif o_type == "Wolf":
                new_o = Wolf(o_x, o_y, self)
            elif o_type == "Turtle":
                new_o = Turtle(o_x, o_y, self)
            elif o_type == "Sheep":
                new_o = Sheep(o_x, o_y, self)
            elif o_type == "Fox":
                new_o = Fox(o_x, o_y, self)
            elif o_type == "Cybersheep":
                new_o = Cybersheep(o_x, o_y, self)
            elif o_type == "Antelope":
                new_o = Antelope(o_x, o_y, self)
            elif o_type == "Grass":
                new_o = Grass(o_x, o_y, self)
            elif o_type == "Dandelion":
                new_o = Dandelion(o_x, o_y, self)
            elif o_type == "Guarana":
                new_o = Guarana(o_x, o_y, self)
            elif o_type == "Nightshade":
                new_o = Nightshade(o_x, o_y, self)
            elif o_type == "Heracleum":
                new_o = Heracleum(o_x, o_y, self)

            if new_o is not None:
                setattr(new_o, "str", o_str)
                self.organisms.append(new_o)

        self.window.grid.wipe_grid()
        self.update_world()
        handle.close()
