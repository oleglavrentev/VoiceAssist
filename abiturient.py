# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abiturient.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Abiturient(object):
    def setupUi(self, Abiturient):
        Abiturient.setObjectName("Abiturient")
        Abiturient.resize(628, 321)
        Abiturient.setStyleSheet("background-color:rgb(85, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(Abiturient)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 491, 41))
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
        self.listWidget.setGeometry(QtCore.QRect(70, 60, 491, 221))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        Abiturient.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Abiturient)
        self.statusbar.setObjectName("statusbar")
        Abiturient.setStatusBar(self.statusbar)

        self.retranslateUi(Abiturient)
        QtCore.QMetaObject.connectSlotsByName(Abiturient)

    def retranslateUi(self, Abiturient):
        _translate = QtCore.QCoreApplication.translate
        Abiturient.setWindowTitle(_translate("Abiturient", "MainWindow"))
        self.label.setText(_translate("Abiturient", "Информация для абитуриентов"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Abiturient", "1. Какие были проходные баллы прошлого года?"))
        item = self.listWidget.item(1)
        item.setText(_translate("Abiturient", "2. Предоставь лицензию университета"))
        item = self.listWidget.item(2)
        item.setText(_translate("Abiturient", "3. Предоставь аккредитацию университета"))
        item = self.listWidget.item(3)
        item.setText(_translate("Abiturient", "4. Сколько стоит обучение?"))
        item = self.listWidget.item(4)
        item.setText(_translate("Abiturient", "5. Покажи количество бюджетных мест"))
        item = self.listWidget.item(5)
        item.setText(_translate("Abiturient", "6. Покажи количество платных мест"))
        item = self.listWidget.item(6)
        item.setText(_translate("Abiturient", "7. Покажи сроки приема документов"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
