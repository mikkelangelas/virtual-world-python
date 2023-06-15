from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from .SpawnBox import SpawnBox


class GridField(QWidget):
    def __init__(self, world, spawn_x, spawn_y):
        super().__init__()

        self.world = world

        self.spawn_x = spawn_x
        self.spawn_y = spawn_y
        self.occupied = False
        self.color = None
        self.label = None

        self.spawn_button = QPushButton()
        self.spawn_button.setMaximumSize(20, 20)
        self.spawn_button.setStyleSheet("background-color:black;border:none;")
        self.spawn_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.spawn_button.clicked.connect(self.init_spawn)

        self.field_layout = QVBoxLayout()
        self.field_layout.addWidget(self.spawn_button)

        self.setLayout(self.field_layout)

        self.spawn_window = None

    def set_occupation(self, o):
        self.spawn_button.setStyleSheet("background-color:"+o.color+";"+"border:none;")
        self.spawn_button.setText(o.label)
        self.update()

    def free_occupation(self):
        self.spawn_button.setStyleSheet("background-color:black;border:none;")
        self.spawn_button.setText("")
        self.update()

    def init_spawn(self):
        self.spawn_window = SpawnBox(self.world, self.spawn_x, self.spawn_y)
