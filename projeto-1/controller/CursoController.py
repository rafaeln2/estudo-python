from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.session import get_db
from repository import UsuarioRepository

router = APIRouter()

@router.get("/cursos")
async def listar_cursos(db: AsyncSession = Depends(get_db)):
    crud = UsuarioRepository.UsuarioRepository(db)
    cursos = await crud.get_all_cursos()  # Você precisa ter esse método async no repositório
    return cursos

@router.get("/teste")
async def teste():
    return {"descricao": "Curso teste API"}

