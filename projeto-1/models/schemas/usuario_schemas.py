from pydantic import BaseModel
from typing import Optional, List

class UsuarioBase(BaseModel):
    nome: str
    email: Optional[str] = None
    ativo: Optional[bool] = True
    hashed_password: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    pass

class UsuarioOut(UsuarioBase):
    id: int
    nome: str
    email: str
    

    class Config:
        orm_mode = True