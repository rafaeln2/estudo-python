from sqlalchemy.orm import Session
import models.entities.Usuario 
import models.entities.Curso

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def insert(self, nome: str, email: str, ativo: bool = True):
        usuario = Usuario(nome=nome, email=email, ativo=ativo)
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)

        return usuario

    def get_usuario_by_id(self, usuario_id: int):
        return self.db.query(Usuario).filter(Usuario.id == usuario_id).first()

    def get_all_usuarios(self, skip: int = 0, limit: int = 10):
        return self.db.query(Usuario).offset(skip).limit(limit).all()

    def get_usuario_by_email(self, email: str):
        return self.db.query(Usuario).filter(Usuario.email == email).first()

    def update_usuario(self, usuario_id: int, nome: str = None, email: str = None, ativo: bool = None):
        usuario = self.get_usuario_by_id(usuario_id)
        if not usuario:
            return None
        if nome:
            usuario.nome = nome
        if email:
            usuario.email = email
        if ativo is not None:
            usuario.ativo = ativo

        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def delete_usuario(self, usuario_id: int):
        usuario = self.get_usuario_by_id(usuario_id)
        if not usuario:
            return None

        # Limpa o vínculo com cursos antes de deletar
        usuario.cursos.clear()
        self.db.commit()

        self.db.delete(usuario)
        self.db.commit()
        return usuario

    def adicionar_curso_ao_usuario(self, usuario_id: int, curso_id: int):
        usuario = self.get_usuario_by_id(usuario_id)
        curso = self.db.query(Curso).filter(Curso.id == curso_id).first()

        if usuario and curso and curso not in usuario.cursos:
            usuario.cursos.append(curso)
            self.db.commit()
            self.db.refresh(usuario)
        return usuario

    def remover_curso_do_usuario(self, usuario_id: int, curso_id: int):
        usuario = self.get_usuario_by_id(usuario_id)
        if not usuario:
            return None

        usuario.cursos = [c for c in usuario.cursos if c.id != curso_id]
        self.db.commit()
        return usuario
