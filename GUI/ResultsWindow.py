# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.SummaryWindow import Ui_SummaryWindow

class Ui_ResultsWindow(object):

    def openSum(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_SummaryWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(610, 432)
        Dialog.setStyleSheet("background-color:#D8D8D8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resultArea = QtWidgets.QWidget(Dialog)
        self.resultArea.setObjectName("resultArea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.resultArea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addWidget(self.resultArea)
        self.Resultslbl = QtWidgets.QLabel(Dialog)
        self.Resultslbl.setStyleSheet("color:#520202")
        self.Resultslbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Resultslbl.setObjectName("Resultslbl")
        self.verticalLayout_2.addWidget(self.Resultslbl)
        self.resultTable = QtWidgets.QTableView(Dialog)
        self.resultTable.setStyleSheet("background-color:#FFFFFF;color:#520202")
        self.resultTable.setObjectName("resultTable")
        self.verticalLayout_2.addWidget(self.resultTable)
        self.ButtonArea = QtWidgets.QWidget(Dialog)
        self.ButtonArea.setObjectName("ButtonArea")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ButtonArea)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.ButtonArea)
        self.pushButton.setStyleSheet("background-color:#790E0E;color:#F86262")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.ButtonArea)
        self.pushButton_2.setStyleSheet("background-color:#790E0E;color:#F86262")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.ButtonArea)
        self.pushButton_3.setStyleSheet("background-color:#790E0E;color:#F86262")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.ButtonArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Results"))
        self.Resultslbl.setText(_translate("Dialog", "Results"))
        self.pushButton.setText(_translate("Dialog", "Summary"))
        self.pushButton_2.setText(_translate("Dialog", "Ok"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
