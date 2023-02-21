import sys
from random import randint

from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtCore


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False
    
    def run(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QtCore.Qt.yellow)
        size = randint(20, 150)
        qp.drawEllipse(randint(0, 450), randint(0, 300), size, size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())