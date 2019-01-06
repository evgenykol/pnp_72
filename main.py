import sys
# Импортируем наш интерфейс из файла
from test import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        #self.ui.pushButton.clicked.connect(self.MyFunction)
        self.ui.actionRun.triggered.connect(self.MyFunction)
        self.ui.menuFire.triggered.connect(self.myRotate)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def MyFunction(self):
        scene = QtWidgets.QGraphicsScene()
        #scene.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(255,170,255), QtCore.Qt.SolidPattern))
        self.ui.graphicsView.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.green)

        r = QtCore.QRectF(QtCore.QPointF(20, 20), QtCore.QSizeF(20, 20))
        scene.addRect(r, pen)


        #scene = QtWidgets.QGraphicsScene(self.ui.graphicsView)
        #scene.setBackgroundBrush(QtGui.QBrush(QtGui.QColor.yellow()))
        #scene.setBackgroundBrush(QtGui.QColor("red"))
        #self.ui.graphicsView.setScene(scene)

        pnpBack = QtSvg.QGraphicsSvgItem("pnp-72-3.svg")
        #pnpBack.setRotation(90)
        scene.addItem(pnpBack)

    def myRotate(self):
        self.ui.scene.pnpBack.setRotation(180)




        #svgWidget.show()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    #myapp.MyFunction()
    myapp.show()
    sys.exit(app.exec_())
