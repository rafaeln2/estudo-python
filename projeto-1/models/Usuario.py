from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from config.base import Base
from pydantic import BaseModel

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    ativo = Column(Boolean, default=True)
    email = Column(String, index=True)
    
    cursos = relationship("Curso", secondary='usuario_curso', back_populates="usuarios")
    

    def __rep__r__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, ativo={self.ativo}, email={self.email})"