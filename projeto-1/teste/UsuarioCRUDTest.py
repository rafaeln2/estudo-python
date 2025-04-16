from config.session import get_db
from config.engine import engine
from config.base import Base
from models.entities import Usuario, Curso, usuario_curso
from repository import UsuarioRepository, CursoRepository

def criar_base():
    Base.metadata.create_all(bind=engine)
    
    db_gen = get_db()
    db = next(db_gen)   
    insert_usuario(db)
    select_usuario_by_email(db)
    update_usuario(db)
    update_usuario_curso(db)

def insert_usuario(db):
    usuarios = (Usuario.Usuario(nome="Charles", email="charles@email.com"), Usuario.Usuario(nome="Samuel", email="samuel@email.com"), Usuario.Usuario(nome="Nicolas", email="nicolas@email.com"))
    crud = UsuarioRepository.UsuarioRepository(db)
    for usuario in usuarios:
        crud.insert(nome=usuario.nome, email=usuario.email, ativo=True)    
    
    usuarios_atualizados = crud.get_all_usuarios()
    print(f"Usuários inseridos com sucesso! ")
    print([usuario.nome for usuario in usuarios_atualizados])
    return usuario

def select_usuario_by_email(db) -> Usuario:
    usuarioCRUD = UsuarioRepository.UsuarioRepository(db)
    usuario = usuarioCRUD.get_usuario_by_email(email="charles@email.com")
    
    print(f"Usuário {usuario.nome} - {usuario.id} selecionado pelo email com sucesso!")
    
    return usuario

def select_usuario(db) -> Usuario:
    usuarioCRUD = UsuarioRepository.UsuarioRepository(db)
    usuario = usuarioCRUD.get_usuario_by_id(usuario_id=1)
    
    print(f"Usuário {usuario.nome} - {usuario.id} selecionado pelo email com sucesso!")
    
    return usuario

def update_usuario(db) :
    usuarioCRUD = UsuarioRepository.UsuarioRepository(db)
    usuario = usuarioCRUD.get_usuario_by_id(usuario_id=1)
    usuario.nome = "Charles Teste"
    usuario = usuarioCRUD.update_usuario(usuario_id=usuario.id, nome=usuario.nome)
    print(f"Usuário {usuario.nome} atualizado com sucesso!")
    return usuario

def update_usuario_curso(db) :
    usuarioCRUD = UsuarioRepository.UsuarioRepository(db)
    cursoCRUD = CursoRepository.CursoRepository(db)
    usuario = usuarioCRUD.get_usuario_by_id(usuario_id=1)
    curso = cursoCRUD.insert("Curso de python avançado")
    usuario = usuarioCRUD.adicionar_curso_ao_usuario(usuario_id=usuario.id, curso_id=curso.id)
    print(f"Curso {curso.nome} atualizado com sucesso!")
    print(f"Usuario possui {len(usuario.cursos)} cursos:")
    print([curso.nome for curso in usuario.cursos])
    
# def prepara_base(db: Session = Depends(get_db)):
#     Base.metadata.create_all(bind=engine)
#     print("Tabelas criadas com sucesso!")
    
if __name__ == "__main__":
    #GERA TABELA
    Base.metadata.create_all(bind=engine)
    
    db_gen = get_db()
    db = next(db_gen)   
    insert_usuario(db)
    select_usuario_by_email(db)
    update_usuario(db)
    update_usuario_curso(db)
    
    #DROPA BASE
    # Base.metadata.drop_all(engine)