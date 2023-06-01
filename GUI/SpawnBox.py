from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class SpawnBox(QMainWindow):
    def __init__(self, world, spawn_x, spawn_y):
        super().__init__()
        self.world = world
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y

        self.spawn_list = QListWidget()
        QListWidgetItem("Wolf", self.spawn_list)
        QListWidgetItem("Sheep", self.spawn_list)
        QListWidgetItem("Fox", self.spawn_list)
        QListWidgetItem("Turtle", self.spawn_list)
        QListWidgetItem("Antelope", self.spawn_list)
        QListWidgetItem("Cybersheep", self.spawn_list)
        QListWidgetItem("Grass", self.spawn_list)
        QListWidgetItem("Dandelion", self.spawn_list)
        QListWidgetItem("Guarana", self.spawn_list)
        QListWidgetItem("Nightshade", self.spawn_list)
        QListWidgetItem("Heracleum", self.spawn_list)

        self.confirm_button = QPushButton()
        self.cancel_button = QPushButton()

        self.spawn_layout = QVBoxLayout()
        self.spawn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.show()

    def spawn_organism(self):
        o = self.spawn_list.selectedItems()
