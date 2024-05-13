import sys
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt6.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget

class DynamicTableModel(QAbstractTableModel):
    def __init__(self, headers, data=None):
        super().__init__()
        self._headers = headers
        self._data = data or []

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        if self._data:
            return len(self._data[0])
        else:
            return 0

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]

if __name__ == "__main__":
    app = QApplication(sys.argv)

    headers = ["Column 1", "Column 2", "Column 3"]
    data = [
        ["Row 1", "Row 1", "Row 1"],
        ["Row 2", "Row 2", "Row 2"],
        ["Row 3", "Row 3", "Row 3"]
    ]

    model = DynamicTableModel(headers, data)
    table = QTableView()
    table.setModel(model)

    layout = QVBoxLayout()
    layout.addWidget(table)

    window = QWidget()
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())