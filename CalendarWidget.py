from datetime import datetime, timedelta
from Calendar import Calendar
from PySide2.QtWidgets import QWidget, QTableView, QHeaderView
from PySide2.QtCore import QAbstractTableModel, Qt

class CalendarWidget(QTableView):
    def __init__(self):
        QTableView.__init__(self)
        model = CalendarModel()
        self.setModel(model)
        self.setSortingEnabled(False)
        self.showGrid()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

class CalendarModel(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self)
        self.calendar = Calendar()
        self.updateData()
        self.header = ['L', 'M', 'M', 'J', 'V']

    def currentWeek(self):
        now = datetime.utcnow()
        start = now - timedelta(days=now.weekday())
        end = start + timedelta(days=4)
        return (start.isoformat() + 'Z', end.isoformat() + 'Z')

    def rowCount(self, index):
        return 12 # Number of hours to show

    def columnCount(self, index):
        return 5 # Number if week days

    def updateData(self):
        self.week = self.currentWeek()
        self.events = self.calendar.events(self.week)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role != Qt.DisplayRole:
            return None
        column = index.column()
        row = index.row() + 9 #Show events from 9 am
        return self.events[row, column]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.header[section]
        return str(9 + section) + ':00'
