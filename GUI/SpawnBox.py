from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class SpawnBox(QMainWindow):
    def __init__(self, world, spawn_x, spawn_y):
        super().__init__()
        self.world = world
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y

        self.spawn_list = QListWidget()
        self.spawn_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
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

        self.confirm_button = QPushButton("Spawn")
        self.confirm_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.confirm_button.clicked.connect(self.spawn_organism)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.cancel_button.clicked.connect(self.close_spawn_box)

        self.spawn_layout = QVBoxLayout()
        self.spawn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spawn_layout.addWidget(self.spawn_list)
        self.spawn_layout.addWidget(self.confirm_button)
        self.spawn_layout.addWidget(self.cancel_button)

        self.spawn_widget = QWidget()
        self.spawn_widget.setLayout(self.spawn_layout)

        self.setCentralWidget(self.spawn_widget)

        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.show()

    def spawn_organism(self):
        organism_type = self.spawn_list.currentItem().text()
        self.world.spawn_organism(organism_type, self.spawn_x, self.spawn_y)
        self.world.update_world()
        self.close_spawn_box()

    def close_spawn_box(self):
        self.world.window.setFocus()
        self.close()
