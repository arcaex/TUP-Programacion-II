from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5 import uic
from menu import menu

class login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        self.menu = menu()
        self.entrar.clicked.connect(self.login)
        #Setear el campo de texto qtext con una máscara de asteriscos (*)
        self.clave.setEchoMode(QLineEdit.Password)
        self.cerrar.clicked.connect(self.cerrarWin)

    def login(self):
        usuario = self.usuario.text()
        clave = self.clave.text()
        if usuario=="admin" and clave=="admin":
            self.menu.show()
            self.setEnabled(False)
        else:
            print("Credenciales Erroneas")
    
    def cerrarWin(self):
        self.menu.hide()


app = QApplication([])

loginWin = login()
loginWin.show()

app.exec_()