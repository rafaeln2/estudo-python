from sqlalchemy.orm import Session
from models.entities import Curso, Usuario


class CursoRepository:
    def __init__(self, db: Session):
        self.db = db

    def insert(self, nome: str):
        curso = Curso(nome=nome)
        self.db.add(curso)
        self.db.commit()
        self.db.refresh(curso)
        return curso

    def get_curso_by_id(self, curso_id: int):
        return self.db.query(Curso).filter(Curso.id == curso_id).first()

    def get_all_cursos(self, skip: int = 0, limit: int = 10):
        return self.db.query(Curso).offset(skip).limit(limit).all()

    def update(self, curso_id: int, nome: str):
        curso = self.get_curso_by_id(curso_id)
        if not curso:
            return None
        curso.nome = nome
        self.db.commit()
        self.db.refresh(curso)
        return curso

    def delete(self, curso_id: int):
        curso = self.get_curso_by_id(curso_id)
        if not curso:
            return None

        # Remove vínculo com usuários
        curso.usuarios.clear()
        self.db.commit()

        self.db.delete(curso)
        self.db.commit()
        return curso

    def adicionar_usuario_ao_curso(self, curso_id: int, usuario_id: int):
        curso = self.get_curso_by_id(curso_id)
        usuario = self.db.query(Usuario).filter(Usuario.id == usuario_id).first()

        if curso and usuario and usuario not in curso.usuarios:
            curso.usuarios.append(usuario)
            self.db.commit()
            self.db.refresh(curso)
        return curso

    def remover_usuario_do_curso(self, curso_id: int, usuario_id: int):
        curso = self.get_curso_by_id(curso_id)
        if not curso:
            return None

        curso.usuarios = [u for u in curso.usuarios if u.id != usuario_id]
        self.db.commit()
        return curso