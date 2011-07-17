# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaajustes.ui'
#
# Created: Fri Jan 14 19:35:27 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ventanaAjustes(object):
    def setupUi(self, ventanaAjustes):
        ventanaAjustes.setObjectName(_fromUtf8("ventanaAjustes"))
        ventanaAjustes.resize(426, 329)
        self.verticalLayout = QtGui.QVBoxLayout(ventanaAjustes)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelAjustes = QtGui.QLabel(ventanaAjustes)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelAjustes.setFont(font)
        self.labelAjustes.setObjectName(_fromUtf8("labelAjustes"))
        self.verticalLayout.addWidget(self.labelAjustes)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelCadacuanto = QtGui.QLabel(ventanaAjustes)
        self.labelCadacuanto.setObjectName(_fromUtf8("labelCadacuanto"))
        self.gridLayout.addWidget(self.labelCadacuanto, 1, 0, 1, 1)
        self.textoCadacuanto = QtGui.QLineEdit(ventanaAjustes)
        self.textoCadacuanto.setObjectName(_fromUtf8("textoCadacuanto"))
        self.gridLayout.addWidget(self.textoCadacuanto, 1, 1, 1, 1)
        self.label = QtGui.QLabel(ventanaAjustes)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.textocategoria = QtGui.QLineEdit(ventanaAjustes)
        self.textocategoria.setObjectName(_fromUtf8("textocategoria"))
        self.gridLayout.addWidget(self.textocategoria, 2, 1, 1, 1)
        self.listacategorias = QtGui.QListWidget(ventanaAjustes)
        self.listacategorias.setObjectName(_fromUtf8("listacategorias"))
        self.gridLayout.addWidget(self.listacategorias, 4, 0, 1, 3)
        self.botonremover = QtGui.QPushButton(ventanaAjustes)
        self.botonremover.setObjectName(_fromUtf8("botonremover"))
        self.gridLayout.addWidget(self.botonremover, 3, 2, 1, 1)
        self.botonagregar = QtGui.QPushButton(ventanaAjustes)
        self.botonagregar.setObjectName(_fromUtf8("botonagregar"))
        self.gridLayout.addWidget(self.botonagregar, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ventanaAjustes)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ventanaAjustes)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ventanaAjustes.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ventanaAjustes.reject)
        QtCore.QObject.connect(self.textocategoria, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.botonagregar.click)
        QtCore.QMetaObject.connectSlotsByName(ventanaAjustes)
        ventanaAjustes.setTabOrder(self.textoCadacuanto, self.textocategoria)
        ventanaAjustes.setTabOrder(self.textocategoria, self.botonagregar)
        ventanaAjustes.setTabOrder(self.botonagregar, self.buttonBox)
        ventanaAjustes.setTabOrder(self.buttonBox, self.listacategorias)

    def retranslateUi(self, ventanaAjustes):
        ventanaAjustes.setWindowTitle(QtGui.QApplication.translate("ventanaAjustes", "Ajustes principales", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAjustes.setText(QtGui.QApplication.translate("ventanaAjustes", "<center>Ajustes principales</center>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCadacuanto.setText(QtGui.QApplication.translate("ventanaAjustes", "Cada cuanto (segundos)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ventanaAjustes", "Agregar Categoría:", None, QtGui.QApplication.UnicodeUTF8))
        self.botonremover.setText(QtGui.QApplication.translate("ventanaAjustes", "Remover", None, QtGui.QApplication.UnicodeUTF8))
        self.botonagregar.setText(QtGui.QApplication.translate("ventanaAjustes", "Agregar", None, QtGui.QApplication.UnicodeUTF8))

