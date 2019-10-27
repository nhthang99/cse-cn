# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServerGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Server.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Server)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listFriend = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listFriend.setObjectName("listFriend")
        self.verticalLayout.addWidget(self.listFriend)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 50, 451, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listMessage = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.listMessage.setObjectName("listMessage")
        self.verticalLayout_2.addWidget(self.listMessage)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 439, 621, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnStartServer = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnStartServer.setObjectName("btnStartServer")
        self.horizontalLayout_2.addWidget(self.btnStartServer)
        self.btnStopServer = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnStopServer.setObjectName("btnStopServer")
        self.btnStopServer.setDisabled(True)
        self.horizontalLayout_2.addWidget(self.btnStopServer)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(179, 10, 451, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.edtHost = QtWidgets.QLineEdit(self.frame)
        self.edtHost.setGeometry(QtCore.QRect(0, 0, 221, 31))
        self.edtHost.setAlignment(QtCore.Qt.AlignCenter)
        self.edtHost.setObjectName("edtHost")
        self.edtPort = QtWidgets.QLineEdit(self.frame)
        self.edtPort.setGeometry(QtCore.QRect(230, 0, 221, 31))
        self.edtPort.setAlignment(QtCore.Qt.AlignCenter)
        self.edtPort.setObjectName("edtPort")
        Server.setCentralWidget(self.centralwidget)

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "MainWindow"))
        self.btnStartServer.setText(_translate("Server", "Start"))
        self.btnStopServer.setText(_translate("Server", "Stop"))
        self.edtHost.setText(_translate("Server", "127.0.0.1"))
        self.edtPort.setText(_translate("Server", "8888"))
