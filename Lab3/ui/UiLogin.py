# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(193, 118)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        LoginDialog.setMaximumSize(QtCore.QSize(400, 240))
        self.gridLayout = QtWidgets.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(LoginDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(LoginDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(LoginDialog)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.LoginBtn = QtWidgets.QPushButton(LoginDialog)
        self.LoginBtn.setAutoFillBackground(True)
        self.LoginBtn.setObjectName("LoginBtn")
        self.gridLayout.addWidget(self.LoginBtn, 2, 1, 1, 1)
        self.username = QtWidgets.QLineEdit(LoginDialog)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "登陆"))
        self.label_4.setText(_translate("LoginDialog", "密码："))
        self.label_3.setText(_translate("LoginDialog", "账号："))
        self.LoginBtn.setText(_translate("LoginDialog", "登陆"))
