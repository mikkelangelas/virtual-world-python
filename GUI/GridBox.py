from PyQt6.QtWidgets import *
from .GridField import GridField


# todo repair this shit


class GridBox(QWidget):
    def __init__(self, world):
        super().__init__()

        self.world = world

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(20)

        self.field_array = [[]]

        for i in range(self.world.height):
            for j in range(self.world.width):
                self.field_array[i][j] = GridField(self.world, j, i)
                self.grid_layout.addWidget(self.field_array[i][j], j + 1, i + 1)

        self.setLayout(self.grid_layout)

    def get_grid(self, x, y):
        return self.field_array[y][x]

