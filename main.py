import sys
from random import randint

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QColor, QPainter, QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1300, 300, 500, 500)
        self.setWindowTitle('random ellipse')

        self.Paint = False

        self.btn = QPushButton(self)
        self.btn.setGeometry(200, 230, 100, 40)
        font = QFont()
        font.setPointSize(10)
        self.btn.setFont(font)
        self.btn.setText('Push me!')

        self.btn.clicked.connect(self.spawn_ellipse)

    def spawn_ellipse(self):
        self.length, self.high, self.coords = self.random_size_coords()

        self.Paint = True
        self.repaint()

    def random_size_coords(self):
        Right = False

        x = randint(5, 100)
        y = randint(5, 100)

        coords = (randint(1, 500 - x), randint(1, 500 - y))
        while not Right:
            if not (100 < coords[0] < 305 and 130 < coords[1] < 275):
                Right = True
            else:
                coords = (randint(1, 500 - x), randint(1, 500 - y))
        print(coords)
        return x, y, coords

    def paintEvent(self, event):
        if self.Paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(self.coords[0], self.coords[1], self.length, self.high)
            qp.end()

            self.Paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
