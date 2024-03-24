from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QDialog, QLabel, QLineEdit, QSpacerItem, QSizePolicy

from uniterm.uniterm import Uniterm
from data_shelter import DataShelter

class UnitermDialog(QDialog):
    def __init__(self, window_title: str, text_1: str, text_2: str, uniterm_type_first: bool):
        super().__init__()
        self.setWindowTitle(window_title)
        self.__uniterm_type = uniterm_type_first

        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedWidth(250)

        self.__init_UI(text_1, text_2)
        self.__set_layouts()
    
    def __init_UI(self, text_1, text_2) -> None:
        self.__label_1 = QLabel(text_1, self)
        self.__line_edit_1 = QLineEdit(self)
        self.__label_2 = QLabel(text_2, self)
        self.__line_edit_2 = QLineEdit(self)
        self.__confirm = QPushButton('Zatwierdz', self)

        self.__confirm.clicked.connect(lambda: self.__confirm_uniterm())

    def __set_layouts(self) -> None:
        vbox = QVBoxLayout()

        vbox.addWidget(self.__label_1, alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(self.__line_edit_1)
        vbox.addWidget(self.__label_2, alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(self.__line_edit_2)


        vbox.addItem(QSpacerItem(0, 15, QSizePolicy.Minimum, QSizePolicy.Fixed))
        vbox.addWidget(self.__confirm)

        vbox.setAlignment(QtCore.Qt.AlignCenter)
        container = QtWidgets.QWidget()
        container.setLayout(vbox)

        self.setLayout(vbox)

    def showEvent(self, event) -> None:
        super().showEvent(event)
        data_shelter = DataShelter()
        
        if data_shelter.uniterm_1 is not None and self.__uniterm_type is True:
            self.__line_edit_1.setText(data_shelter.uniterm_1.a)
            self.__line_edit_2.setText(data_shelter.uniterm_1.b)

        if data_shelter.uniterm_2 is not None and self.__uniterm_type is False:
            self.__line_edit_1.setText(data_shelter.uniterm_2.a)
            self.__line_edit_2.setText(data_shelter.uniterm_2.b)
    
    def __confirm_uniterm(self) -> None:
        try:
            val_1 = self.__line_edit_1.text()
            val_2 = self.__line_edit_2.text()

            data_shelter = DataShelter()

            if self.__uniterm_type is True:
                data_shelter.uniterm_1 = Uniterm(val_1, val_2)

            elif self.__uniterm_type is False: 
                data_shelter.uniterm_2 = Uniterm(val_1, val_2)

            self.close()
        except Exception as e:
            print("An error occurred while confirming Uniterm:", e)