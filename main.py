from fastapi import FastAPI
from database import engine
import models, schemas
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from passlib.context import CryptContext


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db(): 
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()

@app.get("/")
def root():
    return {"mensaje": "Borcho Focus API"}

@app.post("/usuarios", response_model=schemas.UsuarioResponse)
def crear_usuario(usuario: schemas.UsuarioClear, db: Session = Depends(get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    contrasena_hash = pwd_context.hash(usuario.contrasena)
    nuevo_usuario = models.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        contrasena=contrasena_hash
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

    