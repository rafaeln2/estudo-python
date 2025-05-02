    # {
    #   "cep": "01001-000",
    #   "logradouro": "Praça da Sé",
    #   "complemento": "lado ímpar",
    #   "unidade": "",
    #   "bairro": "Sé",
    #   "localidade": "São Paulo",
    #   "uf": "SP",
    #   "estado": "São Paulo",
    #   "regiao": "Sudeste",
    #   "ibge": "3550308",
    #   "gia": "1004",
    #   "ddd": "11",
    #   "siafi": "7107"
    # }

from __future__ import annotations    
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column

from config.base import Base

class ViaCep(Base):
    __tablename__ = 'viacep'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    cep: Mapped[str] = mapped_column(String(10), unique=True, index=True, nullable=False)
    logradouro: Mapped[str] = mapped_column(String(255))
    complemento: Mapped[str] = mapped_column(String(255))
    unidade: Mapped[str] = mapped_column(String(255))
    bairro: Mapped[str] = mapped_column(String(255))
    localidade: Mapped[str] = mapped_column(String(255))
    uf: Mapped[str] = mapped_column(String(2))
    estado: Mapped[str] = mapped_column(String(255))
    regiao: Mapped[str] = mapped_column(String(255))
    ibge: Mapped[str] = mapped_column(String(10))
    gia: Mapped[str] = mapped_column(String(10))
    ddd: Mapped[str] = mapped_column(String(3))
    siafi: Mapped[str] = mapped_column(String(10))
    
    # CHAVE ESTRANGEIRA
    # usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)

    # RELAÇÃO MANY TO ONE
    # usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="enderecos")


    def __init__(self, cep: str, logradouro=None, complemento=None, unidade=None, bairro=None,
                 localidade=None, uf=None, estado = None, regiao = None, ibge=None, gia=None, ddd=None, siafi=None, usuario=None):
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.unidade = unidade
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf
        self.estado = estado
        self.regiao = regiao
        self.ibge = ibge
        self.gia = gia
        self.ddd = ddd
        self.siafi = siafi
        self.usuario = usuario
