import sys
from PyQt5 import QtWidgets, uic

from UI_py.mainwindow import Ui_MainWindow
from UI_py.aero_section_tab import Ui_section
from Slot.slot_mainwindow import Slot_MainWindow
from Slot.slot_section import Slot_Section

# タブの要素
class TabSection(QtWidgets.QTabWidget, Ui_section, Slot_Section):
    def __init__(self, *args, obj=None, **kwargs):
        super(TabSection, self).__init__(*args, **kwargs)
        self.polar_file = ''
        self.zero_lift_alpha = 0
        self.dcl_dalpha = 0
        self.dcl_dalpha_stall = 0
        self.max_cl = 0
        self.min_cl = 0
        self.cl_increment_to_stall = 0
        self.min_cd = 0
        self.cl_at_min_cd = 0
        self.re = 0

        self.setupUi(self)
        self.conectSlot()

    def connectSlot(self):
        # 各種入力値を取得
        self.import_aero_buttom_2.clicked,connect(self.importPolar)
        self.input_aerofile_path_lineEdit.editingFinished.connect(self.getLineInputs)
        self.dcl_dalpha_lineEdit.editingFinished.connect(self.getLineInputs)
        self.dcl_dalpha_at_stall_lineEdit.editingFinished.connect(self.getLineInputs)
        self.max_cl_lineEdit.editingFinished.connect(self.getLineInputs)
        self.min_cl_lineEdit.editingFinished.connect(self.getLineInputs)
        self.cl_increment_to_stall_lineEdit.editingFinished.connect(self.getLineInputs)
        self.min_cd_lineEdit.editingFinished.connect(self.getLineInputs)
        self.cl_at_min_cd_lineEdit.editingFinished.connect(self.getLineInputs)
        self.re_lineEdit.editingFinished.connect(self.getLineInputs)

        # 


# メインウィンドウ
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, Slot_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.connectSlot()

    def connectSlot(self):
        self.add_section_button.clicked.connect(lambda x : self.addSection(self.aero_sections,TabSection))
        self.delete_section_button.clicked.connect(lambda x : self.delSection(self.aero_sections))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
