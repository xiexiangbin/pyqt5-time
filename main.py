# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_main import Ui_MainWindow
from PyQt5 import QtCore, QtGui,QtWidgets

import time,threading
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.Tool|QtCore.Qt.X11BypassWindowManagerHint|QtCore.Qt.WindowStaysOnBottomHint)
        
        self.appPosMove()

        self.changTime()

    def appPosMove(self):     
        screen  =   QtWidgets.QDesktopWidget().screenGeometry() 
        size    =   self.geometry() 
        self.move((screen.width()-size.width())-100,100)   


     # 隐藏窗体突出悬浮控件
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QtWidgets.QApplication.postEvent(self, QtCore.QEvent(174))
            event.accept()
 
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()



    def changTime(self):
        def go():
            while True:
                nt=time.localtime(time.time())
                nt_time=str(nt[3]).zfill(2)+":"+str(nt[4]).zfill(2)+":"+str(nt[5]).zfill(2)
                self.label.setText(nt_time)
        threading.Thread(target=go).start()

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
