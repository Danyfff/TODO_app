from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize, Qt
import sys
from random import choice
from forms.login import Ui_MainWindow
from settings import DB_PATH
from BD import DBManager


window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]  

class Login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# Приложению нужен один (и только один) экземпляр QApplication.
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# # Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
# app = QApplication(sys.argv)
# # Создаём виджет Qt — окно.
# window = Login()
# window.show()  # Важно: окно по умолчанию скрыто.

# # Запускаем цикл событий.
# app.exec()
if __name__ == '__main__': 
    base_manager = DBManager(DB_PATH)