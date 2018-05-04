"""
Master script.

This script.
"""
import sys
from Modules.Qt import QtCore, QtGui, QtWidgets
from General.Maya_Optimizer.UI import BaseInterface, BaseStatus, Base_Details_v004Qt5, InterfaceFunctions
from General.Maya_Optimizer.Core.Steps import Modeling, Animation, Rigging, Shading, VFX, Lighting

modulos = [BaseInterface,BaseStatus,Base_Details_v004Qt5, InterfaceFunctions, 
    Modeling, Animation, Rigging, Shading, VFX, Lighting]
[reload (xi) for xi in modulos]


class MyApplication(QtWidgets.QMainWindow, BaseInterface.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)


class StatusApplication(QtWidgets.QMainWindow, BaseStatus.Ui_form_status):

    def __init__(self, parent=None):
        super(StatusApplication, self).__init__(parent)
        self.setupUi(self)


class DetailWindow(QtWidgets.QMainWindow, Base_Details_v004Qt5.Ui_win_details):

    def __init__(self, parent=None):
        super(DetailWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ != "__main__":
    mdl_ins = Modeling.ModelingControls()
    anim_ins = Animation.AnimationControls()
    rig_ins = Rigging.RiggingControls()
    shd_ins = Shading.ShadingControls()
    vfx_ins = VFX.VfxControls()
    lgt_ins = Lighting.LightingControls()

    CtrlObjects = {
        "Modelling" : mdl_ins,
        "Animation" : anim_ins,
        "Rigging" : rig_ins,
        "Shading" : shd_ins,
        "Vfx" : vfx_ins,
        "Lighting" : lgt_ins
        }

    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)

    app.aboutToQuit.connect(app.quit)

    window = MyApplication()
    status_window = StatusApplication()
    details_window = DetailWindow()

    window.setWindowFlags(
        window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

    details_window.setWindowFlags(
        details_window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

    status_window.setWindowFlags(
        status_window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

    interfaceMacho = InterfaceFunctions.InterfaceActions(
        window_interface=window, status_window=status_window,
        detail_window=details_window, ctrlObjects = CtrlObjects)

    window.show()

    try:
        sys.exit(app.exec_())
    except:
        ""
