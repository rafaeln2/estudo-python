from __future__ import annotations
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Mapped, mapped_column
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from config.base import Base

class Curso(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String, index=True, nullable=False)
    
    usuarios: Mapped[list["Usuario"]] = relationship(secondary="usuario_curso", back_populates="cursos")
    
    def __repr__(self):
        return f"Curso(id={self.id}, nome={self.nome})"