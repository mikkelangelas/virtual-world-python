from PyQt6.QtWidgets import *
from .GridField import GridField


class GridBox(QWidget):
    def __init__(self, world):
        super().__init__()

        self.world = world

        self.grid_layout = QGridLayout()
        self.grid_layout.setVerticalSpacing(0)
        self.grid_layout.setHorizontalSpacing(0)
        self.resize(world.width * 20, world.height * 20)

        self.field_array = list()
        for i in range(self.world.height):
            self.field_array.append(list())
            for j in range(self.world.width):
                self.field_array[i].append(GridField(self.world, j, i))
                self.grid_layout.addWidget(self.field_array[i][j], i, j)

        self.setLayout(self.grid_layout)

    def get_grid(self, x, y):
        return self.field_array[y][x]


