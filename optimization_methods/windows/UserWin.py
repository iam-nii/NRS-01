# Form implementation generated from reading ui file 'userWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtGui import QAction, QIcon
# from PyQt6.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QLabel,
#     QMainWindow,
#     QStatusBar,
#     QToolBar,
# )

import optimization_methods.windows.signals as signals
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QAction


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 705)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 50, 371, 551))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 11, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(560, 50, 301, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 100, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 140, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.min_a1_txt = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.min_a1_txt.setGeometry(QtCore.QRect(500, 139, 81, 31))
        self.min_a1_txt.setObjectName("min_a1_txt")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 191, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.min_a2_txt = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.min_a2_txt.setGeometry(QtCore.QRect(500, 190, 81, 31))
        self.min_a2_txt.setObjectName("min_a2_txt")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(640, 140, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.max_a1_txt = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.max_a1_txt.setGeometry(QtCore.QRect(720, 139, 81, 31))
        self.max_a1_txt.setObjectName("max_a1_txt")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(640, 190, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.max_a2_txt = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.max_a2_txt.setGeometry(QtCore.QRect(720, 189, 81, 31))
        self.max_a2_txt.setObjectName("max_a2_txt")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(420, 240, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(420, 280, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.condition_txt = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.condition_txt.setGeometry(QtCore.QRect(520, 280, 341, 31))
        self.condition_txt.setObjectName("condition_txt")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(740, 340, 121, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(420, 340, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(420, 380, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(420, 460, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(420, 510, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(420, 420, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.method_cbx = QtWidgets.QComboBox(parent=self.centralwidget)
        self.method_cbx.setGeometry(QtCore.QRect(620, 420, 241, 31))
        self.method_cbx.setObjectName("method_cbx")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(420, 560, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(740, 460, 121, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(740, 510, 121, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(740, 560, 121, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.calculate_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculate_btn.setGeometry(QtCore.QRect(730, 630, 131, 31))
        self.calculate_btn.setObjectName("calculate_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(parent=self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.changeUser_menu = QtGui.QAction('Изменить пользователя',parent=MainWindow)
        self.changeUser_menu.setObjectName("changeUser_menu")
        self.help_menu = QtGui.QAction('Справка',parent=MainWindow)
        self.help_menu.setObjectName("help_menu")
        self.exit_menu = QtGui.QAction('Выйти',parent=MainWindow)
        self.exit_menu.setObjectName("exit_menu")
        self.menuMenu.addAction(self.changeUser_menu)
        self.menuMenu.addAction(self.help_menu)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.exit_menu)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect to the signals in the signals file
        signals.connect_signals(self)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Вариант :"))
        self.label_2.setText(_translate("MainWindow", "Параметры задачи"))
        self.label_3.setText(_translate("MainWindow", "Целевая функция : "))
        self.label_4.setText(_translate("MainWindow", " Ограничения первого рода"))
        self.label_5.setText(_translate("MainWindow", "Min A1 :"))
        self.label_6.setText(_translate("MainWindow", "Min A2 :"))
        self.label_7.setText(_translate("MainWindow", "Max A1 :"))
        self.label_8.setText(_translate("MainWindow", "Max A2 :"))
        self.label_9.setText(_translate("MainWindow", " Ограничения второго рода"))
        self.label_10.setText(_translate("MainWindow", "Условие :"))
        self.label_12.setText(_translate("MainWindow", "Точность нахождения решения : "))
        self.label_11.setText(_translate("MainWindow", "Настройки решения оптимизационной задачи"))
        self.label_13.setText(_translate("MainWindow", "Точность отображения 3D графика : "))
        self.label_14.setText(_translate("MainWindow", "Точность отображения табличных значениий : "))
        self.label_15.setText(_translate("MainWindow", "Метод поиска экстремума :"))
        self.label_16.setText(_translate("MainWindow", "Количество ЛРЗ на 2D графике (5-25) : "))
        self.calculate_btn.setText(_translate("MainWindow", "Расчитать"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.changeUser_menu.setText(_translate("MainWindow", "Change User"))
        self.help_menu.setText(_translate("MainWindow", "Help"))
        self.exit_menu.setText(_translate("MainWindow", "Exit"))