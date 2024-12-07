from util.ConexionBaseDatos import ConexionBaseDatos

class AlumnoRepository:

    def __init__(self) -> None:
        self.conexion = ConexionBaseDatos().getConexion()
    
    def listarAlumnos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT a.IdAlumno, a.ApeAlumno, a.NomAlumno, e.NomEsp, a.Proce FROM alumno a INNER JOIN especialidad e ON a.idesp = e.idesp ORDER BY a.idalumno DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarAlumnoxNombre(self, nombre):
        cursor = self.conexion.cursor()
        sql = "SELECT a.IdAlumno, a.ApeAlumno, a.NomAlumno, e.NomEsp, a.Proce FROM alumno a INNER JOIN especialidad e ON a.idesp = e.idesp WHERE nomalumno like '{}%' ORDER BY a.idalumno DESC".format(nombre)
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarAlumnoXid(self, idalumno):
        cursor = self.conexion.cursor()
        sql = "SELECT a.IdAlumno, a.ApeAlumno, a.NomAlumno, e.NomEsp, a.Proce FROM alumno a INNER JOIN especialidad e ON a.idesp = e.idesp WHERE a.idalumno='{}' ORDER BY a.idalumno DESC".format(idalumno)
        cursor.execute(sql)
        return cursor.fetchone()

    def insertarAlumno(self, alumno):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO alumno (nomalumno,apealumno,idesp,proce) VALUES ('{}', '{}','{}', '{}')".format(
            alumno.nomalumno, alumno.apealumno, alumno.especialidad, alumno.proce)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()    

    def actualizarAlumno(self, alumno):
        cursor = self.conexion.cursor()
        sql = "UPDATE alumno SET nomalumno='{}', apealumno='{}', idesp='{}', proce='{}' WHERE idalumno='{}'".format(
            alumno.nomalumno, alumno.apealumno, alumno.especialidad, alumno.proce, alumno.idalumno)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()