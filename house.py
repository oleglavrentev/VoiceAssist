# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'house.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_House(object):
    def setupUi(self, House):
        House.setObjectName("House")
        House.resize(763, 419)
        House.setStyleSheet("background-color:rgb(85, 85, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(House)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 80, 691, 281))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        House.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(House)
        self.statusbar.setObjectName("statusbar")
        House.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(House)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 763, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        House.setMenuBar(self.menuBar)
        self.first = QtWidgets.QAction(House)
        self.first.setObjectName("first")
        self.second = QtWidgets.QAction(House)
        self.second.setObjectName("second")
        self.third = QtWidgets.QAction(House)
        self.third.setObjectName("third")
        self.fourth = QtWidgets.QAction(House)
        self.fourth.setObjectName("fourth")
        self.obth = QtWidgets.QAction(House)
        self.obth.setObjectName("obth")
        self.menu.addAction(self.first)
        self.menu.addAction(self.second)
        self.menu.addAction(self.third)
        self.menu.addAction(self.fourth)
        self.menu.addAction(self.obth)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(House)
        QtCore.QMetaObject.connectSlotsByName(House)

    def retranslateUi(self, House):
        _translate = QtCore.QCoreApplication.translate
        House.setWindowTitle(_translate("House", "MainWindow"))
        self.label.setText(_translate("House", "Вопросы про общежития"))
        self.menu.setTitle(_translate("House", "Вопросы про общежития"))
        self.first.setText(_translate("House", "Первое общежитие"))
        self.second.setText(_translate("House", "Второе общежитие"))
        self.third.setText(_translate("House", "Третье общежитие"))
        self.fourth.setText(_translate("House", "Четвертое общежитие"))
        self.obth.setText(_translate("House", "Общие вопросы"))
