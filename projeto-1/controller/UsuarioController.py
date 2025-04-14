from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.session import get_db
from config.schemas import UsuarioCreate, UsuarioUpdate, UsuarioOut
from models import Usuario, Curso, usuario_curso
from repository import UsuarioRepository
from typing import List
from teste.UsuarioCRUDTest import criar_base

app = FastAPI()

# GET, POST, PUT, DELETE
# @app.get("/usuarios")
# def get_usuarios():
#     print("----------------------------------COMEÇO GET_USUARIOS----------------------------------")
#     db_gen = get_db()        # cria o generator
#     db = next(db_gen)        # pega a sessão (Session)
#     crud = UsuarioRepository.UsuarioRepository(db)
#     usuarios = crud.get_usuario_by_id(1);
#     return usuarios
#     print("----------------------------------FIM GET_USUARIOS----------------------------------")
  
#
@app.get("/create")  
def listar_usuarios():
    criar_base()
    return "-------------------------CRIANDO DATABASE-------------------------"

@app.get("/usuarios", response_model=List[UsuarioOut])  
def listar_usuarios(db: Session = Depends(get_db)):
    return UsuarioRepository.UsuarioRepository(db).get_all_usuarios()
    
@app.get("/{usuario_id}", response_model=UsuarioOut)
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = UsuarioRepository.UsuarioRepository(db).get_usuario_by_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario
    
@app.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_dict = usuario.model_dump()
    print(usuario_dict)
    usuario_salvo = UsuarioRepository.UsuarioRepository(db).insert(usuario_dict["nome"], usuario_dict["email"], usuario_dict["ativo"])
    return usuario_salvo

@app.put("/{usuario_id}", response_model=UsuarioOut, status_code=status.HTTP_200_OK)
def atualizar_usuario(usuario_id: int, dados: UsuarioUpdate, db: Session = Depends(get_db)):
    crud = UsuarioRepository.UsuarioRepository(db)
    usuario = crud.get_usuario_by_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    for key, value in dados.model_dump(exclude_unset=True).items():
        setattr(usuario, key, value)
    usuario_atualizado = crud.update_usuario(usuario_id, usuario.nome, usuario.email, usuario.ativo)
    return usuario_atualizado   

@app.delete("/{usuario_id}", status_code=status.HTTP_200_OK)
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = UsuarioRepository.UsuarioRepository(db).delete_usuario(usuario_id)
    return
    
    