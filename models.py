from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from database import Base
from datetime import datetime, timezone


class Usuario(Base): 
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    contrasena = Column(String, nullable=False)
    rol = Column(String, default="user")
    
class Pomodoro(Base): 
    __tablename__ = "pomodoros"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), index=True, nullable=False)
    fecha = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    tag = Column(String, nullable=False)
    pausas = Column(Integer, nullable=False, default=0)
    tiempo_excedido = Column(Integer, nullable=False, default=0)
    
class Tag(Base): 
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), index=True, nullable=False)
    nombre_tag = Column(String, nullable=False)
    
