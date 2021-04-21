from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5 import uic
from menu import menu
import sqlite3

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
        nick = self.usuario.text()
        clave = self.clave.text()
        #Viene la conexión a la DB (Abstraer)
        conexion = sqlite3.connect('../base_ejemplo.db')
        cursor = conexion.cursor()
        cursor.execute("""SELECT * FROM Jugadores WHERE nick='"""+nick+"""' AND clave='"""+clave+"""'""")
        conexion.commit()
        rows = cursor.fetchall()
        conexion.close()
        #Fin de la Conexión a la DB
        
        if len(rows)==1:
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