# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanallenar.ui'
#
# Created: Thu Jan 13 23:03:20 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ventanallenar(object):
    def setupUi(self, ventanallenar):
        ventanallenar.setObjectName(_fromUtf8("ventanallenar"))
        ventanallenar.resize(388, 171)
        self.verticalLayout = QtGui.QVBoxLayout(ventanallenar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ventanallenar)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textoid = QtGui.QLineEdit(ventanallenar)
        self.textoid.setObjectName(_fromUtf8("textoid"))
        self.gridLayout.addWidget(self.textoid, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.textocorredor = QtGui.QLineEdit(ventanallenar)
        self.textocorredor.setObjectName(_fromUtf8("textocorredor"))
        self.gridLayout.addWidget(self.textocorredor, 1, 2, 1, 1)
        self.botonagregar = QtGui.QPushButton(ventanallenar)
        self.botonagregar.setObjectName(_fromUtf8("botonagregar"))
        self.gridLayout.addWidget(self.botonagregar, 1, 3, 1, 1)
        self.label_2 = QtGui.QLabel(ventanallenar)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(ventanallenar)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.botoncerrar = QtGui.QPushButton(ventanallenar)
        self.botoncerrar.setObjectName(_fromUtf8("botoncerrar"))
        self.horizontalLayout_3.addWidget(self.botoncerrar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(ventanallenar)
        QtCore.QObject.connect(self.botoncerrar, QtCore.SIGNAL(_fromUtf8("clicked()")), ventanallenar.close)
        QtCore.QObject.connect(self.textocorredor, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.botonagregar.click)
        QtCore.QMetaObject.connectSlotsByName(ventanallenar)
        ventanallenar.setTabOrder(self.textocorredor, self.botonagregar)
        ventanallenar.setTabOrder(self.botonagregar, self.botoncerrar)
        ventanallenar.setTabOrder(self.botoncerrar, self.textoid)

    def retranslateUi(self, ventanallenar):
        ventanallenar.setWindowTitle(QtGui.QApplication.translate("ventanallenar", "Contrarreloj - Rellenar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ventanallenar", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rellenar números</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.botonagregar.setText(QtGui.QApplication.translate("ventanallenar", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ventanallenar", "Número en llegar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ventanallenar", "Número de participante", None, QtGui.QApplication.UnicodeUTF8))
        self.botoncerrar.setText(QtGui.QApplication.translate("ventanallenar", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))

