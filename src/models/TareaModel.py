import sqlite3
from .databaseModel import Database

class TareaModel: 
    def __init__(self):
        self.db = Database()

    def listar_por_usuario(self, id_usuario):
        conn = self.db.get_connection()
        conn.row_factory = sqlite3.Row  # permite acceder a columnas por nombre
        cursor = conn.cursor()
        query = "SELECT id, titulo, descripcion, prioridad, clasificacion, estado FROM tareas WHERE id_usuario = ? ORDER BY id ASC"
        cursor.execute(query, (id_usuario,))
        resultado = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return resultado
    
    def crear(self, id_usuario, titulo, descripcion, prioridad, clasificacion):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO tareas (id_usuario, titulo, descripcion, prioridad, clasificacion, estado) 
                   VALUES (?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (id_usuario, titulo, descripcion, prioridad, clasificacion, "pendiente"))
        conn.commit()
        conn.close()
