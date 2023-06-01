from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class ControlBox(QWidget):
    def __init__(self, world):
        super().__init__()

        self.world = world

        self.turn_button = QPushButton("New turn")
        self.turn_button.clicked.connect(self.world.turn)

        self.skill_button = QPushButton("Use skill")
        self.skill_button.clicked.connect(self.world.get_human().activate_skill)

        self.save_button = QPushButton("Save game")
        self.save_button.clicked.connect(self.world.save_state)

        self.load_button = QPushButton("Load game")
        self.load_button.clicked.connect(self.world.load_state)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.world.window.close)

        self.skill_info = QLineEdit()
        self.skill_info.setReadOnly(True)

        self.controls_layout = QVBoxLayout()
        self.controls_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.controls_layout.addWidget(self.turn_button)
        self.controls_layout.addWidget(self.skill_button)
        self.controls_layout.addWidget(self.save_button)
        self.controls_layout.addWidget(self.load_button)
        self.controls_layout.addWidget(self.exit_button)

        self.setLayout(self.controls_layout)
