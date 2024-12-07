from PyQt5 import QtWidgets, uic
from controller.CursoController import CursoController
from controller.AlumnoController import AlumnoController

class PrincipalController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("views/menuprincipal.ui")
        self.ventana.show()
        self.ventana.actionCurso.triggered.connect(self.actionCursoClick)
        self.ventana.actionAlumno.triggered.connect(self.actionAlumnoClick)
        app.exec()

    def actionCursoClick(self):
        self.frmcurso = CursoController()
        self.frmcurso.ventana.show()
    
    def actionAlumnoClick(self):
        self.frmalumno = AlumnoController()
        self.frmalumno.ventana.show()