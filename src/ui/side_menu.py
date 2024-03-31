from PyQt5.QtWidgets import QDockWidget, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox, QButtonGroup
from PyQt5 import QtCore
from typing import Optional

from .uniterm_dialog import UnitermDialog
from ui.info_dialog import InfoDialog
from .display_operations import DisplayOperations
from ui.alert import Alert
from data_shelter import DataShelter

class SideMenu(QDockWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__("Menu", parent)
        self.__init_UI()
        self.__set_layouts()

        self.setMaximumSize(162, 400)

        self.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)

    def __init_UI(self) -> None:
        self.__button_1 = QPushButton("Wprowadź pierwszy uniterm")
        self.__button_2 = QPushButton("Wprowadź drugi uniterm")
        self.__confirm_button = QPushButton("Rysuj")
        self.__clear_button = QPushButton("Wyczyść")
        self.__info_button = QPushButton("Informacja o aplikacji")

        self.__radio_group_first_second = QButtonGroup()
        self.__radio_first = QRadioButton("Za pierwszy")
        self.__radio_second = QRadioButton("Za drugi")
        self.__radio_first.setChecked(True)
        self.__radio_group_first_second.addButton(self.__radio_first)
        self.__radio_group_first_second.addButton(self.__radio_second)
        
        self.__radio_group_semi_comma = QButtonGroup()
        self.__radio_comma = QRadioButton(",")
        self.__radio_semi = QRadioButton(";")
        self.__radio_comma.setChecked(True)
        self.__radio_group_semi_comma.addButton(self.__radio_semi)
        self.__radio_group_semi_comma.addButton(self.__radio_comma)

        self.__button_1.clicked.connect(lambda: self.__open_dialog("Wprowadź pierwszy uniterm", "Wprowadź wartość x", "Wprowadź wartość y", True))
        self.__button_2.clicked.connect(lambda: self.__open_dialog("Wprowadź drugi uniterm", "Wprowadź wartość A", "Wprowadź wartość B", False))
        self.__confirm_button.clicked.connect(lambda: self.__confirm())
        self.__clear_button.clicked.connect(lambda: self.__clear_window())
        self.__info_button.clicked.connect(lambda: self.__open_info_dialog())

    def __set_layouts(self) -> None:
        self.__side_menu_widget = QWidget()

        vbox = QVBoxLayout()
        vbox_radio1 = QVBoxLayout()
        vbox_radio2 = QVBoxLayout()
        hbox = QHBoxLayout()

        vbox.addWidget(QWidget())

        vbox.addWidget(self.__button_1)
        vbox.addWidget(self.__button_2)

        vbox_radio1.addWidget(self.__radio_first)
        vbox_radio1.addWidget(self.__radio_second)
        vbox_radio2.addWidget(self.__radio_semi)
        vbox_radio2.addWidget(self.__radio_comma)

        hbox.addLayout(vbox_radio1)
        hbox.addLayout(vbox_radio2)
        vbox.addLayout(hbox)

        vbox.addWidget(self.__confirm_button)
        vbox.addWidget(self.__clear_button)
        vbox.addWidget(self.__info_button)
        vbox.addStretch()

        self.__side_menu_widget.setLayout(vbox)
        self.setWidget(self.__side_menu_widget)

    def __open_dialog(self, window_title: str, text_1: str, text_2: str, uniterm_type_first: bool) -> None:
        dialog = UnitermDialog(window_title, text_1, text_2, uniterm_type_first)
        dialog.exec_()
    
    def __open_info_dialog(self) -> None:
        dialog = InfoDialog()
        dialog.exec_()

    def __confirm(self) -> None:
        try: 
            data_shelter = DataShelter()

            if data_shelter.uniterm_1 is None or data_shelter.uniterm_2 is None:
                alert = Alert("Informacja", "Nie wpisałeś wszystkich wartości", QMessageBox.Information, self)
                alert.show()
                return
            
            if self.__radio_comma.isChecked():
                break_sign = ","
            elif self.__radio_semi.isChecked():
                break_sign = ";"

            if self.__radio_first.isChecked():
                type_first = True
            elif self.__radio_second.isChecked():
                type_first = False
            
            self.parent().display_operation = DisplayOperations(data_shelter.uniterm_1.a, data_shelter.uniterm_1.b, data_shelter.uniterm_2.a, data_shelter.uniterm_2.b, 
                                                                break_sign, type_first)
            
            self.parent().setCentralWidget(self.parent().display_operation)

        except Exception as e:
            alert = Alert("Bląd", f"Błąd podczas zamiany unitermów: {e}", QMessageBox.Critical, self)
            alert.show()
    
    def __clear_window(self) -> None:
        self.parent().clear_widget()