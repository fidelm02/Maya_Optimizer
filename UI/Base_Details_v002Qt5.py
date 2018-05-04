# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'Base_Details_v002.ui'

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

        win_details.setWindowModality(QtCore.Qt.WindowModal)

        win_details.resize(518, 583)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(win_details)

        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.frame_0 = QtWidgets.QFrame(win_details)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        sizePolicy.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.frame_0.sizePolicy().hasHeightForWidth())

        self.frame_0.setSizePolicy(sizePolicy)

        self.frame_0.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.frame_0.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_0.setObjectName("frame_0")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_0)

        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.lbl_title = QtWidgets.QLabel(self.frame_0)

        font = QtGui.QFont()

        font.setPointSize(11)

        font.setBold(False)

        font.setWeight(50)

        self.lbl_title.setFont(font)

        self.lbl_title.setTextFormat(QtCore.Qt.AutoText)

        self.lbl_title.setObjectName("lbl_title")

        self.verticalLayout_2.addWidget(self.lbl_title)

        self.scrollArea = QtWidgets.QScrollArea(self.frame_0)

        self.scrollArea.setWidgetResizable(True)

        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()

        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 478, 470))

        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)

        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem)

        self.lbl_details = QtWidgets.QLabel(self.scrollAreaWidgetContents)

        self.lbl_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        self.lbl_details.setWordWrap(True)

        self.lbl_details.setObjectName("lbl_details")

        self.horizontalLayout.addWidget(self.lbl_details)

        spacerItem1 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.frame_2 = QtWidgets.QFrame(self.frame_0)

        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_2.setObjectName("frame_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)

        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(spacerItem2)

        self.btn_ok = QtWidgets.QPushButton(self.frame_2)

        self.btn_ok.setObjectName("btn_ok")

        self.horizontalLayout_2.addWidget(self.btn_ok)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

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



