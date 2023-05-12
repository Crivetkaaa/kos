from main_win import * # Файл генерируемы в QtDesigner из него импортируются все функции и классы
from PyQt5 import QtCore, QtGui, QtWidgets #Библиотека для взаимодействия с виджетами
import sys #Библиотека для запуска программы
import utilts.parse as parse # Импортируем функцию и з файла parse.py

# КЛАСС ОКНА
class Interface(QtWidgets.QWidget):
    # Инициализируем объект класса
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow() # Создаем предмет класс
        self.ui.setupUi(self)
        # Переменные необходимые для работы программы
        self.values = []
        self.last_value = 0

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        # Ожидаем нажатия кнопки
        self.ui.pushButton.clicked.connect(self.get_info)
    
    # Считывается с файла и генерирует текст
    def generate_text(self):
        with open('files/info.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        print(text)
        return text
    # После нажатия кнопки запускается этот блок кода
    def get_info(self):
        parse.main() # Запускается функция из файла parse
        self.ui.label.setText("Данные\nполучены") #Появляется надпись
        self.ui.label_2.setText(self.generate_text()) # Выводиться вся спаршеная инфа


def main():
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface() # Создается объект класса Interface
    mywin.show() # Показывает окно
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
