from PyQt5 import QtWidgets, uic
from repository.CursoRepository import CursoRepository
from PyQt5.QtWidgets import QTableWidgetItem
from model.Curso import Curso
class CursoController:

    def __init__(self) -> None:
        self.objCursoRepository = CursoRepository()
        self.ventana = uic.loadUi("views/frmcurso.ui")
        self.ventana.tblcurso.cellClicked.connect(self.tblcursocellclick)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.ventana.btnlimpiar.clicked.connect(self.btnlimpiarclick)
        self.listarCursos()
    
    def btnlimpiarclick(self):
        self.limpiarFormulario()

    def limpiarFormulario(self):
        self.ventana.txtnombre.setText("")
        self.ventana.txtcredito.setText("")
        self.ventana.lblidcurso.setText("")
        self.ventana.lblidcurso.setEnabled(True)
    
    def btnguardarclick(self):
        idcurso = self.ventana.lblidcurso.text()
        nomcurso = self.ventana.txtnombre.text()
        credcurso = self.ventana.txtcredito.text()
        nuevoCurso = Curso(idcurso, nomcurso, credcurso)
        if self.ventana.lblidcurso.isEnabled():
            self.objCursoRepository.insertarCurso(nuevoCurso)
        else:
            self.objCursoRepository.actualizarCurso(nuevoCurso)
        self.listarCursos()
        self.limpiarFormulario()
    
    def tblcursocellclick(self, fila):
        idcurso = self.ventana.tblcurso.item(fila, 0).text()
        self.ventana.lblidcurso.setText(idcurso)
        self.ventana.lblidcurso.setEnabled(False)
        objCurso = self.objCursoRepository.obtenerCursoxId(idcurso)        
        self.ventana.txtnombre.setText(objCurso[1])
        self.ventana.txtcredito.setText(str(objCurso[2]))
   
    def listarCursos(self):
        listaCursos = self.objCursoRepository.listarCursos()
        cantidad = len(listaCursos)
        self.ventana.tblcurso.setRowCount(cantidad)
        fila = 0
        for curso in listaCursos:
            self.ventana.tblcurso.setItem(fila, 0, QTableWidgetItem(str(curso[0])))
            self.ventana.tblcurso.setItem(fila, 1, QTableWidgetItem(curso[1]))
            self.ventana.tblcurso.setItem(fila, 2, QTableWidgetItem(str(curso[2])))
            fila +=1