from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from typing import Optional

class DisplayOperations(QWidget):
    def __init__(self, x: str, y: str, a: str, b: str, break_sign: str, type_first: bool, parent: Optional[QWidget] = None):
        super().__init__(parent)

        self.__set_operands_text_location(x, y, a, b, break_sign)

        if type_first:
            self.__init_first_type_operation(a, b, y, break_sign)
        if not type_first:
            self.__init_second_type_operation(x, a, b, break_sign)

        self.setLayout(self.__vbox)

    def __set_operands_text_location(self, x: str, y: str, a: str, b: str, break_sign: str) -> None:
        self.__vbox = QVBoxLayout()
        top_hbox = QHBoxLayout()
        
        top_left_hbox = QHBoxLayout()
        top_left_vbox = QVBoxLayout()

        top_left_hbox.addWidget(QLabel("("), alignment=QtCore.Qt.AlignCenter)
        top_left_vbox.addWidget(QLabel(x))
        top_left_vbox.addWidget(QLabel(break_sign), alignment=QtCore.Qt.AlignLeft)
        top_left_vbox.addWidget(QLabel(y))
        top_left_hbox.addLayout(top_left_vbox)

        top_right_vbox = QVBoxLayout()
        top_right_hbox = QHBoxLayout()

        top_right_vbox.addWidget(QLabel("͡ ")), #alignment=QtCore.Qt.AlignCenter)
        top_right_hbox.addWidget(QLabel(a))
        top_right_hbox.addWidget(QLabel(break_sign), alignment=QtCore.Qt.AlignLeft)
        top_right_hbox.addWidget(QLabel(b))
        top_right_vbox.addLayout(top_right_hbox)

        top_hbox.addLayout(top_left_hbox)
        top_hbox.addLayout(top_right_vbox)

        self.__vbox.addLayout(top_hbox)

    def __init_first_type_operation(self, a: str, b: str, y :str, break_sign: str) -> None:
        self.__vbox.addWidget(QLabel("Sekwencjonowanie za pierwszy"), alignment=QtCore.Qt.AlignCenter)
        hbox_ab = QHBoxLayout()
        middle_vbox = QVBoxLayout()
        result_hbox = QHBoxLayout()

        hbox_ab.addWidget(QLabel(a))
        hbox_ab.addWidget(QLabel(break_sign), alignment=QtCore.Qt.AlignLeft)
        hbox_ab.addWidget(QLabel(b))

        middle_vbox.addWidget(QLabel("͡ "))#, alignment=QtCore.Qt.AlignCenter)
        middle_vbox.addLayout(hbox_ab)
        middle_vbox.addWidget(QLabel(break_sign), alignment=QtCore.Qt.AlignLeft)
        middle_vbox.addWidget(QLabel(y))

        result_hbox.addWidget(QLabel("("))
        result_hbox.addLayout(middle_vbox)

        self.__vbox.addLayout(result_hbox)

    def __init_second_type_operation(self, x: str, a: str, b: str, break_sign: str) -> None:
        self.__vbox.addWidget(QLabel("Sekwencjonowanie za drugi"), alignment=QtCore.Qt.AlignCenter)

        hbox_ab = QHBoxLayout()
        middle_vbox = QVBoxLayout()
        result_hbox = QHBoxLayout()

        hbox_ab.addWidget(QLabel(a))
        hbox_ab.addWidget(QLabel(break_sign), alignment=QtCore.Qt.AlignLeft)
        hbox_ab.addWidget(QLabel(b))

        middle_vbox.addWidget(QLabel(x))
        middle_vbox.addWidget(QLabel(break_sign), alignment=QtCore.Qt.AlignLeft)
        middle_vbox.addWidget(QLabel("͡ "))#, alignment=QtCore.Qt.AlignCenter)
        middle_vbox.addLayout(hbox_ab)

        result_hbox.addWidget(QLabel("("))
        result_hbox.addLayout(middle_vbox)

        self.__vbox.addLayout(result_hbox)