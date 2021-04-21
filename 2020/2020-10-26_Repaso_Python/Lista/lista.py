from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("lista.ui", self)
        self.agregar.clicked.connect(self.on_agregar)
        # self.editar.clicked.connect(self.on_editar)
        self.lista.itemDoubleClicked.connect(self.on_editar)
        self.quitar.clicked.connect(self.on_quitar)

    def on_agregar(self):
        self.lista.addItem(self.nombre.text())
        self.nombre.setText('')

    def on_editar(self):
        texto_item = self.lista.currentItem().text()
        nuevo_texto, ok = QInputDialog.getText(
            self, 'Editar', 'Ingrese nuevo nombre', text=texto_item)
        if ok:
            self.lista.currentItem().setText(nuevo_texto)

    def on_quitar(self):
        self.lista.takeItem(self.lista.currentRow())


app = QApplication([])

win = MiVentana()
win.show()

app.exec_()
