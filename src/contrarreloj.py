#!/usr/bin/env python2
# -*- coding: utf-8 -*-

########################################################################
#
#    This file is part of Contrarreloj.
#
#    Contrarreloj is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Contrarreloj is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Contrarreloj.  If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

'''
Created on Dec 15, 2010

@author: Ruben Guerra Marin
'''

import sys, datetime
from PyQt4 import QtCore, QtGui
import sqlite3 as dbapi
from ventanaprincipal import Ui_ventanaprincipal
from ventanaajustes import Ui_ventanaAjustes
from ventanallenar import Ui_ventanallenar
from ventanaresultados import Ui_ventanaresultados
from ventanaregistro import Ui_ventanaregistro
from ventanaabout import Ui_ventanaabout
from os import mkdir
import subprocess
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class ventanaprincipal(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ventanaprincipal()
        self.ui.setupUi(self)
        self.iniciado = 0
        self.base_datos = dbapi.connect("contrarreloj.rgm")
        self.cursor = self.base_datos.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS registro (id INTEGER NOT NULL PRIMARY KEY, licencia TEXT, nombre TEXT, equipo TEXT, categoria TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tiempos (id INTEGER NOT NULL PRIMARY KEY, numeroparticipante INTEGER, tiempoparcial INTEGER, tiemporeal INTEGER)")
        self.contador = 0
        self.contador2 = 0
        self.cadacuanto = [0]
        self.cursor.execute("SELECT * FROM registro")
        for row in self.cursor:
            self.contador2 = self.contador2 + 1
        self.ui.lcdtotalparcicipantes.display(self.contador2)
        self.cursor.execute("SELECT * FROM tiempos")
        for row in self.cursor:
            self.contador = self.contador + 1
        self.ui.lcdllegaron.display(self.contador)
        self.listadecategorias = []
        self.connect(self.ui.botonIniciar, QtCore.SIGNAL("clicked()"), self.iniciarreloj)
        self.connect(self.ui.botonCortar, QtCore.SIGNAL("clicked()"), self.cortarreloj)
        self.connect(self.ui.botonborrarultimo, QtCore.SIGNAL("clicked()"), self.borrarultimo)
        self.connect(self.ui.actionRegistro, QtCore.SIGNAL("triggered()"), self.ventanaregistro)
        self.connect(self.ui.actionAjustes_principales, QtCore.SIGNAL("triggered()"), self.ventanaajustes)
        self.connect(self.ui.actionLlenar_numeros, QtCore.SIGNAL("triggered()"), self.ventanallenar)
        self.connect(self.ui.actionResultados, QtCore.SIGNAL("triggered()"), self.ventanaresultados)
        self.connect(self.ui.actionAcerca_de, QtCore.SIGNAL("triggered()"), self.ventanaabout)
        self.connect(self.ui.actionAcerca_de_QT, QtCore.SIGNAL("triggered()"), self.acercadeqt)
        self.connect(self.ui.actionSalir, QtCore.SIGNAL("triggered()"), self.salir)

    def ventanaregistro(self):
        self.vregistro = ventanaregistro(self.base_datos, self.ui.lcdtotalparcicipantes, self.listadecategorias)
        self.vregistro.show()

    def ventanaajustes(self):
        self.vajustes = ventanaAjustes(self.listadecategorias, self.cadacuanto)
        self.vajustes.show()
    
    def iniciarreloj(self):
        if self.iniciado == 0:
            self.cronometroreal = QtCore.QTime()
            self.cronometroreal.start()
            self.ctimer = QtCore.QTimer()
            self.ctimer.setInterval(1)
            self.ctimer.start()
            self.connect(self.ctimer, QtCore.SIGNAL("timeout()"), self.actualizarreloj)
            self.iniciado = 1
        elif self.iniciado == 1:
            mensaje = QtGui.QMessageBox.question(self, 'Mensaje', u"¿Estás seguro que deseas parar el reloj?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if mensaje == QtGui.QMessageBox.Yes: 
                self.ctimer.stop()
                self.iniciado = 0
        
    def actualizarreloj(self):
        self.ui.labelTiempo.setText(str(datetime.timedelta(milliseconds=self.cronometroreal.elapsed())).rstrip('0'))
    
    def cortarreloj(self):
        tupla = (self.contador + 1, self.cronometroreal.elapsed(),)
        self.cursor.execute("INSERT INTO tiempos (id, tiempoparcial) VALUES (?,?)", tupla)
        self.base_datos.commit()
        self.contador = self.contador + 1
        self.ui.lcdllegaron.display(self.contador)
        
    def borrarultimo(self):
        self.cursor.execute("DELETE FROM tiempos WHERE id=?", (self.contador,))
        self.contador = self.contador - 1
        self.ui.lcdllegaron.display(self.contador)
                
    def ventanallenar(self):
        try:
            self.vllenar = ventanallenar(self.base_datos, self.contador, self.cadacuanto[0])
            self.vllenar.show()
        except AttributeError:
            QtGui.QMessageBox.warning(self, "Aviso", "Los ajustes se deben de llenar primero")
        
    def ventanaresultados(self):
        self.vresultados = ventanaresultados(self.base_datos, self.contador, self.listadecategorias)
        self.vresultados.show()
        
    def ventanaabout(self):
        self.vabout = ventanaabout()
        self.vabout.show()
        
    def acercadeqt(self):
        QtGui.QMessageBox.aboutQt(self)
        
    def salir(self):
        self.close()
        
    def closeEvent(self, event):
        respuesta = QtGui.QMessageBox.question(self, 'Mensaje', u"¿Estás seguro que deseas salir?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if respuesta == QtGui.QMessageBox.Yes:
            try:
                self.vabout.close()
            except AttributeError:
                print "ventana about no abierta"
            try:
                self.vajustes.close()
            except AttributeError:
                print "ventana ajustes no abierta"
            try:
                self.vregistro.close()
            except AttributeError:
                print "ventana registro no abierta"
            try:
                self.vresultados.close()
            except AttributeError:
                print "ventana resultados no abierta"
            try:
                self.vllenar.close()
            except AttributeError:
                print "ventana llenar no abierta"
            event.accept()
        else:
            event.ignore()

class ventanaAjustes(QtGui.QWidget):
    def __init__(self, listacat, cadaCuanto, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ventanaAjustes()
        self.ui.setupUi(self)
        self.listadecategorias = listacat
        self.cadacuanto = cadaCuanto
        self.ui.textoCadacuanto.setText(str(self.cadacuanto[0]/1000))
        for categoria in self.listadecategorias:
            item = QtGui.QListWidgetItem(categoria)
            self.ui.listacategorias.addItem(item)
        QtCore.QObject.connect(self.ui.textoCadacuanto, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.accept)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        self.connect(self.ui.botonagregar, QtCore.SIGNAL("clicked()"), self.agregarcategoria)
        self.connect(self.ui.botonremover, QtCore.SIGNAL("clicked()"), self.removercategoria)
        
    def agregarcategoria(self):
        if self.ui.textocategoria.text():
            item = QtGui.QListWidgetItem(self.ui.textocategoria.text())
            self.ui.listacategorias.addItem(item)
            self.listadecategorias.append(self.ui.textocategoria.text())
            self.ui.textocategoria.setText("")
        self.ui.textocategoria.setFocus(True)

    def removercategoria(self):
        quitado = self.ui.listacategorias.takeItem(self.ui.listacategorias.currentRow())
        self.listadecategorias.remove(quitado.text())

    def accept(self):
        try:
            if int(self.ui.textoCadacuanto.text()) >= 0:
                self.cadacuanto[0] = int(self.ui.textoCadacuanto.text())*1000
                self.close()
            else:
                QtGui.QMessageBox.warning(self, "Aviso", u"El número debe de ser 0 o mayor a 0")
        except ValueError:
            QtGui.QMessageBox.warning(self, "Aviso", u"Sólo se permiten números")

    def reject(self):
        self.close()
        
    def closeEvent(self, event):
        self.listadecategorias.sort()

class ventanaregistro(QtGui.QWidget):
    def __init__(self, base_de_datos, lcdtotalparticipantes, listacat, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ventanaregistro()
        self.ui.setupUi(self)
        self.lcdtotal = lcdtotalparticipantes
        self.base_datos = base_de_datos
        self.cursor = self.base_datos.cursor()
        self.contador = 1
        self.listadecategorias = listacat
        print self.listadecategorias
        self.ui.cajacategorias.addItems(self.listadecategorias)
        self.cursor.execute("SELECT * FROM registro")
        for row in self.cursor:
            self.items = QtGui.QTreeWidgetItem([str(row[0]), str(row[1]), str(row[2]), str(row[2]), str(row[3])])
            self.ui.treearbol.addTopLevelItem(self.items)
            self.contador = self.contador + 1
        self.ui.textonumero.setText(str(self.contador))
        self.connect(self.ui.botonagregar, QtCore.SIGNAL("clicked()"), self.guardar)
        self.connect(self.ui.botonretirar, QtCore.SIGNAL("clicked()"), self.retirar)
        
    def guardar(self):
        self.numero = self.ui.textonumero.text()
        self.licencia = self.ui.textolicencia.text()
        self.nombre = self.ui.textonombre.text()
        self.equipo = self.ui.textoequipo.text()
        self.categoria = self.ui.cajacategorias.currentText()
        if self.contador and self.licencia and self.numero and self.nombre and self.equipo:
            self.items = QtGui.QTreeWidgetItem([self.numero, self.licencia, self.nombre, self.equipo, self.categoria])
            self.tupla = (str(self.contador), str(self.licencia), str(self.nombre), str(self.equipo), str(self.categoria))
            self.cursor.execute("INSERT INTO registro (id, licencia, nombre, equipo, categoria) VALUES (?,?,?,?,?)",self.tupla)
            self.base_datos.commit()
            self.ui.treearbol.addTopLevelItem(self.items)
            self.contador = self.contador + 1
            self.ui.textonumero.setText(str(self.contador))
            self.ui.textolicencia.setText("")
            self.ui.textonombre.setText("")
            self.ui.textoequipo.setText("")
            self.ui.treearbol.sortItems(0, 1)
            self.lcdtotal.display(self.contador-1)
            self.cursor.execute("SELECT * FROM registro")
            for row in self.cursor:
                print str(row)
        else:
            QtGui.QMessageBox.warning(self, "Aviso", u"No se permiten elementos vacíos")
        self.ui.textolicencia.setFocus(True) 
          
    def retirar(self):
        self.ui.treearbol.takeTopLevelItem(0)
        self.contador = self.contador - 1
        self.cursor.execute("DELETE FROM registro WHERE id=?", (self.contador,))
        self.base_datos.commit()
        self.ui.textonumero.setText(str(self.contador))
        self.ui.textolicencia.setFocus(True)
        self.lcdtotal.display(self.contador-1)
        
class ventanallenar(QtGui.QWidget):
    def __init__(self,  base_de_datos, total, cadacuantotiempo, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ventanallenar()
        self.ui.setupUi(self)
        self.base_datos = base_de_datos
        self.cursor = self.base_datos.cursor()
        self.cadacuanto = cadacuantotiempo
        self.contador = 1
        self.totalparticipantes = total
        if self.totalparticipantes < 1:
            self.ui.textoid.setText("No hay nadie")
        else:
            self.ui.textoid.setText(str(self.contador))
        self.connect(self.ui.botonagregar, QtCore.SIGNAL("clicked()"), self.rellenar)
           
    def rellenar(self):
        try:
            if int(self.ui.textoid.text()) <= self.totalparticipantes and int(self.ui.textocorredor.text()) <= self.totalparticipantes:
                self.cursor.execute("SELECT tiempoparcial FROM tiempos WHERE id=?",(int(self.ui.textoid.text()),))
                self.tiempoparcial = self.cursor.fetchone()[0]
                self.tiemporeal = self.tiempoparcial - ((int(self.ui.textocorredor.text())-1)*self.cadacuanto)
                self.tupla = (int(self.ui.textocorredor.text()), int(self.tiemporeal), int(self.ui.textoid.text()))
                self.cursor.execute("UPDATE tiempos SET numeroparticipante=?, tiemporeal=? WHERE id=?", self.tupla)
                self.base_datos.commit()
                if self.contador >= self.totalparticipantes and self.contador == int(self.ui.textoid.text()):
                    self.ui.textoid.setText("Ya son todos")
                else:
                    if self.contador == int(self.ui.textoid.text()):
                        self.contador = self.contador+1
                    self.ui.textoid.setText(str(self.contador))
                    self.ui.textocorredor.setText("")
                self.cursor.execute("SELECT * FROM tiempos")
                for row in self.cursor:
                    print row
            else:
                QtGui.QMessageBox.warning(self, "Aviso", u"El número de corredor es mayor a los corredores que llegaron")
        except ValueError:
            QtGui.QMessageBox.warning(self, "Aviso", u"Sólo se permiten números")

class ventanaresultados(QtGui.QWidget):
    def __init__(self, base_de_datos, totalparticipantes, listacat, parent=None):
        QtGui.QWidget.__init__(self, parent)
        try:
            mkdir ("resultados")
        except OSError:
            print "el directorio ya existe"
        self.ui = Ui_ventanaresultados()
        self.ui.setupUi(self)
        self.base_datos = base_de_datos
        self.totalparticipantes = totalparticipantes
        self.contador = 1
        self.cursor = self.base_datos.cursor()
        self.cursor2 = self.base_datos.cursor()
        self.listadecategorias = listacat
        self.PATH = "resultados"
        self.ui.cajacategorias.addItems(self.listadecategorias)
        self.connect(self.ui.cajacategorias, QtCore.SIGNAL("currentIndexChanged(QString)"), self.actualizarresultados)
        self.connect(self.ui.botonresultados, QtCore.SIGNAL("clicked()"), self.abrirresultados)
        self.ui.treeresultados.setSortingEnabled(True)
        self.mostrarresultados()
        self.resultadosporcategoria()
        
    def mostrarresultados(self):
        self.archivo = open(os.path.join(self.PATH, "Generales.txt"), "w")
        self.archivo.write("Resultados Generales\n\n")
        self.archivo.write("%-7s %-15s %-9s %-30s %-30s %s \n\n" %  ("Lugar", "Tiempo", "Número", "Nombre", "Equipo", "Categoría"))
        self.cursor2.execute("SELECT numeroparticipante, tiemporeal FROM tiempos ORDER BY tiemporeal")
        for row in self.cursor2:
            self.cursor.execute("SELECT nombre, equipo, categoria FROM registro WHERE id=?",(row[0],))
            for row2 in self.cursor:
                print self.contador, row[1], row[0], row2[0], row2[1], row2[2]
                self.archivo.write("%-7s %-15s %-8s %-30s %-30s %s \n" %  (str(self.contador), str(datetime.timedelta(milliseconds=row[1])).rstrip('0'), str(row[0]), str(row2[0]), str(row2[1]), str(row2[2])))
                self.items = QtGui.QTreeWidgetItem([str(self.contador), str(datetime.timedelta(milliseconds=row[1])).rstrip('0'), str(row[0]), str(row2[0]), str(row2[1]), str(row2[2])])
                self.ui.treeresultados.addTopLevelItem(self.items)
            self.contador = self.contador + 1
        self.archivo.close()
        
    def actualizarresultados(self):
        self.ui.treeresultados.clear()
        self.contador = 1
        if self.ui.cajacategorias.currentText() == "Generales":
            self.mostrarresultados()
        else:
            categoria = self.ui.cajacategorias.currentText()
            self.cursor2.execute("SELECT numeroparticipante, tiemporeal FROM tiempos ORDER BY tiemporeal")
            for row in self.cursor2:
                self.cursor.execute("SELECT nombre, equipo, categoria FROM registro WHERE id=? AND categoria=?",(row[0],str(categoria)))
                for row2 in self.cursor:
                    self.items = QtGui.QTreeWidgetItem([str(self.contador), str(datetime.timedelta(milliseconds=row[1])).rstrip('0'), str(row[0]), str(row2[0]), str(row2[1]), str(row2[2])])
                    self.ui.treeresultados.addTopLevelItem(self.items)
                    self.contador = self.contador + 1
        
    def resultadosporcategoria(self):
        for categoria in self.listadecategorias:
            self.contador = 1
            self.archivo = open(os.path.join(self.PATH, "%s.txt" % categoria), "w")
            self.archivo.write("Resultados de %s\n\n" % categoria)
            self.archivo.write("%-7s %-15s %-9s %-30s %s \n\n" %  ("Lugar", "Tiempo", "Número", "Nombre", "Equipo"))
            self.cursor2.execute("SELECT numeroparticipante, tiemporeal FROM tiempos ORDER BY tiemporeal")
            for row in self.cursor2:
                self.cursor.execute("SELECT nombre, equipo FROM registro WHERE id=? AND categoria=?",(row[0],str(categoria)))
                for row2 in self.cursor:
                    self.archivo.write("%-7s %-15s %-8s %-30s %s \n" %  (str(self.contador), str(datetime.timedelta(milliseconds=row[1])).rstrip('0'), str(row[0]), str(row2[0]), str(row2[1])))
                    self.contador = self.contador + 1
            self.archivo.close()
            
    def abrirresultados(self):
        categoria = self.ui.cajacategorias.currentText()
        if "posix" is os.name:
            subprocess.call (["xdg-open", os.path.join(self.PATH, "%s.txt" % categoria)])
        elif "nt" is os.name:
            subprocess.call (["notepad", os.path.join(self.PATH, "%s.txt" % categoria)])
        else:
            print "no soportado"
                     
class ventanaabout(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ventanaabout()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ventana = ventanaprincipal()
    ventana.show()
    sys.exit(app.exec_())