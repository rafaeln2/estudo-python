from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from config.session import get_db
from config.schemas import UsuarioCreate, UsuarioUpdate, UsuarioOut
from models import Usuario, Curso, usuario_curso
from repository import UsuarioRepository
from typing import List
from teste.UsuarioCRUDTest import criar_base


router = APIRouter()

@router.get("/cursos")
def listar_cursos(db: Session = Depends(get_db)):
    return UsuarioRepository.UsuarioRepository(db).get_all_cursos()

@router.get("/teste")
def teste():
    return {"descricao": "Curso teste API"}

