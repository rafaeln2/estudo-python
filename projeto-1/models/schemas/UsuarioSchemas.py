from pydantic import BaseModel
from typing import Optional, List

class UsuarioBase(BaseModel):
    nome: str
    email: Optional[str] = None
    ativo: Optional[bool] = True

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    pass

class UsuarioOut(UsuarioBase):
    id: int
    nome: str

    class Config:
        orm_mode = True