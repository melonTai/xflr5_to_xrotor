from PyQt5 import QtGui, QtWidgets, QtCore

class Slot_MainWindow(object):
    # タブにページ追加
    def addSection(self,Section):
        section = Section()
        self.aero_sections.addTab(section,str(self.aero_sections.count() + 1))

    # タブからページ削除
    def delSection(self):
        self.aero_sections.removeTab(self.aero_sections.currentIndex())

    # xrotorのaeroファイル作成
    def build(self):
        count = self.aero_sections.count()
        output_aero_data = ''
        for i in range(count):
            section = self.aero_sections.widget(i)
            output_aero_data += "\n"
            output_aero_data += " Section "+str(i+1)+"   r/R = "+str(section.r_R)+"\n"
            output_aero_data += " ====================================================================\n"
            output_aero_data += " Zero-lift alpha (deg):  {zero_lift_alpha:<2.2f}        Minimum Cd           : {min_Cd:<2.4f}\n".format(zero_lift_alpha = section.zero_lift_alpha,min_Cd = section.min_cd)
            output_aero_data += " d(Cl)/d(alpha)       :  {:<2.3f}".format(section.dcl_dalpha)+"        Cl at minimum Cd     : {:<2.3f}\n".format(section.cl_at_min_cd)
            output_aero_data += " d(Cl)/d(alpha)@stall :  {:<2.3f}".format(section.dcl_dalpha_stall)+"        d(Cd)/d(Cl**2)       : {:<2.4f}".format(section.dcd_ddcl)+"\n"
            output_aero_data += " Maximum Cl           :  {:<2.2f}".format(section.max_cl)+"         Reference Re number  :  {:<6.1f}\n".format(section.re)
            output_aero_data += " Minimum Cl           : {cl_min:<2.2f}         Re scaling exponent  : -0.4000\n".format(cl_min=section.min_cl)
            output_aero_data += " Cl increment to stall: {:<2.3f}".format(section.cl_increment_to_stall)+"         Cm                   : -0.100\n"
            output_aero_data += "                                      Mcrit                :  0.800\n"
            output_aero_data += " ====================================================================\n"

        fname = QtWidgets.QFileDialog.getSaveFileName(self, "Save File","/home")[0];
        if fname != '':
            with open(fname, mode='w') as f:
                f.write(output_aero_data)
