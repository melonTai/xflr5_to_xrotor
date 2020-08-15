from PyQt5 import QtGui, QtWidgets, QtCore
import math
import numpy as np

class Slot_Section(object):
    def is_float(self,value):
        try:
            float(value)
            return True
        except:
            return False
    def update_plot(self):
        self.ydata_model = np.linspace(self.min_cl,self.max_cl,100)
        self.xdata_model = [self.min_cd + self.dcd_ddcl*(self.cl_at_min_cd - y)**2 for y in self.ydata_model]
        self.ydata_polar = self.cl_list
        self.xdata_polar = self.cd_list
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata_model, self.ydata_model, 'r')
        self.canvas.axes.scatter(self.xdata_polar, self.ydata_polar)
        self.canvas.axes.autoscale()
        # Trigger the canvas to update and redraw.
        self.canvas.draw()

    def CalculateModel(self):
        def getCloseIndex(t,s):
            delta = [abs(i-s) for i in t]
            print(delta)
            return delta.index(min(delta))

        #ポーラーファイルからレイノルズ数を読み取る
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

    def importPolar(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open xflr5 polar file','/home')
        self.input_aerofile_path_lineEdit.setText(fname[0])
        self.polar_file = fname[0]

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
            else:
                line.setText('Error')
        self.update_plot()

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
