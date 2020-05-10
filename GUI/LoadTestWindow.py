# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadTestWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadTestWindow(object):
    def setupUi(self, LoadTest):
        LoadTest.setObjectName("LoadTest")
        LoadTest.resize(544, 420)
        self.horizontalLayout = QtWidgets.QHBoxLayout(LoadTest)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Buttonwidget = QtWidgets.QWidget(LoadTest)
        self.Buttonwidget.setObjectName("Buttonwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Buttonwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Loadbtn = QtWidgets.QPushButton(self.Buttonwidget)
        self.Loadbtn.setStyleSheet("background-color:#720E0E;color:#F86262")
        self.Loadbtn.setObjectName("Loadbtn")
        self.verticalLayout_4.addWidget(self.Loadbtn)
        self.horizontalLayout.addWidget(self.Buttonwidget)
        self.Infowidget = QtWidgets.QWidget(LoadTest)
        self.Infowidget.setObjectName("Infowidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Infowidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Info_Area = QtWidgets.QWidget(self.Infowidget)
        self.Info_Area.setStyleSheet("background-color:#790E0E")
        self.Info_Area.setObjectName("Info_Area")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Info_Area)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Info_Text = QtWidgets.QWidget(self.Info_Area)
        self.Info_Text.setStyleSheet("")
        self.Info_Text.setObjectName("Info_Text")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Info_Text)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.Info_Text)
        self.label.setStyleSheet("color:#F86262")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.Info_Text)
        self.textEdit = QtWidgets.QTextEdit(self.Info_Area)
        self.textEdit.setStyleSheet("background-color:#E7E4E4")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_3.addWidget(self.Info_Area)
        self.horizontalLayout.addWidget(self.Infowidget)

        self.retranslateUi(LoadTest)
        QtCore.QMetaObject.connectSlotsByName(LoadTest)

    def retranslateUi(self, LoadTest):
        _translate = QtCore.QCoreApplication.translate
        LoadTest.setWindowTitle(_translate("LoadTest", "Load Test Set"))
        self.Loadbtn.setText(_translate("LoadTest", "Load"))
        self.label.setText(_translate("LoadTest", "Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadTest = QtWidgets.QDialog()
    ui = Ui_LoadTest()
    ui.setupUi(LoadTest)
    LoadTest.show()
    sys.exit(app.exec_())
