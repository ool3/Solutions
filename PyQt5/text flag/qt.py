# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hrhr.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(363, 207)
        MainWindow.setStyleSheet("b")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("background-color: orange;border: 0")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_4.setObjectName("formLayout_4")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_10.setChecked(False)
        self.radioButton_10.setAutoRepeat(False)
        self.radioButton_10.setObjectName("radioButton_10")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_11.setChecked(False)
        self.radioButton_11.setAutoRepeat(False)
        self.radioButton_11.setObjectName("radioButton_11")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_12.setChecked(True)
        self.radioButton_12.setAutoRepeat(False)
        self.radioButton_12.setObjectName("radioButton_12")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_12)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_7.setChecked(False)
        self.radioButton_7.setAutoRepeat(False)
        self.radioButton_7.setObjectName("radioButton_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_7)
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_9.setChecked(False)
        self.radioButton_9.setAutoRepeat(False)
        self.radioButton_9.setObjectName("radioButton_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_9)
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_8.setChecked(True)
        self.radioButton_8.setAutoRepeat(False)
        self.radioButton_8.setObjectName("radioButton_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_8)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_5.setObjectName("formLayout_5")
        self.radioButton_14 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_14.setChecked(False)
        self.radioButton_14.setAutoRepeat(False)
        self.radioButton_14.setObjectName("radioButton_14")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_14)
        self.radioButton_15 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_15.setChecked(False)
        self.radioButton_15.setAutoRepeat(False)
        self.radioButton_15.setObjectName("radioButton_15")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.radioButton_15)
        self.radioButton_13 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_13.setChecked(True)
        self.radioButton_13.setAutoRepeat(False)
        self.radioButton_13.setObjectName("radioButton_13")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_13)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.groupBox)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monotxt_IV50")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Предмет 1"))
        self.label.setText(_translate("MainWindow", "Предмет 2"))
        self.label_3.setText(_translate("MainWindow", "Предмет 3"))
        self.radioButton_10.setText(_translate("MainWindow", "Математика"))
        self.radioButton_11.setText(_translate("MainWindow", "Физика"))
        self.radioButton_12.setText(_translate("MainWindow", "Биология"))
        self.radioButton_7.setText(_translate("MainWindow", "Математика"))
        self.radioButton_9.setText(_translate("MainWindow", "Биология"))
        self.radioButton_8.setText(_translate("MainWindow", "Физика"))
        self.radioButton_14.setText(_translate("MainWindow", "Физика"))
        self.radioButton_15.setText(_translate("MainWindow", "Биология"))
        self.radioButton_13.setText(_translate("MainWindow", "Математика"))
        self.label_4.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Сделать флаг"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())