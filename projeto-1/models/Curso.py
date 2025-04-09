from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from config.base import Base

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    
    usuarios = relationship("Usuario", secondary="usuario_curso", back_populates="cursos")
    
    def __repr__(self):
        return f"Curso(id={self.id}, nome={self.nome})"