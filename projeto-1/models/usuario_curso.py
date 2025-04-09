from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from config.base import Base

usuario_curso = Table(
    'usuario_curso', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id')),
    Column('curso_id', Integer, ForeignKey('cursos.id'))
)