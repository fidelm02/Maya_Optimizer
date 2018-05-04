# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Base_Details_v004.ui'
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
        win_details.resize(543, 605)
        self.centralwidget = QtGui.QWidget(win_details)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_title = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_title.setFont(font)
        self.lbl_title.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.verticalLayout.addWidget(self.lbl_title)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 523, 489))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lbl_details = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_details.setWordWrap(True)
        self.lbl_details.setObjectName(_fromUtf8("lbl_details"))
        self.verticalLayout_2.addWidget(self.lbl_details)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_ok = QtGui.QPushButton(self.centralwidget)
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.horizontalLayout.addWidget(self.btn_ok)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        win_details.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(win_details)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        win_details.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(win_details)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        win_details.setStatusBar(self.statusbar)

        self.retranslateUi(win_details)
        QtCore.QMetaObject.connectSlotsByName(win_details)

    def retranslateUi(self, win_details):
        win_details.setWindowTitle(_translate("win_details", "MainWindow", None))
        self.lbl_title.setText(_translate("win_details", "  Details", None))
        self.lbl_details.setText(_translate("win_details", "Test02", None))
        self.btn_ok.setText(_translate("win_details", "Ok", None))

