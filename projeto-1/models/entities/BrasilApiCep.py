from config.base import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Mapped, mapped_column

class BrasilApiCep(Base):
    __tablename__ = 'brasil_api_cep'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    cep: Mapped[str] = mapped_column(String(8), nullable=False)
    state: Mapped[str] = mapped_column(String(2), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    neighborhood: Mapped[str] = mapped_column(String(100), nullable=False)
    street: Mapped[str] = mapped_column(String(200), nullable=False)
    service: Mapped[str] = mapped_column(String(50), nullable=False)

    # def __init__(self, cep: str, state: str, city: str, neighborhood: str, street: str, service: str):
    #     self.cep = cep
    #     self.state = state
    #     self.city = city
    #     self.neighborhood = neighborhood
    #     self.street = street
    #     self.service = service

    def __repr__(self):
        return f"<Endereco(cep={self.cep}, state={self.state}, city={self.city}, neighborhood={self.neighborhood}, street={self.street}, service={self.service})>"
