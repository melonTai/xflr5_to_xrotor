# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_error_dialog(object):
    def setupUi(self, error_dialog):
        error_dialog.setObjectName("error_dialog")
        error_dialog.resize(240, 320)
        self.gridLayout = QtWidgets.QGridLayout(error_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.error_message = QtWidgets.QTextBrowser(error_dialog)
        self.error_message.setObjectName("error_message")
        self.gridLayout.addWidget(self.error_message, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(error_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(error_dialog)
        self.buttonBox.accepted.connect(error_dialog.accept)
        self.buttonBox.rejected.connect(error_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(error_dialog)

    def retranslateUi(self, error_dialog):
        _translate = QtCore.QCoreApplication.translate
        error_dialog.setWindowTitle(_translate("error_dialog", "error message"))

