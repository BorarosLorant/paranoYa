# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DetailedResultsByFilenameNFMKRs.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(642, 448)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filenamelbl = QLabel(Dialog)
        self.filenamelbl.setObjectName(u"filenamelbl")
        self.filenamelbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.filenamelbl)

        self.Detailedresultstable = QTableView(Dialog)
        self.Detailedresultstable.setObjectName(u"Detailedresultstable")
        self.Detailedresultstable.setBaseSize(QSize(3, 10))

        self.verticalLayout.addWidget(self.Detailedresultstable)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.filenamelbl.setText(QCoreApplication.translate("Dialog", u"\"Filename\" summary", None))
    # retranslateUi

