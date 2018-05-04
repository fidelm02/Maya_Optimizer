# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Base_Details_v003.ui'
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
        win_details.resize(743, 708)
        self.verticalLayout = QtGui.QVBoxLayout(win_details)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_title = QtGui.QLabel(win_details)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_title.setFont(font)
        self.lbl_title.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.verticalLayout.addWidget(self.lbl_title)
        self.frame_2 = QtGui.QFrame(win_details)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.scrollArea_2 = QtGui.QScrollArea(self.frame_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setEnabled(True)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 686, 824))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lbl_details = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lbl_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_details.setWordWrap(True)
        self.lbl_details.setObjectName(_fromUtf8("lbl_details"))
        self.horizontalLayout_4.addWidget(self.lbl_details)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.addWidget(self.scrollArea_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtGui.QFrame(win_details)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_ok = QtGui.QPushButton(self.frame)
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.horizontalLayout_2.addWidget(self.btn_ok)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(win_details)
        QtCore.QMetaObject.connectSlotsByName(win_details)

    def retranslateUi(self, win_details):
        win_details.setWindowTitle(_translate("win_details", "Details", None))
        self.lbl_title.setText(_translate("win_details", "  Details", None))
        self.lbl_details.setText(_translate("win_details", "\n"
"        self.verticalLayout_2.addWidget(self.scrollArea)\n"
"\n"
"        self.frame_2 = QtWidgets.QFrame(self.frame_0)\n"
"\n"
"        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)\n"
"\n"
"        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)\n"
"\n"
"        self.frame_2.setObjectName(\"frame_2\")\n"
"\n"
"        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)\n"
"\n"
"        self.horizontalLayout_2.setObjectName(\"horizontalLayout_2\")\n"
"\n"
"        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)\n"
"\n"
"        self.horizontalLayout_2.addItem(spacerItem2)\n"
"\n"
"        self.btn_ok = QtWidgets.QPushButton(self.frame_2)\n"
"\n"
"        self.btn_ok.setObjectName(\"btn_ok\")\n"
"\n"
"        self.horizontalLayout_2.addWidget(self.btn_ok)\n"
"\n"
"        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)\n"
"\n"
"        self.horizontalLayout_2.addItem(spacerItem3)\n"
"\n"
"        self.verticalLayout_2.addWidget(self.frame_2)\n"
"\n"
"        self.horizontalLayout_3.addWidget(self.frame_0)\n"
"\n"
"\n"
"\n"
"        self.retranslateUi(win_details)\n"
"\n"
"        QtCore.QMetaObject.connectSlotsByName(win_details)\n"
"\n"
"\n"
"\n"
"    def retranslateUi(self, win_details):\n"
"\n"
"        win_details.setWindowTitle(_translate(\"win_details\", \"Details\", None))\n"
"\n"
"        self.lbl_title.setText(_translate(\"win_details\", \"  Details\", None))\n"
"\n"
"        self.lbl_details.setText(_translate(\"win_details\", \"TextLabel\", None))\n"
"\n"
"        self.btn_ok.setText(_translate(\"win_details\", \"Ok\", None))\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"class MyApplication(QtWidgets.QMainWindow, Ui_win_details):\n"
"    def __init__(self, parent=None):\n"
"        super(MyApplication, self).__init__(parent)\n"
"        self.setupUi(self)\n"
"        \n"
"window_ = MyApplication()\n"
"window_.show()", None))
        self.btn_ok.setText(_translate("win_details", "Ok", None))

