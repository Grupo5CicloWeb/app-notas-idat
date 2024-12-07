from PyQt5 import QtWidgets, uic
from repository.AlumnoRepository import AlumnoRepository
from repository.EspecialidadRepository import EspecialidadRepository
from PyQt5.QtWidgets import QTableWidgetItem
from model.Alumno import Alumno

class AlumnoController:

    def __init__(self) -> None:
        self.ventana = uic.loadUi("views/frmalumno.ui")
        self.objAlumnoRepository = AlumnoRepository()
        self.objEspecialidadRepository = EspecialidadRepository()
        self.ventana.tblalumnos.setColumnWidth(0,80)
        self.ventana.tblalumnos.setColumnWidth(2,150)
        self.ventana.tblalumnos.setColumnWidth(3,180)
        self.ventana.tblalumnos.setColumnWidth(4,70)
        self.listarEspecialidad()
        self.listarAlumnos()
        self.ventana.tblalumnos.cellClicked.connect(self.tblalumnoscellclick)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.ventana.btnlimpiar.clicked.connect(self.btnlimpiarclick)

    def btnguardarclick(self):
        idalumno = self.ventana.lblidalumno.text()
        nomalumno = self.ventana.txtnombres.text()
        apealumno = self.ventana.txtapellidos.text()
        idesp = self.ventana.cboespecialidad.currentData()
        proce = "N"
        if self.ventana.rbprivado.isChecked():
            proce = "P"
        objAlumno = Alumno(idalumno,nomalumno,apealumno,idesp,proce)
        if self.ventana.lblidalumno.isEnabled():
            self.objAlumnoRepository.insertarAlumno(objAlumno)
        else: 
            self.objAlumnoRepository.actualizarAlumno(objAlumno)
        self.listarAlumnos()
        self.limpiarFormulario()

    def btnlimpiarclick(self):
        self.limpiarFormulario()
    
    def tblalumnoscellclick(self, fila):
        idalumno = self.ventana.tblalumnos.item(fila, 0).text()
        self.ventana.lblidalumno.setText(idalumno)
        self.ventana.lblidalumno.setEnabled(False)
        objAlumno = self.objAlumnoRepository.buscarAlumnoXid(idalumno)
        self.ventana.txtnombres.setText(objAlumno[2])
        self.ventana.txtapellidos.setText(objAlumno[1])
        self.ventana.cboespecialidad.setCurrentText(objAlumno[3])
        if objAlumno[4] == "P":
            self.ventana.rbprivado.setChecked(True)
        else:
            self.ventana.rbestatal.setChecked(True)
    
    def limpiarFormulario(self):
        self.ventana.txtnombres.setText("")
        self.ventana.txtapellidos.setText("")
        self.ventana.lblidalumno.setText("")
        self.ventana.lblidalumno.setEnabled(True)
        self.ventana.cboespecialidad.setCurrentIndex(0)

    def listarAlumnos(self):
        alumnos = self.objAlumnoRepository.listarAlumnos()
        cantidad = len(alumnos)
        self.ventana.tblalumnos.setRowCount(cantidad)
        fila = 0
        for alumno in alumnos:
            self.ventana.tblalumnos.setItem(fila, 0, QTableWidgetItem(str(alumno[0])))
            self.ventana.tblalumnos.setItem(fila, 1, QTableWidgetItem(alumno[2]))
            self.ventana.tblalumnos.setItem(fila, 2, QTableWidgetItem(str(alumno[1])))

            self.ventana.tblalumnos.setItem(fila, 3, QTableWidgetItem(str(alumno[3])))
            self.ventana.tblalumnos.setItem(fila, 4, QTableWidgetItem(str(alumno[4])))                        
            fila +=1     

    def listarEspecialidad(self):
        especialidades = self.objEspecialidadRepository.listarEspecialidades()
        for especialidad in especialidades:
            self.ventana.cboespecialidad.addItem(
                especialidad[1], 
                especialidad[0])