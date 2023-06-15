from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from World import World
from .GridBox import GridBox
from .AlertBox import AlertBox
from .ControlBox import ControlBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width_label = None
        self.width_input = None
        self.height_label = None
        self.height_input = None
        self.proceed_button = None
        self.menu_layout = None
        self.menu_widget = None

        self.controls = None
        self.grid = None
        self.alerts = None
        self.game_layout = None
        self.game_widget = None

        self.world = None

        self.init_menu()

    def init_menu(self):
        self.resize(400, 400)
        self.setWindowTitle("Virtual world")

        self.width_label = QLabel("Enter width:")

        self.width_input = QLineEdit()
        self.width_input.setValidator(QIntValidator())
        self.width_input.setFixedSize(200, 25)

        self.height_label = QLabel("Select height")

        self.height_input = QLineEdit()
        self.height_input.setValidator(QIntValidator())
        self.height_input.setFixedSize(200, 25)

        self.proceed_button = QPushButton("Proceed")
        self.proceed_button.clicked.connect(self.init_game)

        self.menu_layout = QVBoxLayout()
        self.menu_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.menu_layout.addWidget(self.width_label)
        self.menu_layout.addWidget(self.width_input)
        self.menu_layout.addWidget(self.height_label)
        self.menu_layout.addWidget(self.height_input)
        self.menu_layout.addWidget(self.proceed_button)

        self.menu_widget = QWidget(self)
        self.menu_widget.setLayout(self.menu_layout)

        self.setCentralWidget(self.menu_widget)

    def init_game(self):
        self.resize(800, 600)
        x = int(self.width_input.text())
        y = int(self.height_input.text())
        self.world = World(x, y, self)

        self.controls = ControlBox(self.world)
        self.grid = GridBox(self.world)
        self.alerts = AlertBox()

        self.game_layout = QHBoxLayout()
        self.game_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.game_layout.addWidget(self.controls)
        self.game_layout.addWidget(self.grid)
        self.game_layout.addWidget(self.alerts)

        self.game_widget = QWidget(self)
        self.game_widget.setLayout(self.game_layout)

        self.setCentralWidget(self.game_widget)
        self.world.update_world()

    def keyPressEvent(self, key_event):
        k = key_event.key()
        if k == Qt.Key.Key_Up.value or k == Qt.Key.Key_Right.value or k == Qt.Key.Key_Down.value or k == Qt.Key.Key_Left.value:
            if self.world is not None and self.world.get_human() is not None:
                self.world.turn(k)
