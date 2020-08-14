from PyQt5 import QtGui, QtWidgets, QtCore

class Slot_Section(object):
    def is_float(self,value):
        try:
            float(self.value)
            return True
        except:
            return False

    def setLineInputs(self):
        pass

    def importPolar(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open xflr5 polar file','/home')
        self.input_aerofile_path_lineEdit.setText(fname)

    def getLineInputs(self):
        line = self.sender()
        if line is self.input_aerofile_path_lineEdit:
            self.polar_file = line.text()
        elif line is self.zero_lift_alpha_lineEdit):
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
                self.dcl_dalpha_at_stall = float(line.text())
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
