#!/usr/bin/env python
import sys

from PyQt5.QtWidgets import QApplication , QWidget,QMainWindow
from project_ui import *
from PyQt5 import sip
if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_Post()
    # ui = Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

