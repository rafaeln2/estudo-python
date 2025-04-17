from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from config.session import get_db
from models.schemas.UsuarioSchemas import UsuarioCreate, UsuarioUpdate, UsuarioOut
from repository import UsuarioRepository
from typing import List
from teste.UsuarioCRUDTest import criar_base,  insert_usuario, select_usuario_by_email, update_usuario, update_usuario_curso

router = APIRouter()

# Endpoint de teste simples
@router.get("/teste")
async def teste():
    return {"descricao": "Curso teste API"}

# Criação da base
@router.get("/createALL")
async def criar_db(db: AsyncSession = Depends(get_db)):
    print("entrou no inserts do teste")
    try:
        await insert_usuario(db)
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
    try:
        await select_usuario_by_email(db)
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
    try:
        await update_usuario(db)
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
    try:
        await update_usuario_curso(db)
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
    
    
      # agora é async
    return "-------------------------CRIANDO DATABASE-------------------------"

# Listar todos os usuários
@router.get("/", response_model=List[UsuarioOut])
async def listar_usuarios(db: AsyncSession = Depends(get_db)):
    crud = UsuarioRepository.UsuarioRepository(db)
    usuarios = await crud.get_all_usuarios()
    return usuarios

# Obter um usuário por ID
@router.get("/{usuario_id}", response_model=UsuarioOut)
async def obter_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    crud = UsuarioRepository.UsuarioRepository(db)
    usuario = await crud.get_usuario_by_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

# Criar um novo usuário
@router.post("/", response_model=UsuarioOut, status_code=status.HTTP_201_CREATED)
async def criar_usuario(usuario: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    usuario_dict = usuario.model_dump()
    crud = UsuarioRepository.UsuarioRepository(db)
    usuario_salvo = await crud.insert(usuario_dict["nome"], usuario_dict["email"], usuario_dict["ativo"])
    return usuario_salvo

# Atualizar um usuário existente
@router.put("/{usuario_id}", response_model=UsuarioOut)
async def atualizar_usuario(usuario_id: int, dados: UsuarioUpdate, db: AsyncSession = Depends(get_db)):
    crud = UsuarioRepository.UsuarioRepository(db)
    usuario = await crud.get_usuario_by_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    for key, value in dados.model_dump(exclude_unset=True).items():
        setattr(usuario, key, value)

    usuario_atualizado = await crud.update_usuario(usuario_id, usuario.nome, usuario.email, usuario.ativo)
    return usuario_atualizado

# Deletar um usuário
@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    crud = UsuarioRepository.UsuarioRepository(db)
    usuario = await crud.delete_usuario(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return
