# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aero_section_tab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_section(object):
    def setupUi(self, section):
        section.setObjectName("section")
        section.resize(645, 338)
        self.gridLayout = QtWidgets.QGridLayout(section)
        self.gridLayout.setObjectName("gridLayout")
        self.aero_graph_wrap_2 = QtWidgets.QGroupBox(section)
        self.aero_graph_wrap_2.setObjectName("aero_graph_wrap_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.aero_graph_wrap_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.aero_graph = QtWidgets.QWidget(self.aero_graph_wrap_2)
        self.aero_graph.setObjectName("aero_graph")
        self.gridLayout_4.addWidget(self.aero_graph, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.aero_graph_wrap_2, 0, 0, 1, 1)
        self.input_param_2 = QtWidgets.QGroupBox(section)
        self.input_param_2.setObjectName("input_param_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.input_param_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.import_aero_buttom_2 = QtWidgets.QPushButton(self.input_param_2)
        self.import_aero_buttom_2.setObjectName("import_aero_buttom_2")
        self.horizontalLayout_3.addWidget(self.import_aero_buttom_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.input_aerofile_path_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.input_aerofile_path_lineEdit.setObjectName("input_aerofile_path_lineEdit")
        self.horizontalLayout_3.addWidget(self.input_aerofile_path_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.zero_lift_alpha_label_2 = QtWidgets.QLabel(self.input_param_2)
        self.zero_lift_alpha_label_2.setObjectName("zero_lift_alpha_label_2")
        self.horizontalLayout_2.addWidget(self.zero_lift_alpha_label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.zero_lift_alpha_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.zero_lift_alpha_lineEdit.setObjectName("zero_lift_alpha_lineEdit")
        self.horizontalLayout_2.addWidget(self.zero_lift_alpha_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dcl_dalpha_label = QtWidgets.QLabel(self.input_param_2)
        self.dcl_dalpha_label.setObjectName("dcl_dalpha_label")
        self.horizontalLayout_4.addWidget(self.dcl_dalpha_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.dcl_dalpha_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.dcl_dalpha_lineEdit.setObjectName("dcl_dalpha_lineEdit")
        self.horizontalLayout_4.addWidget(self.dcl_dalpha_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dcl_dalpha_at_stall_label = QtWidgets.QLabel(self.input_param_2)
        self.dcl_dalpha_at_stall_label.setObjectName("dcl_dalpha_at_stall_label")
        self.horizontalLayout_5.addWidget(self.dcl_dalpha_at_stall_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.dcl_dalpha_at_stall_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.dcl_dalpha_at_stall_lineEdit.setObjectName("dcl_dalpha_at_stall_lineEdit")
        self.horizontalLayout_5.addWidget(self.dcl_dalpha_at_stall_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.max_cl_label = QtWidgets.QLabel(self.input_param_2)
        self.max_cl_label.setObjectName("max_cl_label")
        self.horizontalLayout_8.addWidget(self.max_cl_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.max_cl_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.max_cl_lineEdit.setObjectName("max_cl_lineEdit")
        self.horizontalLayout_8.addWidget(self.max_cl_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.min_cl_label = QtWidgets.QLabel(self.input_param_2)
        self.min_cl_label.setObjectName("min_cl_label")
        self.horizontalLayout_10.addWidget(self.min_cl_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.min_cl_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.min_cl_lineEdit.setObjectName("min_cl_lineEdit")
        self.horizontalLayout_10.addWidget(self.min_cl_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.cl_increment_to_stall_label = QtWidgets.QLabel(self.input_param_2)
        self.cl_increment_to_stall_label.setObjectName("cl_increment_to_stall_label")
        self.horizontalLayout_11.addWidget(self.cl_increment_to_stall_label)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.cl_increment_to_stall_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.cl_increment_to_stall_lineEdit.setObjectName("cl_increment_to_stall_lineEdit")
        self.horizontalLayout_11.addWidget(self.cl_increment_to_stall_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.min_cd_label = QtWidgets.QLabel(self.input_param_2)
        self.min_cd_label.setObjectName("min_cd_label")
        self.horizontalLayout_12.addWidget(self.min_cd_label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.min_cd_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.min_cd_lineEdit.setObjectName("min_cd_lineEdit")
        self.horizontalLayout_12.addWidget(self.min_cd_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.cl_at_min_cd_label = QtWidgets.QLabel(self.input_param_2)
        self.cl_at_min_cd_label.setObjectName("cl_at_min_cd_label")
        self.horizontalLayout_13.addWidget(self.cl_at_min_cd_label)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.cl_at_min_cd_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.cl_at_min_cd_lineEdit.setObjectName("cl_at_min_cd_lineEdit")
        self.horizontalLayout_13.addWidget(self.cl_at_min_cd_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.re_label = QtWidgets.QLabel(self.input_param_2)
        self.re_label.setObjectName("re_label")
        self.horizontalLayout_14.addWidget(self.re_label)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem9)
        self.re_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.re_lineEdit.setObjectName("re_lineEdit")
        self.horizontalLayout_14.addWidget(self.re_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.r_R_label = QtWidgets.QLabel(self.input_param_2)
        self.r_R_label.setObjectName("r_R_label")
        self.horizontalLayout.addWidget(self.r_R_label)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.r_R_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.r_R_lineEdit.setObjectName("r_R_lineEdit")
        self.horizontalLayout.addWidget(self.r_R_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.dcd_ddcl_label = QtWidgets.QLabel(self.input_param_2)
        self.dcd_ddcl_label.setObjectName("dcd_ddcl_label")
        self.horizontalLayout_6.addWidget(self.dcd_ddcl_label)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.dcd_ddcl_lineEdit = QtWidgets.QLineEdit(self.input_param_2)
        self.dcd_ddcl_lineEdit.setObjectName("dcd_ddcl_lineEdit")
        self.horizontalLayout_6.addWidget(self.dcd_ddcl_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.input_param_2, 1, 0, 1, 1)

        self.retranslateUi(section)
        QtCore.QMetaObject.connectSlotsByName(section)

    def retranslateUi(self, section):
        _translate = QtCore.QCoreApplication.translate
        section.setWindowTitle(_translate("section", "Form"))
        self.aero_graph_wrap_2.setTitle(_translate("section", "aero_graph"))
        self.input_param_2.setTitle(_translate("section", "input_param"))
        self.import_aero_buttom_2.setText(_translate("section", "import_polar"))
        self.zero_lift_alpha_label_2.setText(_translate("section", "Zelo-lift-alpha(deg)"))
        self.dcl_dalpha_label.setText(_translate("section", " d(Cl)/d(alpha)"))
        self.dcl_dalpha_at_stall_label.setText(_translate("section", "d(Cl)/d(alpha)@stall"))
        self.max_cl_label.setText(_translate("section", "Maximum Cl"))
        self.min_cl_label.setText(_translate("section", "Minimum Cl"))
        self.cl_increment_to_stall_label.setText(_translate("section", "Cl increment to stall"))
        self.min_cd_label.setText(_translate("section", "Minimum Cd"))
        self.cl_at_min_cd_label.setText(_translate("section", "Cl at minimum Cd"))
        self.re_label.setText(_translate("section", "Reference Re number"))
        self.r_R_label.setText(_translate("section", "r/R"))
        self.dcd_ddcl_label.setText(_translate("section", " d(Cd)/d(Cl**2)"))

