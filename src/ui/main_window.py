from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from .side_menu import SideMenu

from .config import WINDOW_WIDTH, WINDOW_HEIGHT

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("V2H Uniterm")

        self.__init_UI()
        self.__set_geometry()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

    def __init_UI(self) -> None:
        self.display_operations = QWidget()
        side_menu = SideMenu(self)
        
        self.addDockWidget(1, side_menu)
        self.setCentralWidget(self.display_operations)

    def __set_geometry(self) -> None:
        self.showNormal()

        screen_size = QApplication.primaryScreen().size()
        window_x = int((screen_size.width() - WINDOW_WIDTH) / 2)
        window_y = int((screen_size.height() - WINDOW_HEIGHT) / 2)

        self.setMaximumSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setMinimumSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.setGeometry(window_x, window_y, WINDOW_WIDTH, WINDOW_HEIGHT)