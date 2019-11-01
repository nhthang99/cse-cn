# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 560)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 60, 171, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 171, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lvFriend = QtWidgets.QListView(self.verticalLayoutWidget)
        self.lvFriend.setObjectName("lvFriend")
        self.lvFriend.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.verticalLayout.addWidget(self.lvFriend)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(190, 10, 581, 541))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 581, 501))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        # self.lvBodyMessage = QtWidgets.QListView(self.frame_3)
        self.lvBodyMessage = QtWidgets.QListWidget(self.frame_3)
        self.lvBodyMessage.setGeometry(0, 0, 581, 501)
        self.lvBodyMessage.setObjectName("lvBodyMessage")
        self.lvBodyMessage.raise_()
        self.lvBodyMessage.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lvBodyMessage.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.verticalLayoutWidget.raise_()
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(0, 510, 581, 31))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.btnSend = QtWidgets.QPushButton(self.frame_4)
        self.btnSend.setGeometry(QtCore.QRect(480, 0, 101, 31))
        self.btnSend.setObjectName("btnSend")
        self.etxtMessage = QtWidgets.QLineEdit(self.frame_4)
        self.etxtMessage.setGeometry(QtCore.QRect(0, 0, 471, 31))
        self.etxtMessage.setObjectName("etxtMessage")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.frame_5.setAutoFillBackground(True)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_5)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 171, 41))
        self.graphicsView.setObjectName("graphicsView")
        self.txtUsername = QtWidgets.QLabel(self.frame_5)
        self.txtUsername.setGeometry(QtCore.QRect(40, 10, 121, 20))
        self.txtUsername.setObjectName("txtUsername")
        self.ivAvatar = QtWidgets.QLabel(self.frame_5)
        self.ivAvatar.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.ivAvatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ivAvatar.setLineWidth(0)
        self.ivAvatar.setText("")
        self.ivAvatar.setPixmap(QtGui.QPixmap("../imgs/default_avatar.png"))
        self.ivAvatar.setScaledContents(True)
        self.ivAvatar.setObjectName("ivAvatar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat App"))
        self.btnSend.setText(_translate("MainWindow", "Send"))
        self.txtUsername.setText(_translate("MainWindow", "Unknown"))
