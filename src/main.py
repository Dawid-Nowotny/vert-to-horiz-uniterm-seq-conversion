import sys
from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow

def main():
    App = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(App.exec())