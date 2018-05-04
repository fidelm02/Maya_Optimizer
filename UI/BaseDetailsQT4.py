# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Base_Details.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_win_details(object):
    def setupUi(self, win_details):
        win_details.setObjectName(_fromUtf8("win_details"))
        win_details.resize(400, 305)
        self.scrollArea = QtGui.QScrollArea(win_details)
        self.scrollArea.setGeometry(QtCore.QRect(30, 30, 341, 231))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 229))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.lbl_details = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_details.setGeometry(QtCore.QRect(10, 10, 301, 201))
        self.lbl_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_details.setWordWrap(True)
        self.lbl_details.setObjectName(_fromUtf8("lbl_details"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btn_ok = QtGui.QPushButton(win_details)
        self.btn_ok.setGeometry(QtCore.QRect(160, 270, 75, 23))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))

        self.retranslateUi(win_details)
        QtCore.QMetaObject.connectSlotsByName(win_details)

    def retranslateUi(self, win_details):
        win_details.setWindowTitle(_translate("win_details", "Details", None))
        self.lbl_details.setText(_translate("win_details", "TextLabel", None))
        self.btn_ok.setText(_translate("win_details", "Ok", None))

