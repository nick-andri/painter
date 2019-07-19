import sys
from PySide2.QtWidgets import QApplication, QWidget,QSlider
from PySide2.QtGui import QPainter, QPaintEvent
from PySide2 import QtCore,QtWidgets

class MonPainter(QWidget):
    def __init__(self, parent=None):
        super(MonPainter, self).__init__(parent)
        self.valeur= 0


    def paintEvent(self, event:QPaintEvent):
        p = QPainter(self)
        p.setBrush(QtCore.Qt.blue)

        taille = min(self.width(),self.height())

        p.drawRect(10,10,taille-20, taille-20)
        p.setBrush(QtCore.Qt.yellow)
        p.drawEllipse(20,20,taille-40, taille-40)


        p.translate(taille/2,taille/2)
        p.rotate(135 + self.valeur*2.7)

        p.drawLine(0,0,0,taille/3)



    def setValeur(self,val):
        self.valeur = val
        self.update()

class MaFenetrePrincipale(QWidget):

    def __init__(self,parent = None):
        super(MaFenetrePrincipale,self).__init__(parent)

        self.compteur = MonPainter()
        self.slider = QSlider(QtCore.Qt.Horizontal)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.compteur)
        self.layout.addWidget(self.slider)
        self.setLayout(self.layout)
        self.slider.valueChanged.connect(self.compteur.setValeur)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    maFen = MaFenetrePrincipale()
    maFen.show()
    sys.exit(app.exec_())