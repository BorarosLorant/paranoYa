# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetailedResultsByFilename.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SummaryWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(642, 448)
        Dialog.setStyleSheet("background-color:#D8D8D8")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filenamelbl = QtWidgets.QLabel(Dialog)
        self.filenamelbl.setStyleSheet("color:#520202")
        self.filenamelbl.setAlignment(QtCore.Qt.AlignCenter)
        self.filenamelbl.setObjectName("filenamelbl")
        self.verticalLayout.addWidget(self.filenamelbl)
        self.Detailedresultstable = QtWidgets.QTableView(Dialog)
        self.Detailedresultstable.setBaseSize(QtCore.QSize(3, 10))
        self.Detailedresultstable.setStyleSheet("background-color:#FFFFFF")
        self.Detailedresultstable.setObjectName("Detailedresultstable")
        self.verticalLayout.addWidget(self.Detailedresultstable)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "\"Filename\" summary"))
        self.filenamelbl.setText(_translate("Dialog", "\"Filename\" summary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
