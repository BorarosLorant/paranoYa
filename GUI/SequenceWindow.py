# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sequence.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SequenceWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 339)
        Dialog.setStyleSheet("background-color:#D8D8D8")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Input_Area_Sequence = QtWidgets.QWidget(Dialog)
        self.Input_Area_Sequence.setObjectName("Input_Area_Sequence")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Input_Area_Sequence)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Input_path_lbl = QtWidgets.QLabel(self.Input_Area_Sequence)
        self.Input_path_lbl.setStyleSheet("Color:#520202")
        self.Input_path_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Input_path_lbl.setObjectName("Input_path_lbl")
        self.verticalLayout.addWidget(self.Input_path_lbl)
        self.Path_Input = QtWidgets.QLineEdit(self.Input_Area_Sequence)
        self.Path_Input.setStyleSheet("background-color:#FFFFFF;color:#520202")
        self.Path_Input.setObjectName("Path_Input")
        self.verticalLayout.addWidget(self.Path_Input)
        self.radbtn_1mb = QtWidgets.QRadioButton(self.Input_Area_Sequence)
        self.radbtn_1mb.setStyleSheet("Color:#520202")
        self.radbtn_1mb.setObjectName("radbtn_1mb")
        self.verticalLayout.addWidget(self.radbtn_1mb)
        self.radbtn_10mb = QtWidgets.QRadioButton(self.Input_Area_Sequence)
        self.radbtn_10mb.setStyleSheet("Color:#520202")
        self.radbtn_10mb.setObjectName("radbtn_10mb")
        self.verticalLayout.addWidget(self.radbtn_10mb)
        self.FileList = QtWidgets.QListWidget(self.Input_Area_Sequence)
        self.FileList.setStyleSheet("background-color:#FFFFFF;Color:#520202")
        self.FileList.setObjectName("FileList")
        item = QtWidgets.QListWidgetItem()
        self.FileList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileList.addItem(item)
        self.verticalLayout.addWidget(self.FileList)
        self.horizontalLayout.addWidget(self.Input_Area_Sequence)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sequence"))
        self.Input_path_lbl.setText(_translate("Dialog", "Set input path:"))
        self.radbtn_1mb.setText(_translate("Dialog", "1 MB files"))
        self.radbtn_10mb.setText(_translate("Dialog", "10 MB files"))
        __sortingEnabled = self.FileList.isSortingEnabled()
        self.FileList.setSortingEnabled(False)
        item = self.FileList.item(0)
        item.setText(_translate("Dialog", "New Item"))
        item = self.FileList.item(1)
        item.setText(_translate("Dialog", "New Item"))
        item = self.FileList.item(2)
        item.setText(_translate("Dialog", "New Item"))
        item = self.FileList.item(3)
        item.setText(_translate("Dialog", "New Item"))
        self.FileList.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
