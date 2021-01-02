import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.run)
        self.show()

    def run(self):
        painter = QPainter()
        painter.begin(self)
        painter.drawEllipse(self, random.randrange(3, 30))
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


