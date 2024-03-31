from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from typing import Optional

from .seq_bracelet_widget import SeqBraceletWidget

class DisplayOperations(QWidget):
    def __init__(self, x: str, y: str, a: str, b: str, break_sign: str, type_first: bool, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.__vbox = QVBoxLayout()
        self.__character_font = QFont("Arial", 11)
        self.__break_font = QFont("Arial", 11)

        self.__set_operands_text_location(x, y, a, b, break_sign)

        if type_first:
            self.__init_first_type_operation(a, b, y, break_sign)
        if not type_first:
            self.__init_second_type_operation(x, a, b, break_sign)

        self.setLayout(self.__vbox)

    def __set_operands_text_location(self, x: str, y: str, a: str, b: str, break_sign: str) -> None:
        top_hbox = QHBoxLayout()
        top_left_hbox = QHBoxLayout()
        top_left_vbox = QVBoxLayout()
        top_right_vbox = QVBoxLayout()
        top_right_hbox = QHBoxLayout()
        bracket_normal = SeqBraceletWidget(1, 1, 40, 75, 90 * 16, 180 * 16, 10, 80)
        bracket_roof = SeqBraceletWidget(1, 1, 75, 40, 30 * 16, 120 * 16, 80, 10)

        top_left_hbox.addStretch()
        top_left_hbox.addWidget(bracket_normal, alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        top_left_vbox.addItem(QSpacerItem(0, 15, QSizePolicy.Minimum, QSizePolicy.Fixed))
        top_left_vbox.addStretch()
        top_left_vbox.addWidget(QLabel(x, font = self.__character_font))
        top_left_vbox.addWidget(QLabel(break_sign, font = self.__break_font), alignment=QtCore.Qt.AlignLeft)
        top_left_vbox.addWidget(QLabel(y, font = self.__character_font))
        top_left_vbox.addStretch()
        top_left_hbox.addLayout(top_left_vbox)
        top_left_vbox.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        top_left_hbox.addStretch()

        top_right_vbox.addStretch()
        top_right_vbox.addItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))
        top_right_hbox.addItem(QSpacerItem(7, 0, QSizePolicy.Minimum, QSizePolicy.Fixed))
        top_right_vbox.addWidget(bracket_roof, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        top_right_hbox.addStretch()
        top_right_hbox.addWidget(QLabel(a, font = self.__character_font), alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        top_right_hbox.addItem(QSpacerItem(10, 0, QSizePolicy.Minimum, QSizePolicy.Fixed))
        top_right_hbox.addWidget(QLabel(break_sign, font = self.__break_font), alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        top_right_hbox.addItem(QSpacerItem(10, 0, QSizePolicy.Minimum, QSizePolicy.Fixed))
        top_right_hbox.addWidget(QLabel(b, font = self.__character_font), alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        top_right_hbox.addItem(QSpacerItem(10, 0, QSizePolicy.Minimum, QSizePolicy.Fixed))
        top_right_hbox.addStretch()
        top_right_vbox.addLayout(top_right_hbox)
        top_right_vbox.addItem(QSpacerItem(0, 50, QSizePolicy.Minimum, QSizePolicy.Fixed))
        top_right_vbox.addStretch()
        
        top_hbox.addLayout(top_left_hbox)
        top_hbox.addLayout(top_right_vbox)

        self.__vbox.addLayout(top_hbox)

    def __init_first_type_operation(self, a: str, b: str, y :str, break_sign: str) -> None:
        self.__vbox.addWidget(QLabel("Sekwencjonowanie za pierwszy"), alignment=QtCore.Qt.AlignCenter)

        hbox_ab = QHBoxLayout()
        middle_vbox = QVBoxLayout()
        result_hbox = QHBoxLayout()
        bracket_normal = SeqBraceletWidget(1, 1, 40, 100, 90 * 16, 180 * 16, 10, 100)
        bracket_roof = SeqBraceletWidget(1, 1, 75, 40, 30 * 16, 120 * 16, 80, 10)

        hbox_ab.addStretch()
        hbox_ab.addWidget(QLabel(a, font = self.__character_font), alignment=QtCore.Qt.AlignLeft)
        hbox_ab.addWidget(QLabel(break_sign, font = self.__break_font), alignment=QtCore.Qt.AlignLeft)
        hbox_ab.addWidget(QLabel(b, font = self.__character_font), alignment=QtCore.Qt.AlignLeft)
        hbox_ab.addStretch()

        middle_vbox.addStretch()
        middle_vbox.addWidget(bracket_roof, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        middle_vbox.addLayout(hbox_ab)
        middle_vbox.addWidget(QLabel(break_sign, font = self.__break_font), alignment=QtCore.Qt.AlignLeft)
        middle_vbox.addWidget(QLabel(y, font = self.__character_font), alignment=QtCore.Qt.AlignCenter)
        middle_vbox.addStretch()

        result_hbox.addStretch()
        result_hbox.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        result_hbox.addWidget(bracket_normal, alignment=QtCore.Qt.AlignCenter)
        result_hbox.addLayout(middle_vbox)
        result_hbox.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        result_hbox.addStretch()

        self.__vbox.addLayout(result_hbox)

    def __init_second_type_operation(self, x: str, a: str, b: str, break_sign: str) -> None:
        self.__vbox.addWidget(QLabel("Sekwencjonowanie za drugi"), alignment=QtCore.Qt.AlignCenter)

        hbox_ab = QHBoxLayout()
        middle_vbox = QVBoxLayout()
        result_hbox = QHBoxLayout()
        bracket_normal = SeqBraceletWidget(1, 1, 40, 100, 90 * 16, 180 * 16, 10, 100)
        bracket_roof = SeqBraceletWidget(1, 1, 75, 40, 30 * 16, 120 * 16, 80, 10)

        hbox_ab.addStretch()
        hbox_ab.addWidget(QLabel(a, font = self.__character_font), alignment=QtCore.Qt.AlignLeft)
        hbox_ab.addWidget(QLabel(break_sign, font = self.__break_font), alignment=QtCore.Qt.AlignLeft)
        hbox_ab.addWidget(QLabel(b, font = self.__character_font), alignment=QtCore.Qt.AlignLeft)
        hbox_ab.addStretch()

        middle_vbox.addStretch()
        middle_vbox.addWidget(QLabel(x, font = self.__character_font), alignment=QtCore.Qt.AlignCenter)
        middle_vbox.addWidget(QLabel(break_sign, font = self.__break_font), alignment=QtCore.Qt.AlignLeft)
        middle_vbox.addWidget(bracket_roof, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        middle_vbox.addLayout(hbox_ab)
        middle_vbox.addStretch()

        result_hbox.addStretch()
        result_hbox.addWidget(bracket_normal, alignment=QtCore.Qt.AlignCenter)
        result_hbox.addLayout(middle_vbox)
        result_hbox.addStretch()

        self.__vbox.addLayout(result_hbox)