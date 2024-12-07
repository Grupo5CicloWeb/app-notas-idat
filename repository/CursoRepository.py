from util.ConexionBaseDatos import ConexionBaseDatos

class CursoRepository:

    def __init__(self) -> None:
        self.conexion = ConexionBaseDatos().getConexion()
    

    def listarCursos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM curso ORDER BY idcurso DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def obtenerCursoxId(self, idcurso):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM curso WHERE idcurso = '{}'".format(idcurso)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarCurso(self, curso):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO curso (nomcurso,credito) VALUES ('{}', '{}')".format(
            curso.nomcurso, curso.credito)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarCurso(self, curso):
        cursor = self.conexion.cursor()
        sql = "UPDATE curso SET nomcurso='{}', credito='{}' WHERE idcurso='{}'".format(
            curso.nomcurso, curso.credito, curso.idcurso)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
        