from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from config.base import Base
from pydantic import BaseModel

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome : Mapped[str]= mapped_column(String, index=True, nullable=False)
    ativo: Mapped[bool] = mapped_column(Boolean, default=True)
    email: Mapped[str] = mapped_column(String, index=True)
    hashed_password : Mapped[str]= mapped_column(String, nullable=False)
    cursos: Mapped[list["Curso"]] = relationship(secondary="usuario_curso", back_populates="usuarios")
    

    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, ativo={self.ativo}, email={self.email}, senha={self.hashed_password})"