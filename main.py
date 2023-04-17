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
        from test import xs, ys, color
        if len(self.values) >= 2:
            if self.values[-1] > 1.4 * self.values[-2] or self.values[-1] < 0.6 * self.values[-2]:
                color.append("-r")

            elif (self.values[-1] > self.values[-2] and self.values[-1] < 1.05*self.values[-2]) and (self.values[-1] < self.values[-2] and self.values[-1] > 0.95*self.values[-2]):
                color.append("-o")
            else:
                color.append("-g")

        else:
            color = '-g'
        xs.append(len(self.values))
        ys.append(self.values[-1])
       

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())