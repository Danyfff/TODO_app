from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from .forms.main_window import Ui_MainWindow
from .db_scripts.notes_scripts import note
from .db_scripts.user_scripts import user


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_all_notes()
        
        
    def get_all_notes(self):
        row = 0
        print(user.id)
        notes = note.get_notes(int(user.id))["data"]
        print(notes)
        for nt in notes:
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(nt[1])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(nt[3])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(nt[4])))
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            row += 0