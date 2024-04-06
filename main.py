from PyQt6.QtWidgets import QApplication
import sys
from app.login import Login
from app.db_scripts.user_scripts import User


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()