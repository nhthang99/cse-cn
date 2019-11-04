# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 166)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(210, 130, 91, 29))
        self.btnLogin.setObjectName("btnLogin")
        self.edtUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.edtUsername.setGeometry(QtCore.QRect(90, 10, 211, 31))
        self.edtUsername.setInputMethodHints(QtCore.Qt.ImhLowercaseOnly)
        self.edtUsername.setObjectName("edtUsername")
        self.lbUsername = QtWidgets.QLabel(self.centralwidget)
        self.lbUsername.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.lbUsername.setAutoFillBackground(True)
        self.lbUsername.setObjectName("lbUsername")
        self.edtHost = QtWidgets.QLineEdit(self.centralwidget)
        self.edtHost.setGeometry(QtCore.QRect(90, 50, 211, 31))
        self.edtHost.setObjectName("edtHost")
        self.lbPort = QtWidgets.QLabel(self.centralwidget)
        self.lbPort.setGeometry(QtCore.QRect(10, 90, 71, 31))
        self.lbPort.setAutoFillBackground(True)
        self.lbPort.setObjectName("lbPort")
        self.lbHost = QtWidgets.QLabel(self.centralwidget)
        self.lbHost.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.lbHost.setAutoFillBackground(True)
        self.lbHost.setObjectName("lbHost")
        self.edtPort = QtWidgets.QLineEdit(self.centralwidget)
        self.edtPort.setGeometry(QtCore.QRect(90, 90, 211, 31))
        self.edtPort.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.edtPort.setObjectName("edtPort")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.edtUsername.setText(_translate("MainWindow", "nhthang"))
        self.lbUsername.setText(_translate("MainWindow", "Username:"))
        self.edtHost.setText(_translate("MainWindow", "127.0.0.1"))
        self.lbPort.setText(_translate("MainWindow", "Port:"))
        self.lbHost.setText(_translate("MainWindow", "Host:"))
        self.edtPort.setText(_translate("MainWindow", "8888"))
