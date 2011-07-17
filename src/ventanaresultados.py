# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaresultados.ui'
#
# Created: Fri Jan 14 22:18:32 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ventanaresultados(object):
    def setupUi(self, ventanaresultados):
        ventanaresultados.setObjectName(_fromUtf8("ventanaresultados"))
        ventanaresultados.resize(704, 569)
        self.verticalLayout = QtGui.QVBoxLayout(ventanaresultados)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ventanaresultados)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(ventanaresultados)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cajacategorias = QtGui.QComboBox(ventanaresultados)
        self.cajacategorias.setObjectName(_fromUtf8("cajacategorias"))
        self.cajacategorias.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cajacategorias)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.treeresultados = QtGui.QTreeWidget(ventanaresultados)
        self.treeresultados.setObjectName(_fromUtf8("treeresultados"))
        self.verticalLayout.addWidget(self.treeresultados)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.botonresultados = QtGui.QPushButton(ventanaresultados)
        self.botonresultados.setObjectName(_fromUtf8("botonresultados"))
        self.horizontalLayout.addWidget(self.botonresultados)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.botoncerrar = QtGui.QPushButton(ventanaresultados)
        self.botoncerrar.setObjectName(_fromUtf8("botoncerrar"))
        self.horizontalLayout.addWidget(self.botoncerrar)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ventanaresultados)
        QtCore.QObject.connect(self.botoncerrar, QtCore.SIGNAL(_fromUtf8("clicked()")), ventanaresultados.close)
        QtCore.QMetaObject.connectSlotsByName(ventanaresultados)

    def retranslateUi(self, ventanaresultados):
        ventanaresultados.setWindowTitle(QtGui.QApplication.translate("ventanaresultados", "Contrarreloj - Resultados", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ventanaresultados", "<center>Resultados</center>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ventanaresultados", "Categoría:", None, QtGui.QApplication.UnicodeUTF8))
        self.cajacategorias.setItemText(0, QtGui.QApplication.translate("ventanaresultados", "Generales", None, QtGui.QApplication.UnicodeUTF8))
        self.treeresultados.headerItem().setText(0, QtGui.QApplication.translate("ventanaresultados", "Lugar general", None, QtGui.QApplication.UnicodeUTF8))
        self.treeresultados.headerItem().setText(1, QtGui.QApplication.translate("ventanaresultados", "Tiempo", None, QtGui.QApplication.UnicodeUTF8))
        self.treeresultados.headerItem().setText(2, QtGui.QApplication.translate("ventanaresultados", "Número", None, QtGui.QApplication.UnicodeUTF8))
        self.treeresultados.headerItem().setText(3, QtGui.QApplication.translate("ventanaresultados", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.treeresultados.headerItem().setText(4, QtGui.QApplication.translate("ventanaresultados", "Equipo", None, QtGui.QApplication.UnicodeUTF8))
        self.treeresultados.headerItem().setText(5, QtGui.QApplication.translate("ventanaresultados", "Categoría", None, QtGui.QApplication.UnicodeUTF8))
        self.botonresultados.setText(QtGui.QApplication.translate("ventanaresultados", "Ver resultados en texto plano", None, QtGui.QApplication.UnicodeUTF8))
        self.botoncerrar.setText(QtGui.QApplication.translate("ventanaresultados", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))

