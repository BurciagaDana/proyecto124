import sqlite3
from models.databaseModel import Database
from datetime import datetime

class UserController:
    def registrar_usuario(self, nombre, email, password):
        conn = Database.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO usuarios (nombre, email, password, fecha_registro)
                VALUES (?, ?, ?, ?)
            """, (nombre, email, password, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
            return True, "Usuario creado correctamente"
        except sqlite3.IntegrityError:
            return False, "El email ya está registrado"
        except Exception as e:
            return False, f"Error al registrar: {e}"
        finally:
            cursor.close()
            conn.close()

    def iniciar_sesion(self, email, password):
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, nombre FROM usuarios WHERE email=? AND password=?
        """, (email, password))
        usuario = cursor.fetchone()

        if usuario:
            cursor.execute("""
                UPDATE usuarios SET ultimo_inicio=? WHERE id=?
            """, (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), usuario[0]))
            conn.commit()
            cursor.close()
            conn.close()
            return True, {"id_usuario": usuario[0], "nombre": usuario[1]}
        else:
            cursor.close()
            conn.close()
            return False, "Email o contraseña incorrectos"
