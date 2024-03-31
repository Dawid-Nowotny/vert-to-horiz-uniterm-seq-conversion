from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from typing import Optional

class SeqBraceletWidget(QWidget):
    def __init__(self, x: int, y: int, w: int, h: int, a: int, alen: int, fixed_x: Optional[int], fixed_y: Optional[int], parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__a = a
        self.__alen = alen
        self.setFixedSize(fixed_x, fixed_y)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor("blue"))
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawArc(self.__x, self.__y, self.__w, self.__h, self.__a, self.__alen) 