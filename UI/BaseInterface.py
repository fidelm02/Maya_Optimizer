# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Base_Interface.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 493)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs_master = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs_master.setGeometry(QtCore.QRect(150, 40, 491, 351))
        self.tabs_master.setObjectName("tabs_master")
        self.tab_modeling = QtWidgets.QWidget()
        self.tab_modeling.setObjectName("tab_modeling")
        self.mdl_grp_scan = QtWidgets.QGroupBox(self.tab_modeling)
        self.mdl_grp_scan.setGeometry(QtCore.QRect(20, 20, 191, 281))
        self.mdl_grp_scan.setObjectName("mdl_grp_scan")
        self.layoutWidget = QtWidgets.QWidget(self.mdl_grp_scan)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 20, 141, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chk_mdl_transformation = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_mdl_transformation.setObjectName("chk_mdl_transformation")
        self.verticalLayout.addWidget(self.chk_mdl_transformation)
        self.chk_mdl_history = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_mdl_history.setObjectName("chk_mdl_history")
        self.verticalLayout.addWidget(self.chk_mdl_history)
        self.chk_mdl_hierarchy = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_mdl_hierarchy.setAutoFillBackground(False)
        self.chk_mdl_hierarchy.setObjectName("chk_mdl_hierarchy")
        self.verticalLayout.addWidget(self.chk_mdl_hierarchy)
        self.chk_mdl_names = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_mdl_names.setObjectName("chk_mdl_names")
        self.verticalLayout.addWidget(self.chk_mdl_names)
        self.chk_mdl_materials = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_mdl_materials.setObjectName("chk_mdl_materials")
        self.verticalLayout.addWidget(self.chk_mdl_materials)
        self.chk_mdl_uvSets = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_mdl_uvSets.setObjectName("chk_mdl_uvSets")
        self.verticalLayout.addWidget(self.chk_mdl_uvSets)
        self.chk_mdl_center = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_mdl_center.setObjectName("chk_mdl_center")
        self.verticalLayout.addWidget(self.chk_mdl_center)
        self.chk_mdl_unknown = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_mdl_unknown.setAutoFillBackground(False)
        self.chk_mdl_unknown.setObjectName("chk_mdl_unknown")
        self.verticalLayout.addWidget(self.chk_mdl_unknown)
        self.chk_mdl_invalidNames = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_mdl_invalidNames.setObjectName("chk_mdl_invalidNames")
        self.verticalLayout.addWidget(self.chk_mdl_invalidNames)
        self.mdl_grp_fix = QtWidgets.QGroupBox(self.tab_modeling)
        self.mdl_grp_fix.setGeometry(QtCore.QRect(240, 20, 221, 171))
        self.mdl_grp_fix.setObjectName("mdl_grp_fix")
        self.scrollArea = QtWidgets.QScrollArea(self.mdl_grp_fix)
        self.scrollArea.setGeometry(QtCore.QRect(0, 20, 221, 151))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 219, 149))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lbl_mdl_fix = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_mdl_fix.setGeometry(QtCore.QRect(10, 10, 181, 131))
        self.lbl_mdl_fix.setObjectName("lbl_mdl_fix")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.mdl_grp_reference = QtWidgets.QGroupBox(self.tab_modeling)
        self.mdl_grp_reference.setGeometry(QtCore.QRect(240, 210, 221, 81))
        self.mdl_grp_reference.setObjectName("mdl_grp_reference")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.mdl_grp_reference)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 20, 221, 61))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 219, 59))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.lbl_mdl_reference = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lbl_mdl_reference.setGeometry(QtCore.QRect(10, 10, 181, 41))
        self.lbl_mdl_reference.setObjectName("lbl_mdl_reference")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabs_master.addTab(self.tab_modeling, "")
        self.tab_rig = QtWidgets.QWidget()
        self.tab_rig.setObjectName("tab_rig")
        self.rig_grp_Scan = QtWidgets.QGroupBox(self.tab_rig)
        self.rig_grp_Scan.setGeometry(QtCore.QRect(20, 20, 191, 271))
        self.rig_grp_Scan.setObjectName("rig_grp_Scan")
        self.frame = QtWidgets.QFrame(self.rig_grp_Scan)
        self.frame.setGeometry(QtCore.QRect(10, 20, 171, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chk_rig_reference = QtWidgets.QCheckBox(self.frame)
        self.chk_rig_reference.setObjectName("chk_rig_reference")
        self.verticalLayout_2.addWidget(self.chk_rig_reference)
        self.chk_rig_unknown = QtWidgets.QCheckBox(self.frame)
        self.chk_rig_unknown.setAutoFillBackground(False)
        self.chk_rig_unknown.setObjectName("chk_rig_unknown")
        self.verticalLayout_2.addWidget(self.chk_rig_unknown)
        self.chk_rig_invalidNames = QtWidgets.QCheckBox(self.frame)
        self.chk_rig_invalidNames.setObjectName("chk_rig_invalidNames")
        self.verticalLayout_2.addWidget(self.chk_rig_invalidNames)
        self.mdl_grp_reference_2 = QtWidgets.QGroupBox(self.tab_rig)
        self.mdl_grp_reference_2.setGeometry(QtCore.QRect(240, 210, 221, 81))

        self.mdl_grp_reference_2.setObjectName("mdl_grp_reference_2")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.mdl_grp_reference_2)
        self.scrollArea_4.setGeometry(QtCore.QRect(0, 20, 221, 61))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")

        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()

        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 219, 59))

        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")

        self.lbl_rig_reference = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)

        self.lbl_rig_reference.setGeometry(QtCore.QRect(10, 10, 181, 41))

        self.lbl_rig_reference.setObjectName("lbl_rig_reference")

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.mdl_grp_fix_2 = QtWidgets.QGroupBox(self.tab_rig)

        self.mdl_grp_fix_2.setGeometry(QtCore.QRect(240, 20, 221, 171))

        self.mdl_grp_fix_2.setObjectName("mdl_grp_fix_2")

        self.scrollArea_3 = QtWidgets.QScrollArea(self.mdl_grp_fix_2)

        self.scrollArea_3.setGeometry(QtCore.QRect(0, 20, 221, 151))

        self.scrollArea_3.setWidgetResizable(True)

        self.scrollArea_3.setObjectName("scrollArea_3")

        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()

        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 219, 149))

        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")

        self.lbl_rig_fix = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)

        self.lbl_rig_fix.setGeometry(QtCore.QRect(10, 10, 181, 131))

        self.lbl_rig_fix.setObjectName("lbl_rig_fix")

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.tabs_master.addTab(self.tab_rig, "")

        self.tab_animation = QtWidgets.QWidget()

        self.tab_animation.setObjectName("tab_animation")

        self.anim_grp_scan = QtWidgets.QGroupBox(self.tab_animation)

        self.anim_grp_scan.setGeometry(QtCore.QRect(20, 20, 191, 271))

        self.anim_grp_scan.setObjectName("anim_grp_scan")

        self.frame_2 = QtWidgets.QFrame(self.anim_grp_scan)

        self.frame_2.setGeometry(QtCore.QRect(10, 20, 171, 241))

        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_2.setObjectName("frame_2")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)

        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.chk_anim_atom = QtWidgets.QCheckBox(self.frame_2)

        self.chk_anim_atom.setObjectName("chk_anim_atom")

        self.verticalLayout_3.addWidget(self.chk_anim_atom)

        self.chk_anim_reference = QtWidgets.QCheckBox(self.frame_2)

        self.chk_anim_reference.setObjectName("chk_anim_reference")

        self.verticalLayout_3.addWidget(self.chk_anim_reference)

        self.chk_anim_unknown = QtWidgets.QCheckBox(self.frame_2)

        self.chk_anim_unknown.setAutoFillBackground(False)

        self.chk_anim_unknown.setObjectName("chk_anim_unknown")

        self.verticalLayout_3.addWidget(self.chk_anim_unknown)

        self.chk_anim_invalidNames = QtWidgets.QCheckBox(self.frame_2)

        self.chk_anim_invalidNames.setObjectName("chk_anim_invalidNames")

        self.verticalLayout_3.addWidget(self.chk_anim_invalidNames)

        self.mdl_grp_reference_3 = QtWidgets.QGroupBox(self.tab_animation)

        self.mdl_grp_reference_3.setGeometry(QtCore.QRect(240, 210, 221, 81))

        self.mdl_grp_reference_3.setObjectName("mdl_grp_reference_3")

        self.scrollArea_6 = QtWidgets.QScrollArea(self.mdl_grp_reference_3)

        self.scrollArea_6.setGeometry(QtCore.QRect(0, 20, 221, 61))

        self.scrollArea_6.setWidgetResizable(True)

        self.scrollArea_6.setObjectName("scrollArea_6")

        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()

        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 219, 59))

        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")

        self.lbl_anim_reference = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)

        self.lbl_anim_reference.setGeometry(QtCore.QRect(10, 10, 181, 41))

        self.lbl_anim_reference.setObjectName("lbl_anim_reference")

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.mdl_grp_fix_3 = QtWidgets.QGroupBox(self.tab_animation)

        self.mdl_grp_fix_3.setGeometry(QtCore.QRect(240, 20, 221, 171))

        self.mdl_grp_fix_3.setObjectName("mdl_grp_fix_3")

        self.scrollArea_5 = QtWidgets.QScrollArea(self.mdl_grp_fix_3)

        self.scrollArea_5.setGeometry(QtCore.QRect(0, 20, 221, 151))

        self.scrollArea_5.setWidgetResizable(True)

        self.scrollArea_5.setObjectName("scrollArea_5")

        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()

        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 219, 149))

        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")

        self.lbl_anim_fix = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)

        self.lbl_anim_fix.setGeometry(QtCore.QRect(10, 10, 181, 131))

        self.lbl_anim_fix.setObjectName("lbl_anim_fix")

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.tabs_master.addTab(self.tab_animation, "")

        self.tab_lighting = QtWidgets.QWidget()

        self.tab_lighting.setObjectName("tab_lighting")

        self.grp_Scan_5 = QtWidgets.QGroupBox(self.tab_lighting)

        self.grp_Scan_5.setGeometry(QtCore.QRect(20, 20, 191, 271))

        self.grp_Scan_5.setObjectName("grp_Scan_5")

        self.frame_3 = QtWidgets.QFrame(self.grp_Scan_5)

        self.frame_3.setGeometry(QtCore.QRect(10, 20, 171, 241))

        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_3.setObjectName("frame_3")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)

        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.chk_light_external = QtWidgets.QCheckBox(self.frame_3)

        self.chk_light_external.setObjectName("chk_light_external")

        self.verticalLayout_4.addWidget(self.chk_light_external)

        self.chk_light_reference = QtWidgets.QCheckBox(self.frame_3)

        self.chk_light_reference.setObjectName("chk_light_reference")

        self.verticalLayout_4.addWidget(self.chk_light_reference)

        self.chk_light_unknown = QtWidgets.QCheckBox(self.frame_3)

        self.chk_light_unknown.setAutoFillBackground(False)

        self.chk_light_unknown.setObjectName("chk_light_unknown")

        self.verticalLayout_4.addWidget(self.chk_light_unknown)

        self.chk_light_invalidNames = QtWidgets.QCheckBox(self.frame_3)

        self.chk_light_invalidNames.setObjectName("chk_light_invalidNames")

        self.verticalLayout_4.addWidget(self.chk_light_invalidNames)

        self.mdl_grp_reference_4 = QtWidgets.QGroupBox(self.tab_lighting)

        self.mdl_grp_reference_4.setGeometry(QtCore.QRect(240, 210, 221, 81))

        self.mdl_grp_reference_4.setObjectName("mdl_grp_reference_4")

        self.scrollArea_8 = QtWidgets.QScrollArea(self.mdl_grp_reference_4)

        self.scrollArea_8.setGeometry(QtCore.QRect(0, 20, 221, 61))

        self.scrollArea_8.setWidgetResizable(True)

        self.scrollArea_8.setObjectName("scrollArea_8")

        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()

        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 219, 59))

        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")

        self.lbl_light_reference = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)

        self.lbl_light_reference.setGeometry(QtCore.QRect(10, 10, 181, 41))

        self.lbl_light_reference.setObjectName("lbl_light_reference")

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.mdl_grp_fix_4 = QtWidgets.QGroupBox(self.tab_lighting)

        self.mdl_grp_fix_4.setGeometry(QtCore.QRect(240, 20, 221, 171))

        self.mdl_grp_fix_4.setObjectName("mdl_grp_fix_4")

        self.scrollArea_7 = QtWidgets.QScrollArea(self.mdl_grp_fix_4)

        self.scrollArea_7.setGeometry(QtCore.QRect(0, 20, 221, 151))

        self.scrollArea_7.setWidgetResizable(True)

        self.scrollArea_7.setObjectName("scrollArea_7")

        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()

        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 219, 149))

        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")

        self.lbl_light_fix = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)

        self.lbl_light_fix.setGeometry(QtCore.QRect(10, 10, 181, 131))

        self.lbl_light_fix.setObjectName("lbl_light_fix")

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.tabs_master.addTab(self.tab_lighting, "")

        self.tab_shading = QtWidgets.QWidget()

        self.tab_shading.setObjectName("tab_shading")

        self.grp_Scan_4 = QtWidgets.QGroupBox(self.tab_shading)

        self.grp_Scan_4.setGeometry(QtCore.QRect(20, 20, 191, 271))

        self.grp_Scan_4.setObjectName("grp_Scan_4")

        self.frame_4 = QtWidgets.QFrame(self.grp_Scan_4)

        self.frame_4.setGeometry(QtCore.QRect(10, 20, 171, 251))

        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_4.setObjectName("frame_4")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)

        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.chk_shd_repeated = QtWidgets.QCheckBox(self.frame_4)

        self.chk_shd_repeated.setObjectName("chk_shd_repeated")

        self.verticalLayout_5.addWidget(self.chk_shd_repeated)

        self.chk_shd_external = QtWidgets.QCheckBox(self.frame_4)

        self.chk_shd_external.setObjectName("chk_shd_external")

        self.verticalLayout_5.addWidget(self.chk_shd_external)

        self.chk_shd_reference = QtWidgets.QCheckBox(self.frame_4)

        self.chk_shd_reference.setObjectName("chk_shd_reference")

        self.verticalLayout_5.addWidget(self.chk_shd_reference)

        self.chk_shd_textures = QtWidgets.QCheckBox(self.frame_4)

        self.chk_shd_textures.setObjectName("chk_shd_textures")

        self.verticalLayout_5.addWidget(self.chk_shd_textures)

        self.chk_shd_unknown = QtWidgets.QCheckBox(self.frame_4)

        self.chk_shd_unknown.setAutoFillBackground(False)

        self.chk_shd_unknown.setObjectName("chk_shd_unknown")

        self.verticalLayout_5.addWidget(self.chk_shd_unknown)

        self.chk_shd_invalidNames = QtWidgets.QCheckBox(self.frame_4)

        self.chk_shd_invalidNames.setObjectName("chk_shd_invalidNames")

        self.verticalLayout_5.addWidget(self.chk_shd_invalidNames)

        self.mdl_grp_reference_5 = QtWidgets.QGroupBox(self.tab_shading)

        self.mdl_grp_reference_5.setGeometry(QtCore.QRect(240, 210, 221, 81))

        self.mdl_grp_reference_5.setObjectName("mdl_grp_reference_5")

        self.scrollArea_10 = QtWidgets.QScrollArea(self.mdl_grp_reference_5)

        self.scrollArea_10.setGeometry(QtCore.QRect(0, 20, 221, 61))

        self.scrollArea_10.setWidgetResizable(True)

        self.scrollArea_10.setObjectName("scrollArea_10")

        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()

        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 219, 59))

        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")

        self.lbl_shd_reference = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)

        self.lbl_shd_reference.setGeometry(QtCore.QRect(10, 10, 181, 41))

        self.lbl_shd_reference.setObjectName("lbl_shd_reference")

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)

        self.mdl_grp_fix_5 = QtWidgets.QGroupBox(self.tab_shading)

        self.mdl_grp_fix_5.setGeometry(QtCore.QRect(240, 20, 221, 171))

        self.mdl_grp_fix_5.setObjectName("mdl_grp_fix_5")

        self.scrollArea_9 = QtWidgets.QScrollArea(self.mdl_grp_fix_5)

        self.scrollArea_9.setGeometry(QtCore.QRect(0, 20, 221, 151))

        self.scrollArea_9.setWidgetResizable(True)

        self.scrollArea_9.setObjectName("scrollArea_9")

        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()

        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 219, 149))

        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")

        self.lbl_shd_fix = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)

        self.lbl_shd_fix.setGeometry(QtCore.QRect(10, 10, 181, 131))

        self.lbl_shd_fix.setObjectName("lbl_shd_fix")

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)

        self.tabs_master.addTab(self.tab_shading, "")

        self.tab_vfx = QtWidgets.QWidget()

        self.tab_vfx.setObjectName("tab_vfx")

        self.grp_Scan_6 = QtWidgets.QGroupBox(self.tab_vfx)

        self.grp_Scan_6.setGeometry(QtCore.QRect(20, 20, 191, 271))

        self.grp_Scan_6.setObjectName("grp_Scan_6")

        self.frame_5 = QtWidgets.QFrame(self.grp_Scan_6)

        self.frame_5.setGeometry(QtCore.QRect(10, 20, 131, 241))

        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_5.setObjectName("frame_5")

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)

        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.chk_vfx_reference = QtWidgets.QCheckBox(self.frame_5)

        self.chk_vfx_reference.setObjectName("chk_vfx_reference")

        self.verticalLayout_6.addWidget(self.chk_vfx_reference)

        self.chk_vfx_unknown = QtWidgets.QCheckBox(self.frame_5)

        self.chk_vfx_unknown.setAutoFillBackground(False)

        self.chk_vfx_unknown.setObjectName("chk_vfx_unknown")

        self.verticalLayout_6.addWidget(self.chk_vfx_unknown)

        self.chk_vfx_invalidNames = QtWidgets.QCheckBox(self.frame_5)

        self.chk_vfx_invalidNames.setObjectName("chk_vfx_invalidNames")

        self.verticalLayout_6.addWidget(self.chk_vfx_invalidNames)

        self.mdl_grp_reference_6 = QtWidgets.QGroupBox(self.tab_vfx)

        self.mdl_grp_reference_6.setGeometry(QtCore.QRect(240, 210, 221, 81))

        self.mdl_grp_reference_6.setObjectName("mdl_grp_reference_6")

        self.scrollArea_12 = QtWidgets.QScrollArea(self.mdl_grp_reference_6)

        self.scrollArea_12.setGeometry(QtCore.QRect(0, 20, 221, 61))

        self.scrollArea_12.setWidgetResizable(True)

        self.scrollArea_12.setObjectName("scrollArea_12")

        self.scrollAreaWidgetContents_12 = QtWidgets.QWidget()

        self.scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 219, 59))

        self.scrollAreaWidgetContents_12.setObjectName("scrollAreaWidgetContents_12")

        self.lbl_vfx_reference = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)

        self.lbl_vfx_reference.setGeometry(QtCore.QRect(10, 10, 181, 41))

        self.lbl_vfx_reference.setObjectName("lbl_vfx_reference")

        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)

        self.mdl_grp_fix_6 = QtWidgets.QGroupBox(self.tab_vfx)

        self.mdl_grp_fix_6.setGeometry(QtCore.QRect(240, 20, 221, 171))

        self.mdl_grp_fix_6.setObjectName("mdl_grp_fix_6")

        self.scrollArea_11 = QtWidgets.QScrollArea(self.mdl_grp_fix_6)

        self.scrollArea_11.setGeometry(QtCore.QRect(0, 20, 221, 151))

        self.scrollArea_11.setWidgetResizable(True)

        self.scrollArea_11.setObjectName("scrollArea_11")

        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()

        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 219, 149))

        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")

        self.lbl_vfx_fix = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)

        self.lbl_vfx_fix.setGeometry(QtCore.QRect(10, 10, 181, 131))

        self.lbl_vfx_fix.setObjectName("lbl_vfx_fix")

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)

        self.tabs_master.addTab(self.tab_vfx, "")

        self.btn_Check = QtWidgets.QPushButton(self.centralwidget)

        self.btn_Check.setGeometry(QtCore.QRect(30, 150, 75, 23))

        self.btn_Check.setObjectName("btn_Check")

        self.btn_Ok = QtWidgets.QPushButton(self.centralwidget)

        self.btn_Ok.setGeometry(QtCore.QRect(30, 200, 75, 23))

        self.btn_Ok.setObjectName("btn_Ok")

        self.btn_details = QtWidgets.QPushButton(self.centralwidget)

        self.btn_details.setGeometry(QtCore.QRect(560, 420, 75, 23))

        self.btn_details.setObjectName("btn_details")

        self.chk_box_checkall = QtWidgets.QPushButton(self.centralwidget)

        self.chk_box_checkall.setGeometry(QtCore.QRect(190, 420, 75, 23))

        self.chk_box_checkall.setObjectName("chk_box_checkall")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 21))

        self.menubar.setObjectName("menubar")

        self.menuAbout = QtWidgets.QMenu(self.menubar)

        self.menuAbout.setObjectName("menuAbout")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())



        self.retranslateUi(MainWindow)

        self.tabs_master.setCurrentIndex(5)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "Maya scenes debuger", None))

        self.mdl_grp_scan.setTitle(_translate("MainWindow", "Scan", None))

        self.chk_mdl_transformation.setText(_translate("MainWindow", "Transformations", None))

        self.chk_mdl_history.setText(_translate("MainWindow", "History", None))

        self.chk_mdl_hierarchy.setText(_translate("MainWindow", "Hierarchy", None))

        self.chk_mdl_names.setText(_translate("MainWindow", "Names", None))

        self.chk_mdl_materials.setText(_translate("MainWindow", "Materials", None))

        self.chk_mdl_uvSets.setText(_translate("MainWindow", "UV Sets", None))

        self.chk_mdl_center.setText(_translate("MainWindow", "Center", None))

        self.chk_mdl_unknown.setText(_translate("MainWindow", "Unknown Nodes", None))

        self.chk_mdl_invalidNames.setText(_translate("MainWindow", "Invalid Names", None))

        self.mdl_grp_fix.setTitle(_translate("MainWindow", "Fix", None))

        self.lbl_mdl_fix.setText(_translate("MainWindow", "Modeling Elements with problems.", None))

        self.mdl_grp_reference.setTitle(_translate("MainWindow", "Reference problem", None))

        self.lbl_mdl_reference.setText(_translate("MainWindow", "References with problems.", None))

        self.tabs_master.setTabText(self.tabs_master.indexOf(self.tab_modeling), _translate("MainWindow", "Modeling", None))

        self.rig_grp_Scan.setTitle(_translate("MainWindow", "Scan", None))

        self.chk_rig_reference.setText(_translate("MainWindow", "Non referenced", None))

        self.chk_rig_unknown.setText(_translate("MainWindow", "Unknown Nodes", None))

        self.chk_rig_invalidNames.setText(_translate("MainWindow", "Invalid Names", None))

        self.mdl_grp_reference_2.setTitle(_translate("MainWindow", "Reference problem", None))

        self.lbl_rig_reference.setText(_translate("MainWindow", "References with problems.", None))

        self.mdl_grp_fix_2.setTitle(_translate("MainWindow", "Fix", None))

        self.lbl_rig_fix.setText(_translate("MainWindow", "Rigging Elements with problems.", None))

        self.tabs_master.setTabText(self.tabs_master.indexOf(self.tab_rig), _translate("MainWindow", "Rig", None))

        self.anim_grp_scan.setTitle(_translate("MainWindow", "Scan", None))

        self.chk_anim_atom.setText(_translate("MainWindow", "Atom Nodes", None))

        self.chk_anim_reference.setText(_translate("MainWindow", "Non referenced", None))

        self.chk_anim_unknown.setText(_translate("MainWindow", "Unknown Nodes", None))

        self.chk_anim_invalidNames.setText(_translate("MainWindow", "Invalid Names", None))

        self.mdl_grp_reference_3.setTitle(_translate("MainWindow", "Reference problem", None))

        self.lbl_anim_reference.setText(_translate("MainWindow", "References with problems.", None))

        self.mdl_grp_fix_3.setTitle(_translate("MainWindow", "Fix", None))

        self.lbl_anim_fix.setText(_translate("MainWindow", "Animation Elements with problems.", None))

        self.tabs_master.setTabText(self.tabs_master.indexOf(self.tab_animation), _translate("MainWindow", "Animation", None))

        self.grp_Scan_5.setTitle(_translate("MainWindow", "Scan", None))

        self.chk_light_external.setText(_translate("MainWindow", "External lights", None))

        self.chk_light_reference.setText(_translate("MainWindow", "Non referenced", None))

        self.chk_light_unknown.setText(_translate("MainWindow", "Unknown Nodes", None))

        self.chk_light_invalidNames.setText(_translate("MainWindow", "Invalid Names", None))

        self.mdl_grp_reference_4.setTitle(_translate("MainWindow", "Reference problem", None))

        self.lbl_light_reference.setText(_translate("MainWindow", "References with problems.", None))

        self.mdl_grp_fix_4.setTitle(_translate("MainWindow", "Fix", None))

        self.lbl_light_fix.setText(_translate("MainWindow", "Lighting Elements with problems.", None))

        self.tabs_master.setTabText(self.tabs_master.indexOf(self.tab_lighting), _translate("MainWindow", "Lighting", None))

        self.grp_Scan_4.setTitle(_translate("MainWindow", "Scan", None))

        self.chk_shd_repeated.setText(_translate("MainWindow", "Repeated shaders", None))

        self.chk_shd_external.setText(_translate("MainWindow", "External shaders", None))

        self.chk_shd_reference.setText(_translate("MainWindow", "Non referenced", None))

        self.chk_shd_textures.setText(_translate("MainWindow", "Local Textures", None))

        self.chk_shd_unknown.setText(_translate("MainWindow", "Unknown Nodes", None))

        self.chk_shd_invalidNames.setText(_translate("MainWindow", "Invalid Names", None))

        self.mdl_grp_reference_5.setTitle(_translate("MainWindow", "Reference problem", None))

        self.lbl_shd_reference.setText(_translate("MainWindow", "References with problems.", None))

        self.mdl_grp_fix_5.setTitle(_translate("MainWindow", "Fix", None))

        self.lbl_shd_fix.setText(_translate("MainWindow", "Shading Elements with problems.", None))

        self.tabs_master.setTabText(self.tabs_master.indexOf(self.tab_shading), _translate("MainWindow", "Shading", None))

        self.grp_Scan_6.setTitle(_translate("MainWindow", "Scan", None))

        self.chk_vfx_reference.setText(_translate("MainWindow", "Non referenced", None))

        self.chk_vfx_unknown.setText(_translate("MainWindow", "Unknown Nodes", None))

        self.chk_vfx_invalidNames.setText(_translate("MainWindow", "Invalid Names", None))

        self.mdl_grp_reference_6.setTitle(_translate("MainWindow", "Reference problem", None))

        self.lbl_vfx_reference.setText(_translate("MainWindow", "References with problems.", None))

        self.mdl_grp_fix_6.setTitle(_translate("MainWindow", "Fix", None))

        self.lbl_vfx_fix.setText(_translate("MainWindow", "VFX Elements with problems.", None))

        self.tabs_master.setTabText(self.tabs_master.indexOf(self.tab_vfx), _translate("MainWindow", "VFX", None))

        self.btn_Check.setText(_translate("MainWindow", "Check", None))

        self.btn_Ok.setText(_translate("MainWindow", "Fix", None))

        self.btn_details.setText(_translate("MainWindow", "Details", None))

        self.chk_box_checkall.setText(_translate("MainWindow", "Check all", None))

        self.menuAbout.setTitle(_translate("MainWindow", "About", None))



