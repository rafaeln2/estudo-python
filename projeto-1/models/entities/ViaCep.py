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
    
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column

from config.base import Base

class ViaCep(Base):
    __tablename__ = 'viacep'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    cep: Mapped[str] = mapped_column(String(8), unique=True, index=True, nullable=False)
    logradouro: Mapped[str] = mapped_column(String(255))
    complemento: Mapped[str] = mapped_column(String(255))
    bairro: Mapped[str] = mapped_column(String(255))
    localidade: Mapped[str] = mapped_column(String(255))
    uf: Mapped[str] = mapped_column(String(2))
    ibge: Mapped[str] = mapped_column(String(10))
    gia: Mapped[str] = mapped_column(String(10))
    ddd: Mapped[str] = mapped_column(String(3))
    siafi: Mapped[str] = mapped_column(String(10))
    usuario_id: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id'))

    def __init__(self, cep: str, logradouro=None, complemento=None, bairro=None,
                 localidade=None, uf=None, ibge=None, gia=None, ddd=None, siafi=None, usuario_id=None):
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf
        self.ibge = ibge
        self.gia = gia
        self.ddd = ddd
        self.siafi = siafi
        self.usuario_id = usuario_id
