# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Base_Status.ui'
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

class Ui_form_status(object):
    def setupUi(self, form_status):
        form_status.setObjectName(_fromUtf8("form_status"))
        form_status.resize(302, 148)
        self.lbl_elements = QtGui.QLabel(form_status)
        self.lbl_elements.setGeometry(QtCore.QRect(0, 100, 301, 21))
        self.lbl_elements.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_elements.setObjectName(_fromUtf8("lbl_elements"))
        self.lbl_status = QtGui.QLabel(form_status)
        self.lbl_status.setGeometry(QtCore.QRect(0, 40, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_status.setFont(font)
        self.lbl_status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.progressBar_01 = QtGui.QProgressBar(form_status)
        self.progressBar_01.setEnabled(True)
        self.progressBar_01.setGeometry(QtCore.QRect(70, 80, 171, 16))
        self.progressBar_01.setProperty("value", 0)
        self.progressBar_01.setInvertedAppearance(False)
        self.progressBar_01.setObjectName(_fromUtf8("progressBar_01"))
        self.lbl_step = QtGui.QLabel(form_status)
        self.lbl_step.setGeometry(QtCore.QRect(0, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_step.setFont(font)
        self.lbl_step.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_step.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_step.setObjectName(_fromUtf8("lbl_step"))

        self.retranslateUi(form_status)
        QtCore.QMetaObject.connectSlotsByName(form_status)

    def retranslateUi(self, form_status):
        form_status.setWindowTitle(_translate("form_status", "Form", None))
        self.lbl_elements.setText(_translate("form_status", "0/0", None))
        self.lbl_status.setText(_translate("form_status", "I", None))
        self.lbl_step.setText(_translate("form_status", "I", None))

