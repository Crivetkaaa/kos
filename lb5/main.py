from main_win import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from utilts.parse import Global, parse


class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data_val = []
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.get_val()
        self.ui.pushButton.clicked.connect(self.get_kyrs)

    def get_kyrs(self):
        text = self.ui.comboBox.currentText()
        print(Global.kall_info)

        self.ui.label.setText(f'{Global.kall_info[text]["exchange_rates"]} руб.')
       
    def get_val(self):
        parse()
        count = 0
        for item in Global.data:
            self.data_val.append(Global.all_info[item]["currencies"])

        for item in self.data_val:
            print(item)
            self.ui.comboBox.addItem(item)
            count += 1


def main():
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()