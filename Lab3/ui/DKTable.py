# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dktable.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(1074, 440)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.table = QtWidgets.QTableWidget(LoginDialog)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridLayout_4.addWidget(self.table, 1, 0, 1, 1)
        self.tablepay = QtWidgets.QTableWidget(LoginDialog)
        self.tablepay.setMinimumSize(QtCore.QSize(0, 300))
        self.tablepay.setObjectName("tablepay")
        self.tablepay.setColumnCount(0)
        self.tablepay.setRowCount(0)
        self.gridLayout_4.addWidget(self.tablepay, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(LoginDialog)
        font = QtGui.QFont()
        font.setFamily("方正清刻本悦宋简体")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(LoginDialog)
        font = QtGui.QFont()
        font.setFamily("方正清刻本悦宋简体")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.line = QtWidgets.QFrame(LoginDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout.addLayout(self.verticalLayout, 1, 3, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.npayM = QtWidgets.QCheckBox(LoginDialog)
        self.npayM.setObjectName("npayM")
        self.gridLayout_3.addWidget(self.npayM, 5, 7, 1, 1)
        self.Id = QtWidgets.QLineEdit(LoginDialog)
        self.Id.setInputMask("")
        self.Id.setText("")
        self.Id.setObjectName("Id")
        self.gridLayout_3.addWidget(self.Id, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(LoginDialog)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(LoginDialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 5, 1, 1, 1)
        self.namountM = QtWidgets.QCheckBox(LoginDialog)
        self.namountM.setObjectName("namountM")
        self.gridLayout_3.addWidget(self.namountM, 5, 5, 1, 1)
        self.Owner = QtWidgets.QLineEdit(LoginDialog)
        self.Owner.setObjectName("Owner")
        self.gridLayout_3.addWidget(self.Owner, 1, 3, 1, 1)
        self.amountM = QtWidgets.QDoubleSpinBox(LoginDialog)
        self.amountM.setMaximum(999999999999.0)
        self.amountM.setObjectName("amountM")
        self.gridLayout_3.addWidget(self.amountM, 1, 5, 1, 1)
        self.payM = QtWidgets.QDoubleSpinBox(LoginDialog)
        self.payM.setMaximum(999999999999.0)
        self.payM.setObjectName("payM")
        self.gridLayout_3.addWidget(self.payM, 1, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(LoginDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 5, 2, 1, 1)
        self.status = QtWidgets.QComboBox(LoginDialog)
        self.status.setObjectName("status")
        self.status.addItem("")
        self.status.addItem("")
        self.status.addItem("")
        self.gridLayout_3.addWidget(self.status, 1, 4, 1, 1)
        self.Name = QtWidgets.QLineEdit(LoginDialog)
        self.Name.setText("")
        self.Name.setObjectName("Name")
        self.gridLayout_3.addWidget(self.Name, 1, 2, 1, 1)
        self.amountL = QtWidgets.QDoubleSpinBox(LoginDialog)
        self.amountL.setMaximum(999999999999.0)
        self.amountL.setObjectName("amountL")
        self.gridLayout_3.addWidget(self.amountL, 1, 6, 1, 1)
        self.namountL = QtWidgets.QCheckBox(LoginDialog)
        self.namountL.setObjectName("namountL")
        self.gridLayout_3.addWidget(self.namountL, 5, 6, 1, 1)
        self.npayL = QtWidgets.QCheckBox(LoginDialog)
        self.npayL.setObjectName("npayL")
        self.gridLayout_3.addWidget(self.npayL, 5, 8, 1, 1)
        self.payL = QtWidgets.QDoubleSpinBox(LoginDialog)
        self.payL.setMaximum(999999999999.0)
        self.payL.setObjectName("payL")
        self.gridLayout_3.addWidget(self.payL, 1, 8, 1, 1)
        self.nstatus = QtWidgets.QCheckBox(LoginDialog)
        self.nstatus.setObjectName("nstatus")
        self.gridLayout_3.addWidget(self.nstatus, 5, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 8, 3, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.flushButton = QtWidgets.QPushButton(LoginDialog)
        self.flushButton.setObjectName("flushButton")
        self.verticalLayout_2.addWidget(self.flushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.AddBtn = QtWidgets.QPushButton(LoginDialog)
        self.AddBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.AddBtn.setObjectName("AddBtn")
        self.verticalLayout_2.addWidget(self.AddBtn)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SearchBtn = QtWidgets.QPushButton(LoginDialog)
        self.SearchBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.SearchBtn.setObjectName("SearchBtn")
        self.verticalLayout_3.addWidget(self.SearchBtn)
        self.gridLayout.addLayout(self.verticalLayout_3, 8, 1, 1, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "贷款管理"))
        self.label_14.setText(_translate("LoginDialog", "贷款发放"))
        self.label_13.setText(_translate("LoginDialog", "贷款信息"))
        self.title.setText(_translate("LoginDialog", "贷款管理"))
        self.npayM.setText(_translate("LoginDialog", "最高已发放额度"))
        self.label_15.setText(_translate("LoginDialog", "持有者"))
        self.label.setText(_translate("LoginDialog", "贷款号"))
        self.namountM.setText(_translate("LoginDialog", "最高总额度"))
        self.label_2.setText(_translate("LoginDialog", "支行名"))
        self.status.setItemText(0, _translate("LoginDialog", "未发放"))
        self.status.setItemText(1, _translate("LoginDialog", "发放中"))
        self.status.setItemText(2, _translate("LoginDialog", "已发放"))
        self.namountL.setText(_translate("LoginDialog", "最低总额度"))
        self.npayL.setText(_translate("LoginDialog", "最低已发放额度"))
        self.nstatus.setText(_translate("LoginDialog", "贷款状态"))
        self.flushButton.setText(_translate("LoginDialog", "刷新"))
        self.AddBtn.setText(_translate("LoginDialog", "添加"))
        self.SearchBtn.setText(_translate("LoginDialog", "查询"))