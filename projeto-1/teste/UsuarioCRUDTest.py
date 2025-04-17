import asyncio
from config.session import get_db
from config.engine import engine
from config.base import Base
from models.entities import Usuario, Curso
from repository import UsuarioRepository, CursoRepository
from sqlalchemy.ext.asyncio import AsyncSession

async def criar_base():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async for db in get_db():
        print("entrou no inserts do teste")
        await insert_usuario(db)
        await select_usuario_by_email(db)
        await update_usuario(db)
        await update_usuario_curso(db)

async def insert_usuario(db: AsyncSession):
    usuarios = (
        Usuario.Usuario(nome="Charles", email="charles@email.com"),
        Usuario.Usuario(nome="Samuel", email="samuel@email.com"),
        Usuario.Usuario(nome="Nicolas", email="nicolas@email.com"),
    )
    crud = UsuarioRepository.UsuarioRepository(db)
    for usuario in usuarios:
        await crud.insert(nome=usuario.nome, email=usuario.email, ativo=True)

    usuarios_atualizados = await crud.get_all_usuarios()
    print("Usuários inseridos com sucesso!")
    print([usuario.nome for usuario in usuarios_atualizados])
    return usuarios_atualizados

async def select_usuario_by_email(db: AsyncSession) -> Usuario.Usuario:
    usuario_crud = UsuarioRepository.UsuarioRepository(db)
    usuario = await usuario_crud.get_usuario_by_email(email="charles@email.com")

    print(f"Usuário {usuario.nome} - {usuario.id} selecionado pelo email com sucesso!")
    return usuario

async def select_usuario(db: AsyncSession) -> Usuario.Usuario:
    usuario_crud = UsuarioRepository.UsuarioRepository(db)
    usuario = await usuario_crud.get_usuario_by_id(usuario_id=1)

    print(f"Usuário {usuario.nome} - {usuario.id} selecionado com sucesso!")
    return usuario

async def update_usuario(db: AsyncSession):
    usuario_crud = UsuarioRepository.UsuarioRepository(db)
    usuario = await usuario_crud.get_usuario_by_id(usuario_id=1)
    usuario.nome = "Charles Teste"
    usuario = await usuario_crud.update_usuario(usuario_id=usuario.id, nome=usuario.nome)
    print(f"Usuário {usuario.nome} atualizado com sucesso!")
    return usuario

async def update_usuario_curso(db: AsyncSession):
    usuario_crud = UsuarioRepository.UsuarioRepository(db)
    curso_crud = CursoRepository.CursoRepository(db)

    usuario = await usuario_crud.get_usuario_by_id(usuario_id=1)
    curso = await curso_crud.insert("Curso de python avançado")
    usuario = await usuario_crud.adicionar_curso_ao_usuario(usuario_id=usuario.id, curso_id=curso.id)

    print(f"Curso {curso.nome} vinculado com sucesso!")
    print(f"Usuário possui {len(usuario.cursos)} cursos:")
    print([curso.nome for curso in usuario.cursos])

# Rodar como script
if __name__ == "__main__":
    asyncio.run(criar_base())

# if __name__ == "__main__":
#     #GERA TABELA
#     Base.metadata.create_all(bind=engine)
    
#     db_gen = get_db()
#     db = next(db_gen)   
#     insert_usuario(db)
#     select_usuario_by_email(db)
#     update_usuario(db)
#     update_usuario_curso(db)
    
    
#DROPA BASE
#     Base.metadata.drop_all(engine)