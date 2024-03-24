from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from .config import WINDOW_WIDTH, WINDOW_HEIGHT

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AppName")
        #self.setWindowIcon(QIcon("..."))

        self.__set_geometry()

    def __set_geometry(self) -> None:
        self.showNormal()

        screen_size = QApplication.primaryScreen().size()
        window_x = int((screen_size.width() - WINDOW_WIDTH) / 2)
        window_y = int((screen_size.height() - WINDOW_HEIGHT) / 2)

        self.setGeometry(window_x, window_y, WINDOW_WIDTH, WINDOW_HEIGHT)