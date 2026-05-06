import sqlite3
import os

class Database:
    @staticmethod
    def get_connection():
        DB_PATH = os.path.join(os.path.dirname(__file__), "../../data/mi_base.db")
        return sqlite3.connect(DB_PATH)

    @staticmethod
    def create_tables():
        conn = Database.get_connection()
        cursor = conn.cursor()

        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                fecha_registro TEXT DEFAULT CURRENT_TIMESTAMP,
                ultimo_inicio TEXT
            )
        """)

        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                prioridad TEXT,
                clasificacion TEXT,
                estado TEXT DEFAULT 'pendiente',
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
            )
        """)

        conn.commit()
        cursor.close()
        conn.close()
