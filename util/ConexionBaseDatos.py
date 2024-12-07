import mysql.connector

class ConexionBaseDatos:

    def __init__(self) -> None:
        self.conexion = mysql.connector.connect(host='localhost', 
                                                database='bdnotas',
                                                user='root',
                                                password='123456')
    def getConexion(self):
        return self.conexion

