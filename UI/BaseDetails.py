# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Base_Details.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from Modules.Qt import QtCore, QtGui, QtWidgets

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_win_details(object):
    def setupUi(self, win_details):
        win_details.setObjectName("win_details")
        win_details.resize(400, 305)
        self.scrollArea = QtWidgets.QScrollArea(win_details)
        self.scrollArea.setGeometry(QtCore.QRect(30, 30, 341, 231))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 229))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lbl_details = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_details.setGeometry(QtCore.QRect(10, 10, 301, 201))
        self.lbl_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_details.setWordWrap(True)
        self.lbl_details.setObjectName("lbl_details")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btn_ok = QtWidgets.QPushButton(win_details)
        self.btn_ok.setGeometry(QtCore.QRect(160, 270, 75, 23))
        self.btn_ok.setObjectName("btn_ok")

        self.retranslateUi(win_details)
        QtCore.QMetaObject.connectSlotsByName(win_details)

    def retranslateUi(self, win_details):
        win_details.setWindowTitle(_translate("win_details", "Details", None))
        self.lbl_details.setText(_translate("win_details", "TextLabel", None))
        self.btn_ok.setText(_translate("win_details", "Ok", None))

