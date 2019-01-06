# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.graphicsView.setTabletTracking(False)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView.setForegroundBrush(brush)
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFire = QtWidgets.QMenu(self.menubar)
        self.menuFire.setObjectName("menuFire")
        MainWindow.setMenuBar(self.menubar)
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.menuFile.addAction(self.actionRun)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFire.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFire.setTitle(_translate("MainWindow", "Fire"))
        self.actionRun.setText(_translate("MainWindow", "Run"))

