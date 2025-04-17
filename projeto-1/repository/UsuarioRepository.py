from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from models.entities.Usuario import Usuario
from models.entities.Curso import Curso

class UsuarioRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def insert(self, nome: str, email: str, ativo: bool = True):
        usuario = Usuario(nome=nome, email=email, ativo=ativo)
        self.db.add(usuario)
        await self.db.commit()  # Commit deve ser assíncrono
        await self.db.refresh(usuario)  # Refresh também precisa ser aguardado
        return usuario

    async def get_usuario_by_id(self, usuario_id: int):
        result = await self.db.execute(select(Usuario).filter(Usuario.id == usuario_id))
        return result.scalars().first()

    async def get_all_usuarios(self, skip: int = 0, limit: int = 10):
        result = await self.db.execute(select(Usuario).offset(skip).limit(limit))
        return result.scalars().all()

    async def get_usuario_by_email(self, email: str):
        result = await self.db.execute(select(Usuario).filter(Usuario.email == email))
        return result.scalars().first()

    async def update_usuario(self, usuario_id: int, nome: str = None, email: str = None, ativo: bool = None):
        usuario = await self.get_usuario_by_id(usuario_id)
        if not usuario:
            return None
        if nome:
            usuario.nome = nome
        if email:
            usuario.email = email
        if ativo is not None:
            usuario.ativo = ativo

        await self.db.commit()  # Commit assíncrono
        await self.db.refresh(usuario)  # Refresh assíncrono
        return usuario

    async def delete_usuario(self, usuario_id: int):
        usuario = await self.get_usuario_by_id(usuario_id)
        if not usuario:
            return None

        # Limpa o vínculo com cursos antes de deletar
        usuario.cursos.clear()
        await self.db.commit()  # Commit assíncrono

        await self.db.delete(usuario)  # Deletar usuário
        await self.db.commit()  # Commit assíncrono
        return usuario

    async def adicionar_curso_ao_usuario(self, usuario_id: int, curso_id: int):
        usuario = await self.get_usuario_by_id(usuario_id)
        curso = await self.db.execute(select(Curso).filter(Curso.id == curso_id))
        curso = curso.scalars().first()

        if usuario and curso and curso not in usuario.cursos:
            usuario.cursos.append(curso)
            await self.db.commit()  # Commit assíncrono
            await self.db.refresh(usuario)  # Refresh assíncrono
        return usuario

    async def remover_curso_do_usuario(self, usuario_id: int, curso_id: int):
        usuario = await self.get_usuario_by_id(usuario_id)
        if not usuario:
            return None

        usuario.cursos = [c for c in usuario.cursos if c.id != curso_id]
        await self.db.commit()  # Commit assíncrono
        return usuario
