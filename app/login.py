from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from .forms.login import Ui_LoginWindow
from .db_scripts.user_scripts import user
from .main_form import MainWindow


class Login(QMainWindow, Ui_LoginWindow):

    login_correct = pyqtSignal()
    main_window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.usr = user
        self.login.clicked.connect(self.chec_user)
        self.register_user.clicked.connect(self.registerate_user)


    def chec_user(self):
        user = self.usr.check_user(self.name_input.text(), self.pass_input.text())
        if user['code'] == 200:
            self.usr.activ_user(int(user['data'][0]), user['data'][1])
            print(self.usr.__dict__)
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()

    def registerate_user(self):
        register_user = self.usr.create_user(self.name_input.text(), self.pass_input.text())
        print(register_user)
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()