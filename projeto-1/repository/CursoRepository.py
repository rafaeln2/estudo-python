from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.entities.Curso import Curso
from models.entities.Usuario import Usuario

class CursoRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def insert(self, nome: str):
        curso = Curso(nome=nome)
        self.db.add(curso)
        await self.db.commit()
        await self.db.refresh(curso)
        return curso

    async def get_curso_by_id(self, curso_id: int):
        result = await self.db.execute(select(Curso).filter(Curso.id == curso_id))
        return result.scalars().first()

    async def get_all_cursos(self, skip: int = 0, limit: int = 10):
        result = await self.db.execute(select(Curso).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, curso_id: int, nome: str):
        curso = await self.get_curso_by_id(curso_id)
        if not curso:
            return None
        curso.nome = nome
        await self.db.commit()
        await self.db.refresh(curso)
        return curso

    async def delete(self, curso_id: int):
        curso = await self.get_curso_by_id(curso_id)
        if not curso:
            return None

        # Remove vínculo com usuários
        curso.usuarios.clear()
        await self.db.commit
