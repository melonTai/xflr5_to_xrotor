from PyQt5 import QtGui, QtWidgets, QtCore

class Slot_MainWindow(object):
    def relabel(self, TabWidget):
    def addSection(self,TabWidget,Section):
        section = Section()
        TabWidget.addTab(section,str(TabWidget.count() + 1))
    def delSection(self,TabWidgets):
        TabWidgets.removeTab(TabWidgets.currentIndex())
