from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("boton.ui", self)
        self.boton.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.etiqueta.setText("Chau mundo!")


app = QApplication([])

win = MiVentana()
win.show()

app.exec_()
