# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTest.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTestWindow(object):
    def setupUi(self, AddTestWindow):
        AddTestWindow.setObjectName("Dialog")
        AddTestWindow.resize(692, 546)
        AddTestWindow.setWindowOpacity(1.0)
        AddTestWindow.setStyleSheet("background-color:#D8D8D8;")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(AddTestWindow)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 56, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.Info_Area = QtWidgets.QWidget(AddTestWindow)
        self.Info_Area.setObjectName("Info_Area")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Info_Area)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TestArea = QtWidgets.QWidget(self.Info_Area)
        self.TestArea.setObjectName("TestArea")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.TestArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Test_Combo = QtWidgets.QComboBox(self.TestArea)
        self.Test_Combo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Test_Combo.setStyleSheet("background-color:#550202;color:#F86262")
        self.Test_Combo.setObjectName("Test_Combo")
        self.Test_Combo.addItem("")
        self.Test_Combo.addItem("")
        self.Test_Combo.addItem("")
        self.Test_Combo.addItem("")
        self.verticalLayout_3.addWidget(self.Test_Combo)
        self.Addbtn = QtWidgets.QPushButton(self.TestArea)
        self.Addbtn.setStyleSheet("background-color:#790E0E;color:#F86262")
        self.Addbtn.setObjectName("Addbtn")
        self.verticalLayout_3.addWidget(self.Addbtn)
        self.Test_List = QtWidgets.QListWidget(self.TestArea)
        self.Test_List.setStyleSheet("background-color:#FFFFFF;color:#520202")
        self.Test_List.setObjectName("Test_List")
        item = QtWidgets.QListWidgetItem()
        self.Test_List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Test_List.addItem(item)
        self.verticalLayout_3.addWidget(self.Test_List)
        self.horizontalLayout.addWidget(self.TestArea)
        self.InputArea = QtWidgets.QWidget(self.Info_Area)
        self.InputArea.setObjectName("InputArea")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.InputArea)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Param1_lbl = QtWidgets.QLabel(self.InputArea)
        self.Param1_lbl.setStyleSheet("background-color:#D8D8D8;color:#550202")
        self.Param1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Param1_lbl.setObjectName("Param1_lbl")
        self.verticalLayout_2.addWidget(self.Param1_lbl)
        self.Param1_input = QtWidgets.QLineEdit(self.InputArea)
        self.Param1_input.setStyleSheet("background-color:#FFFFFF;color:#520202")
        self.Param1_input.setObjectName("Param1_input")
        self.verticalLayout_2.addWidget(self.Param1_input)
        self.Param2_lbl = QtWidgets.QLabel(self.InputArea)
        self.Param2_lbl.setStyleSheet("background-color:#D8D8D8;color:#550202")
        self.Param2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Param2_lbl.setObjectName("Param2_lbl")
        self.verticalLayout_2.addWidget(self.Param2_lbl)
        self.Param2_input = QtWidgets.QLineEdit(self.InputArea)
        self.Param2_input.setStyleSheet("background-color:#FFFFFF;color:#520202")
        self.Param2_input.setObjectName("Param2_input")
        self.verticalLayout_2.addWidget(self.Param2_input)
        self.Param3_lbl = QtWidgets.QLabel(self.InputArea)
        self.Param3_lbl.setStyleSheet("background-color:#D8D8D8;color:#550202")
        self.Param3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Param3_lbl.setObjectName("Param3_lbl")
        self.verticalLayout_2.addWidget(self.Param3_lbl)
        self.Param3_input = QtWidgets.QLineEdit(self.InputArea)
        self.Param3_input.setStyleSheet("background-color:#FFFFFF;color:#520202")
        self.Param3_input.setObjectName("Param3_input")
        self.verticalLayout_2.addWidget(self.Param3_input)
        self.Setbtn = QtWidgets.QPushButton(self.InputArea)
        self.Setbtn.setStyleSheet("background-color:#790E0E;color:#F86262")
        self.Setbtn.setObjectName("Setbtn")
        self.verticalLayout_2.addWidget(self.Setbtn)
        self.horizontalLayout.addWidget(self.InputArea)
        self.verticalLayout_4.addWidget(self.Info_Area)
        spacerItem2 = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 56, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.ButtonArea = QtWidgets.QWidget(AddTestWindow)
        self.ButtonArea.setObjectName("ButtonArea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ButtonArea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Savebtn = QtWidgets.QPushButton(self.ButtonArea)
        self.Savebtn.setStyleSheet("background-color:#790E0E;color:#F86262")
        self.Savebtn.setObjectName("Savebtn")
        self.verticalLayout.addWidget(self.Savebtn)
        self.Loadbtn = QtWidgets.QPushButton(self.ButtonArea)
        self.Loadbtn.setStyleSheet("background-color:#790E0E;color:#F86262")
        self.Loadbtn.setObjectName("Loadbtn")
        self.verticalLayout.addWidget(self.Loadbtn)
        self.verticalLayout_4.addWidget(self.ButtonArea)
        spacerItem4 = QtWidgets.QSpacerItem(671, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem4)

        self.retranslateUi(AddTestWindow)
        QtCore.QMetaObject.connectSlotsByName(AddTestWindow)

    def retranslateUi(self, AddTestWindow):
        _translate = QtCore.QCoreApplication.translate
        AddTestWindow.setWindowTitle(_translate("Dialog", "AddTest"))
        self.Test_Combo.setItemText(0, _translate("Dialog", "Test1"))
        self.Test_Combo.setItemText(1, _translate("Dialog", "Test2"))
        self.Test_Combo.setItemText(2, _translate("Dialog", "Test3"))
        self.Test_Combo.setItemText(3, _translate("Dialog", "Test4"))
        self.Addbtn.setText(_translate("Dialog", "Add"))
        __sortingEnabled = self.Test_List.isSortingEnabled()
        self.Test_List.setSortingEnabled(False)
        item = self.Test_List.item(0)
        item.setText(_translate("Dialog", "Test1"))
        item = self.Test_List.item(1)
        item.setText(_translate("Dialog", "Test2"))
        self.Test_List.setSortingEnabled(__sortingEnabled)
        self.Param1_lbl.setText(_translate("Dialog", "Param1"))
        self.Param1_input.setText(_translate("Dialog", "0.01"))
        self.Param2_lbl.setText(_translate("Dialog", "Param2"))
        self.Param2_input.setText(_translate("Dialog", "0.02"))
        self.Param3_lbl.setText(_translate("Dialog", "Param3"))
        self.Param3_input.setText(_translate("Dialog", "8848"))
        self.Setbtn.setText(_translate("Dialog", "Set"))
        self.Savebtn.setText(_translate("Dialog", "Save"))
        self.Loadbtn.setText(_translate("Dialog", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddTestWindow = QtWidgets.QDialog()
    ui = Ui_AddTestWindow()
    ui.setupUi(AddTestWindow)
    AddTestWindow.show()
    sys.exit(app.exec_())
