# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Base_Details_v003.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
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
        win_details.resize(743, 708)
        self.verticalLayout_ = QtWidgets.QVBoxLayout(win_details)
        self.verticalLayout_.setObjectName("verticalLayout")
        self.lbl_title = QtWidgets.QLabel(win_details)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_title.setFont(font)
        self.lbl_title.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_title.setObjectName("lbl_title")
        #self.verticalLayout_.addWidget(self.lbl_title)
        self.frame_2 = QtWidgets.QFrame(win_details)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setEnabled(True)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 686, 824))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_details = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lbl_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_details.setWordWrap(True)
        self.lbl_details.setObjectName("lbl_details")
        self.horizontalLayout_4.addWidget(self.lbl_details)
        #self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        #self.horizontalLayout_3.addWidget(self.scrollArea_2)
        #self.verticalLayout_.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(win_details)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(self.frame)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_2.addWidget(self.btn_ok)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        #self.verticalLayout_.addWidget(self.frame)

        self.retranslateUi(win_details)
        QtCore.QMetaObject.connectSlotsByName(win_details)

    def retranslateUi(self, win_details):
        win_details.setWindowTitle(_translate("win_details", "Details", None))
        self.lbl_title.setText(_translate("win_details", "  Details", None))
        self.lbl_details.setText(_translate("win_details", "Test", None))
        self.btn_ok.setText(_translate("win_details", "Okis", None))

