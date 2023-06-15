from PyQt6.QtWidgets import *


class AlertBox(QWidget):
    def __init__(self):
        super().__init__()
        self.alert_area = QTextEdit()
        self.alert_area.setReadOnly(True)

        self.alerts_layout = QHBoxLayout()
        self.alerts_layout.addWidget(self.alert_area)

        self.setLayout(self.alerts_layout)

    def add_alert(self, text):
        self.alert_area.append(text)

    def wipe_alerts(self):
        self.alert_area.clear()
