from PyQt5 import QtGui, QtWidgets, QtCore
import math
import numpy as np
from Slot.slot_errorDialog import Slot_ErrorDialog
from UI_py.error_dialog import Ui_error_dialog

# エラーメッセージダイアログ
class ErrorDialog(QtWidgets.QDialog, Ui_error_dialog, Slot_ErrorDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(ErrorDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

# TabWidgetのスロット設定
class Slot_Section(object):
    # 入力文字列がfloat型か確認
    def is_float(self,value):
        try:
            float(value)
            return True
        except:
            return False

    # グラフアップデート
    def update_plot(self):
        if self.canvas.plotted_line1 is not None:
            self.canvas.plotted_line1.remove()
        if self.canvas.plotted_line2_1 is not None:
            self.canvas.plotted_line2_1.remove()
        if self.canvas.plotted_line2_2 is not None:
            self.canvas.plotted_line2_2.remove()
        if self.canvas.plotted_scatter1 is not None:
            self.canvas.plotted_scatter1.remove()
        if self.canvas.plotted_scatter2 is not None:
            self.canvas.plotted_scatter2.remove()

        self.cl_model = np.linspace(self.min_cl,self.max_cl,100)
        self.cd_model = [self.min_cd + self.dcd_ddcl*(self.cl_at_min_cd - y)**2 for y in self.cl_model]
        self.canvas.plotted_line1, = self.canvas.axes1.plot(self.cd_model, self.cl_model, 'r')
        self.canvas.plotted_scatter1 = self.canvas.axes1.scatter(self.cd_list, self.cl_list,c = 'b')

        self.alpha_model = [x for x in np.linspace(self.alpha_list[0],self.alpha_list[-1],100,endpoint=True) if self.min_cl <= self.dcl_dalpha*(x-self.zero_lift_alpha*math.pi/180) and self.dcl_dalpha*(x-self.zero_lift_alpha*math.pi/180) <= self.max_cl]
        self.cl_model2 = [self.dcl_dalpha*(x-self.zero_lift_alpha*math.pi/180) for x in self.alpha_model]
        self.cl_model_stall = np.linspace(self.max_cl, self.max_cl+self.cl_increment_to_stall, 50)
        self.alpha_model_stall = [(y - self.max_cl)/self.dcl_dalpha_stall + self.alpha_model[-1] for y in self.cl_model_stall]
        self.canvas.plotted_line2_1, = self.canvas.axes2.plot(self.alpha_model, self.cl_model2, 'r')
        self.canvas.plotted_line2_2, = self.canvas.axes2.plot(self.alpha_model_stall, self.cl_model_stall, 'g')
        self.canvas.plotted_scatter2 = self.canvas.axes2.scatter(self.alpha_list, self.cl_list, c = 'b')

        # Trigger the canvas to update and redraw.
        self.canvas.draw()

    # 翼型特性自動近似
    def CalculateModel(self):
        def getCloseIndex(t,s):
            delta = [abs(i-s) for i in t]
            return delta.index(min(delta))

        #ポーラーファイルからレイノルズ数を読み取る
        try:
            file = open(self.polar_file, "r")
            Re = file.readlines()[7]
            Re = float(Re[29:33])*1e6
            self.re = math.floor(Re)
            file.close()

            aero = np.loadtxt(fname=self.polar_file,skiprows=11).T#解析ファイル読み込み
            check_posi = [i for i in range(len(aero[2]) - 1) if(aero[2][i + 1] - aero[2][i]) / (aero[1][i + 1] - aero[1][i]) >= 0.05 and aero[1][i]>0]
            cl_list = [aero[1][i] for i in range(len(aero[2]) - 1) if abs((aero[2][i + 1] - aero[2][i]) / (aero[1][i + 1] - aero[1][i])) < 0.05]
            cd_list = [aero[2][i] for i in range(len(aero[2]) - 1) if abs((aero[2][i + 1] - aero[2][i]) / (aero[1][i + 1] - aero[1][i])) < 0.05]
            self.cl_list = [aero[1][i] for i in range(len(aero[2]) - 1)]
            self.cd_list = [aero[2][i] for i in range(len(aero[2]) - 1)]
            self.alpha_list = [aero[0][i]*math.pi/180 for i in range(len(aero[2]) - 1)]
            alpha_list = [aero[0][i] for i in range(len(aero[2]) - 1) if abs((aero[2][i + 1] - aero[2][i]) / (aero[1][i + 1] - aero[1][i])) < 0.05]
            alpha_list_posi = [aero[0][i] for i in check_posi]
            cl_list_posi = [aero[1][i] for i in check_posi]
            res2 = np.polyfit(cl_list,cd_list, 2)#最小二乗法による二次関数近似
            self.cl_at_min_cd = -res2[1]/(2*res2[0])
            cl_index = getCloseIndex(cl_list,self.cl_at_min_cd)#設計揚力係数ともっとも近い解析地点を探す
            cl_delta_deg = (cl_list[cl_index+1]-cl_list[cl_index])/(alpha_list[cl_index+1]-alpha_list[cl_index])#設計揚力係数付近の揚力係数の傾きを求める
            self.dcl_dalpha = float(cl_delta_deg*180/math.pi)#揚力係数傾きの単位をcl/degからcl/radに変更
            alpha = alpha_list[cl_index]#設計揚力係数に近い迎角を得る
            self.zero_lift_alpha = float(alpha - cl_list[cl_index]/cl_delta_deg)#設計揚力係数を通るようにpolarグラフを近似した時のx切片
            self.min_cd = -res2[1]**2/(4*res2[0])+res2[2]#設計揚力係数
            self.max_cl = cl_list[-1]#最大揚力係数
            self.min_cl = cl_list[0]#最小揚力係数
            self.dcl_dalpha_stall = (max(cl_list_posi)-cl_list[-1])/(alpha_list_posi[cl_list_posi.index(max(cl_list_posi))]-alpha_list[-1])*180/math.pi
            self.cl_increment_to_stall = max(cl_list_posi)-cl_list[-1]
            self.dcd_ddcl = res2[0]
            self.setAllLineInputs()
            self.update_plot()
        except Exception as e:
            dialog = ErrorDialog()
            dialog.error_message.setText('error:{}'.format(e))
            dialog.show()
            dialog.exec_()

    # ポーラーファイルインポート
    def importPolar(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open xflr5 polar file','/home')[0]
        self.input_aerofile_path_lineEdit.setText(fname)
        self.polar_file = fname

    # 各種入力値を取得
    def getLineInputs(self):
        line = self.sender()
        if line is self.input_aerofile_path_lineEdit:
            self.polar_file = line.text()
        elif line is self.zero_lift_alpha_lineEdit:
            if self.is_float(line.text()):
                self.zero_lift_alpha = float(line.text())
            else:
                line.setText('Error')
        elif line is self.dcl_dalpha_lineEdit:
            if self.is_float(line.text()):
                self.dcl_dalpha = float(line.text())
            else:
                line.setText('Error')
        elif line is self.dcl_dalpha_at_stall_lineEdit:
            if self.is_float(line.text()):
                self.dcl_dalpha_stall = float(line.text())
            else:
                line.setText('Error')
        elif line is self.max_cl_lineEdit:
            if self.is_float(line.text()):
                self.max_cl = float(line.text())
            else:
                line.setText('Error')
        elif line is self.min_cl_lineEdit:
            if self.is_float(line.text()):
                self.min_cl = float(line.text())
            else:
                line.setText('Error')
        elif line is self.cl_increment_to_stall_lineEdit:
            if self.is_float(line.text()):
                self.cl_increment_to_stall = float(line.text())
            else:
                line.setText('Error')
        elif line is self.min_cd_lineEdit:
            if self.is_float(line.text()):
                self.min_cd = float(line.text())
            else:
                line.setText('Error')
        elif line is self.cl_at_min_cd_lineEdit:
            if self.is_float(line.text()):
                self.cl_at_min_cd = float(line.text())
            else:
                line.setText('Error')
        elif line is self.re_lineEdit:
            if self.is_float(line.text()):
                self.re = float(line.text())
            else:
                line.setText('Error')
        elif line is self.r_R_lineEdit:
            if self.is_float(line.text()):
                self.r_R = float(line.text())
            else:
                line.setText('Error')
        elif line is self.dcd_ddcl_lineEdit:
            if self.is_float(line.text()):
                self.dcd_ddcl = float(line.text())
                print("dcd_ddcl")
            else:
                line.setText('Error')
        self.update_plot()

    # polarファイルインポート時に自動入力
    def setAllLineInputs(self):
        self.input_aerofile_path_lineEdit.setText(self.polar_file)
        self.zero_lift_alpha_lineEdit.setText('{:.4f}'.format(self.zero_lift_alpha))
        self.dcl_dalpha_lineEdit.setText('{:.4f}'.format(self.dcl_dalpha))
        self.dcl_dalpha_at_stall_lineEdit.setText('{:.4f}'.format(self.dcl_dalpha_stall))
        self.max_cl_lineEdit.setText('{:.4f}'.format(self.max_cl))
        self.min_cl_lineEdit.setText('{:.4f}'.format(self.min_cl))
        self.cl_increment_to_stall_lineEdit.setText('{:.4f}'.format(self.cl_increment_to_stall))
        self.min_cd_lineEdit.setText('{:.4f}'.format(self.min_cd))
        self.cl_at_min_cd_lineEdit.setText('{:.4f}'.format(self.cl_at_min_cd))
        self.re_lineEdit.setText('{:.4f}'.format(self.re))
        self.r_R_lineEdit.setText('{:.4f}'.format(self.r_R))
        self.dcd_ddcl_lineEdit.setText('{:.4f}'.format(self.dcd_ddcl))
