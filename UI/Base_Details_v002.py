# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Base_Details_v002.ui'
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
        win_details.setWindowModality(QtCore.Qt.WindowModal)
        win_details.resize(518, 583)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(win_details)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame_0 = QtGui.QFrame(win_details)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_0.sizePolicy().hasHeightForWidth())
        self.frame_0.setSizePolicy(sizePolicy)
        self.frame_0.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_0.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_0.setObjectName(_fromUtf8("frame_0"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lbl_title = QtGui.QLabel(self.frame_0)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_title.setFont(font)
        self.lbl_title.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.verticalLayout_2.addWidget(self.lbl_title)
        self.scrollArea = QtGui.QScrollArea(self.frame_0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 478, 470))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_details = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_details.setWordWrap(True)
        self.lbl_details.setObjectName(_fromUtf8("lbl_details"))
        self.horizontalLayout.addWidget(self.lbl_details)
        spacerItem1 = QtGui.QSpacerItem(4, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.frame_2 = QtGui.QFrame(self.frame_0)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_ok = QtGui.QPushButton(self.frame_2)
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.horizontalLayout_2.addWidget(self.btn_ok)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_3.addWidget(self.frame_0)

        self.retranslateUi(win_details)
        QtCore.QMetaObject.connectSlotsByName(win_details)

    def retranslateUi(self, win_details):
        win_details.setWindowTitle(_translate("win_details", "Details", None))
        self.lbl_title.setText(_translate("win_details", "  Details", None))
        self.lbl_details.setText(_translate("win_details", "TextLabel", None))
        self.btn_ok.setText(_translate("win_details", "Ok", None))

