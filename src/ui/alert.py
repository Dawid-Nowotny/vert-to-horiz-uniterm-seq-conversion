from PyQt5.QtWidgets import QMessageBox, QWidget
from typing import Optional

class Alert:
    def __init__(self, title: str, message: str, icon: QMessageBox.Icon, parent: Optional[QWidget] = None):
        self.__title = title
        self.__message = message
        self.__icon = icon
        self.__parent = parent

    def show(self) -> None:
        alert = QMessageBox(self.__parent)
        alert.setWindowTitle(self.__title)
        alert.setText(self.__message)
        alert.setIcon(self.__icon)
        alert.exec_()