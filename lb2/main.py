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
        self.last_value = 0
        self.all_labels = [self.ui.label_3, self.ui.label_4, self.ui.label_5, 
                           self.ui.label_6, self.ui.label_7, self.ui.label_8, 
                           self.ui.label_9, self.ui.label_10, self.ui.label_11, self.ui.label_12]

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.ui.pushButton.clicked.connect(self.get_text)
    
    def update_info(self, value):
        self.values.append(value)
        self.last_value = value
        self.update_labels()
    
    def else_info(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("TypeError")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def maxmin(self, max, min):
        if max != '':
            try:
                float_max = float(max)
            except:
                self.else_info('Максимум должен быть числом.')
        else:
            float_max = float('+inf')

        if min != '':
            try:
                float_min = float(min)
            except:
                self.else_info('Минимум должен быть числом.')

        else:
            float_min = float('-inf')

        return float_max, float_min

    def check_max_min(self, value):
        max = self.ui.lineEdit_max.text()
        min = self.ui.lineEdit_min.text()
        max, min = self.maxmin(max, min)
        if max and min:
            if value < max and value > min:
                self.update_info(value)
            else:
                self.else_info('Число выходит за пределы')        

    def get_text(self):
        value = self.ui.lineEdit.text()
        try:
            float_value = float(value)
            self.check_max_min(float_value)

        except:     
            self.else_info("Введите число.")
        
    def update_labels(self):
        if len(self.values) < 10:
            for i in range(0, len(self.values)):
                self.all_labels[i].setText(str(self.values[i]))
        else:
            for i in range(1, 10):
                self.all_labels[-i].setText(str(self.values[-i]))
        self.update_file()

    def update_file(self):
        from test import xs, ys, color, average, vals, labels, color_diogram, her, all_values_from_test
        if len(self.values) >= 2:
            if self.values[-1] > 1.4 * self.values[-2] or self.values[-1] < 0.6 * self.values[-2]:
                color.append("-r")

            elif (self.values[-1] > 1.05*self.values[-2] or self.values[-1] < 0.95*self.values[-2]):
                color.append("orange")
            else:
                color.append("-g")

        else:
            color = '-g'

        xs.append(len(self.values))
        ys.append(self.values[-1])
        average.append(self.average_func())
        if self.last_value not in all_values_from_test:
            all_values_from_test.append(self.values[-1])
        
        her[self.last_value] = {
            'count': self.numbers_in_values()
        }
        labels.clear()
        vals.clear()
        for value in all_values_from_test:
            labels.append(str(value))
            vals.append(her[value]['count'])
            
    def numbers_in_values(self):
        value = self.values[-1]
        count = 0
        for i in range(0, len(self.values)):
            if self.values[i] == value:
                count+=1
        return count  
    
    def average_func(self):
        sum = 0
        for i in range(0, len(self.values)):
            sum += self.values[i]
        return sum/len(self.values)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()