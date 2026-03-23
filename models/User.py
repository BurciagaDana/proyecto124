import bcrypt
from .database import Database

class UsuarioModel:
    def _init_(self):
        self.db = Database()
        
        def registrar(self, usuario_data):
            #Encriptar contraseña
            salt = bcrypt.gensalt()
            hashed_pw = bcrypt.hashpw(usuario_data.password.encode())