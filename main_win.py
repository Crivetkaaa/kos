# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 208)
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 191, 22))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setStatusTip("")
        self.comboBox.setWhatsThis("")
        self.comboBox.setAccessibleName("")
        self.comboBox.setAccessibleDescription("")
        self.comboBox.setStyleSheet("")
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(220, 10, 75, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(10, 80, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 47, 13))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.pushButton.setText(_translate("MainWindow", "Получить\n"
"курс"))
        self.label_2.setText(_translate("MainWindow", "Валюты"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
