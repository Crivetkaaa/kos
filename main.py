from main_win import *
from PyQt5 import QtCore, QtGui, QtWidgets
from DataBase import DB
from PyQt5.QtWidgets import QMessageBox
import random

import sys


class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        DB.create_table()
        self.ui.pushButton.clicked.connect(self.get_info)
        self.ui.pushButton_2.clicked.connect(self.insert_info)


    def num(self, len):
        num = [i for i in range(0, len)]
        return num

    def num_to_str(self, num):
        str_num = [str(i+1) for i in num]
        return str_num

    def check_data(self, data):
        if len(data) > 0:
            return True
        else:
            return False

    def else_info(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("TypeError")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def get_info(self):
        sclad = int(self.ui.comboBox.currentText()[-1])
        data = DB.get_info(text=f"SELECT * FROM users WHERE sclad={sclad}")

        if self.check_data(data):
            len_data = len(data)

            num = self.num(len_data)

            self.ui.tableWidget.setRowCount(num[-1]+1)
            self.ui.tableWidget.setVerticalHeaderLabels(self.num_to_str(num))

            for i in num:
                product_name = QtWidgets.QTableWidgetItem(data[i][1])
                product_code = QtWidgets.QTableWidgetItem(data[i][2])
                product_count = QtWidgets.QTableWidgetItem(str(data[i][3]))

                self.ui.tableWidget.setItem(i, 0, product_name)
                self.ui.tableWidget.setItem(i, 1, product_code)
                self.ui.tableWidget.setItem(i, 2, product_count)
        else:
            self.else_info(text=f'На складе {sclad} нет товаров')

    def generate_code(self, sclad):
        random_code = random.randint(1, 10000)
        if len(str(random_code))<5:
            string = f"00{sclad}{'0'*(5-len(str(random_code)))}{random_code}"
        else:
            string = f"00{sclad}{random_code}"

        return string

    def check_sclad_product(self, product_name, sclad, product_count):
        data = DB.get_info(text=f"SELECT * FROM users WHERE sclad={sclad}")
        all_name = []
        for row in data:
            all_name.append(row[1])
        
        if product_name in all_name:
            DB.update_info(name=product_name, count=product_count, sclad=sclad)
        else:
            code = self.generate_code(sclad=sclad)
            DB.inser_info(sclad=sclad, name=product_name, code=code, count=product_count)

    def insert_info(self):
        sclad = int(self.ui.comboBox.currentText()[-1])
        product_name = self.ui.lineEdit.text()
        product_count = self.ui.lineEdit_2.text()
        self.check_sclad_product(sclad=sclad, product_name=product_name, product_count=product_count)
        self.get_info_2()



    def get_info_2(self):
        sclad = int(self.ui.comboBox_2.currentText()[-1])
        data = DB.get_info(text=f"SELECT * FROM users WHERE sclad={sclad}")

        if self.check_data(data):
            len_data = len(data)

            num = self.num(len_data)

            self.ui.tableWidget_2.setRowCount(num[-1]+1)
            self.ui.tableWidget_2.setVerticalHeaderLabels(self.num_to_str(num))

            for i in num:
                product_name = QtWidgets.QTableWidgetItem(data[i][1])
                product_code = QtWidgets.QTableWidgetItem(data[i][2])
                product_count = QtWidgets.QTableWidgetItem(str(data[i][3]))

                self.ui.tableWidget_2.setItem(i, 0, product_name)
                self.ui.tableWidget_2.setItem(i, 1, product_code)
                self.ui.tableWidget_2.setItem(i, 2, product_count)
        else:
            self.else_info(text=f'На складе {sclad} нет товаров')


def main():
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()