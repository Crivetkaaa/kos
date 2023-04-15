from main_window import *
from PyQt5 import QtCore, QtGui, QtWidgets

import sys


class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.reg)
        
    def get_text(self):
        value = self.ui.lineEdit.text()
        return value
    
    def reg(self):
        value = self.get_text()
        self.create_label()
        

    def create_label(self):
        label = QtWidgets.QLabel(mywin)
        text = self.get_text()
        print('Gde')
        label.setText(text)
        label.move(100, 100)
        label.adjustSize()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())