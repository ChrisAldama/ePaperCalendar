# This Python file uses the following encoding: utf-8
import sys
from CalendarWidget import CalendarWidget
from epd.contants import EPD_WIDTH, EPD_HEIGHT
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout)


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.calendar = CalendarWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.setMargin(0)
        layout.setSpacing(0)
        self.setLayout(layout)
        self.resize(EPD_HEIGHT, EPD_WIDTH)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
