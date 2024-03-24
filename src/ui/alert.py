from PyQt5.QtWidgets import QMessageBox, QWidget
from typing import Optional

class Alert:
    def __init__(self, title: str, message: str, icon: QMessageBox.Icon, parent: Optional[QWidget] = None):
        self.title = title
        self.message = message
        self.icon = icon
        self.parent = parent

    def show(self) -> None:
        alert = QMessageBox(self.parent)
        alert.setWindowTitle(self.title)
        alert.setText(self.message)
        alert.setIcon(self.icon)
        alert.exec_()