from PyQt6.QtWidgets import *
from .SpawnBox import SpawnBox


# todo repair this shit


class GridField(QWidget):
    def __init__(self, world, spawn_x, spawn_y):
        super().__init__()

        self.world = world

        self.spawn_x = spawn_x
        self.spawn_y = spawn_y
        self.occupied = False
        self.occupating = None

        self.spawn_button = QToolButton()
        self.spawn_button.setAutoRaise(True)

        self.spawn_window = None

    def set_occupating(self, o):
        self.occupating = o

    def init_spawn(self):
        self.spawn_window = SpawnBox(self.world, self.spawn_x, self.spawn_y)

