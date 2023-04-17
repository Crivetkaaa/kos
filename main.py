from main_window import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.values = []
        self.all_labels = [self.ui.label_3, self.ui.label_4, self.ui.label_5, 
                           self.ui.label_6, self.ui.label_7, self.ui.label_8, 
                           self.ui.label_9, self.ui.label_10, self.ui.label_11, self.ui.label_12]

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.ui.pushButton.clicked.connect(self.get_text)
        
    def get_text(self):
        value = self.ui.lineEdit.text()
        try:
            int_value = int(value)
            self.values.append(int_value)
            self.update_labels()
                
        except:
            print('sorry')
            msg = QMessageBox()
            msg.setWindowTitle("TypeError")
            msg.setText("Введите число.")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        
    def update_labels(self):
        if len(self.values) < 10:
            for i in range(0, len(self.values)):
                self.all_labels[i].setText(str(self.values[i]))
        else:
            for i in range(1, 10):
                self.all_labels[-i].setText(str(self.values[-i]))
        self.update_file()

    def update_file(self):
        with open('info.txt', 'a') as file:
            file.write(f"{len(self.values)}, {self.values[-1]}\n")
       

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())