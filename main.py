from main_win import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import utilts.parse as parse

# КЛАСС ОКНА
class Interface(QtWidgets.QWidget):
    # Инициализируем объект класса
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.values = []
        self.last_value = 0

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        # Ожидаем нажатия кнопки
        self.ui.pushButton.clicked.connect(self.get_info)
    
    # Считывается с файла и генерирует текс
    def generate_text(self):
        with open('files/info.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        print(text)
        return text
    # После нажатия кнопки 
    def get_info(self):
        parse.main() # Запускается функция из файла parse
        self.ui.label.setText("Данные\nполучены") #Появляется надпись
        self.ui.label_2.setText(self.generate_text()) # Выводиться вся спаршеная инфа


def main():
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
