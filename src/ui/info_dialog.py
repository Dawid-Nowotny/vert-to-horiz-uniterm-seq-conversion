from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from PyQt5 import QtCore

class InfoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Informacje o aplikacji")

        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedWidth(250)

        self.__set_layouts()

    def __set_layouts(self) -> None:
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("Aplikacja realizująca zamianę unitermu pionowej"), alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(QLabel("operacji sekwencjowania unitermów na poziomą"), alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(QLabel("operację sekwencjowania unitermów."), alignment=QtCore.Qt.AlignCenter)

        author_label = QLabel("<a href='https://github.com/Dawid-Nowotny'>Autor: Dawid Nowotny</a>")
        author_label.setOpenExternalLinks(True)
        vbox.addWidget(author_label, alignment=QtCore.Qt.AlignCenter)

        self.setLayout(vbox)