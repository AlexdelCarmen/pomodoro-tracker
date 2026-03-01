from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioClear(BaseModel):
    nombre: str
    email: EmailStr
    contrasena: str
    
class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    rol: str
    
    class Config: 
        from_attributes = True
        
class TagClear(BaseModel):
    nombre_tag: str

class TagResponse(BaseModel):
    id: int
    nombre_tag: str
    
    class Config: 
        from_attributes = True

class PomodoroClear(BaseModel):
    tag: str
    pausas: int
    tiempo_excedido: int
    
class PomodoroResponse(BaseModel):
    id: int
    usuario_id: int
    fecha: datetime
    tag: str
    pausas: int
    tiempo_excedido: int
    
    class Config: 
        from_attributes = True