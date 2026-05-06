from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UsuariosSchema(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)


    
class TareaSchema(BaseModel):
    titulo: str = Field(min_length=1, max_lenght=200)
    descripcion: Optional[str]= None
    prioridad: str = "media"
    clasificacion: str = "personal"    

class UsuarioAlta(BaseModel):
    nombre: str = Field(min_lenght= 3, max_length=100)
    apellido: str = Field(min_length=3, max_lenght=20)
    email: EmailStr
    activo: bool = True
    password: str = Field(min_length=8)
    fecha_registro: datetime = Field(default_factory=datetime.now)
    ultimo_ingreso: datetime = Field(default_factory=datetime.now)
