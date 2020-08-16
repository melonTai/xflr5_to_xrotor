import sys
from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# UIデザイン
from UI_py.mainwindow import Ui_MainWindow
from UI_py.aero_section_tab import Ui_section
from UI_py.error_dialog import Ui_error_dialog

# スロット
from Slot.slot_mainwindow import Slot_MainWindow
from Slot.slot_section import Slot_Section
from Slot.slot_errorDialog import Slot_ErrorDialog

# エラーメッセージダイアログ
class ErrorDialog(QtWidgets.QDialog, Ui_error_dialog, Slot_ErrorDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(ErrorDialog, self).__init__(*args, **kwargs)

# グラフ描画クラス
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = fig.add_subplot(121)
        self.axes2 = fig.add_subplot(122)
        super(MplCanvas, self).__init__(fig)
        self.plotted_line1 = None
        self.plotted_scatter1 = None
        self.plotted_scatter2 = None
        self.plotted_line2_1 = None
        self.plotted_line2_2 = None

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
        self.dcd_ddcl = 0
        self.re = 0
        self.r_R = 0

        self.setupUi(self)
        self.connectSlot()

        # グラフ描画部分
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        toolbar = NavigationToolbar(self.canvas, self)
        layout = QtWidgets.QGridLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)
        self.aero_graph.setLayout(layout)

    # シグナルをスロットに接続
    def connectSlot(self):
        self.import_aero_buttom_2.clicked.connect(self.importPolar)
        self.import_aero_buttom_2.clicked.connect(self.CalculateModel)
        self.input_aerofile_path_lineEdit.editingFinished.connect(self.getLineInputs)
        self.dcl_dalpha_lineEdit.editingFinished.connect(self.getLineInputs)
        self.dcl_dalpha_at_stall_lineEdit.editingFinished.connect(self.getLineInputs)
        self.max_cl_lineEdit.editingFinished.connect(self.getLineInputs)
        self.min_cl_lineEdit.editingFinished.connect(self.getLineInputs)
        self.cl_increment_to_stall_lineEdit.editingFinished.connect(self.getLineInputs)
        self.min_cd_lineEdit.editingFinished.connect(self.getLineInputs)
        self.cl_at_min_cd_lineEdit.editingFinished.connect(self.getLineInputs)
        self.re_lineEdit.editingFinished.connect(self.getLineInputs)
        self.dcd_ddcl_lineEdit.editingFinished.connect(self.getLineInputs)
        self.r_R_lineEdit.editingFinished.connect(self.getLineInputs)

# メインウィンドウ
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, Slot_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.connectSlot()

    # シグナルをスロットに接続
    def connectSlot(self):
        self.add_section_button.clicked.connect(lambda x : self.addSection(TabSection))
        self.delete_section_button.clicked.connect(self.delSection)
        self.build_button.clicked.connect(self.build)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
