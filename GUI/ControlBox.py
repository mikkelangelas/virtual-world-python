from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class ControlBox(QWidget):
    def __init__(self, world):
        super().__init__()

        self.world = world

        self.turn_button = QPushButton("New turn")
        self.turn_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.turn_button.clicked.connect(self.world.turn)

        self.skill_button = QPushButton("Use skill")
        self.skill_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.skill_button.clicked.connect(self.activate_skill)

        self.save_button = QPushButton("Save game")
        self.save_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.save_button.clicked.connect(self.world.save_state)

        self.load_button = QPushButton("Load game")
        self.load_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.load_button.clicked.connect(self.world.load_state)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
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
        self.controls_layout.addWidget(self.skill_info)

        self.setLayout(self.controls_layout)

    def update_skill_status(self):
        cooldown = getattr(self.world.get_human(), "cooldown")
        if cooldown == 0:
            self.skill_info.setText("Skill is ready to use!")
        elif cooldown > 5:
            self.skill_info.setText("Skill is active: " + str(cooldown - 5))
        else:
            self.skill_info.setText("Skill is on cooldown: " + str(cooldown))

    def activate_skill(self):
        self.world.get_human().activate_skill()
