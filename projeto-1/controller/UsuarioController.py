import stat
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from config.session import get_db
from models.schemas.usuario_schemas import UsuarioCreate, UsuarioUpdate, UsuarioOut
from controller.AuthController import get_current_user
from repository import UsuarioRepository
from typing import List
from teste.UsuarioCRUDTest import criar_base,  insert_usuario, select_usuario_by_email, update_usuario, update_usuario_curso
from typing import Annotated

import csv
import random
import requests
import httpx
from mensageria import Consumer, Publisher
import pika
from io import StringIO

router = APIRouter(dependencies=[Depends(get_current_user)])
router_publico = APIRouter()
            
@router_publico.get("/csv_read")
def read_csv():
    with open('off 200.csv', 'r') as file: # with é um alternativa pra um try finally pra abrir e fechar o reader
        csv_reader = csv.reader(file)
        next(csv_reader) #pula a primeira linha
        list = []
        for row in csv_reader:
            list.append(row)
        return list
    
@router_publico.get("/csv_write")
def write_csv():
    with open('off 200.csv', 'r') as file: # with é um alternativa pra um try finally pra abrir e fechar o reader
        csv_reader = csv.reader(file)
        
        with open('new_file.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter='/')
            csv_writer.writerow([next(csv_reader),'Idade'])
            for row in csv_reader:        
                csv_writer.writerow([row[0], random.randint(1950, 2001)])
                
@router_publico.get("/enderecos")
async def write_csv():
    via_cep_url = 'https://viacep.com.br/ws/{}/json/'
    with open('enderecos_1.csv', 'r') as file:
        csv_reader = csv.reader(file)
        with open('enderecos_completos.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter='/')
            csv_writer.writerow([next(csv_reader)[0], 'UF', 'Bairro', 'Logradouro'])
            for row in csv_reader:        
                response = requests.get(via_cep_url.format(row[0].replace('-', '')))
                endereco = response.json()
                if response.status_code == 200 and "erro" not in endereco:
                    csv_writer.writerow([row[0], endereco['uf'], endereco['bairro'], endereco['logradouro']])
                else:
                    print(f"Erro ao buscar dados do CEP {row[0]}: {response.status_code}")

                
@router_publico.post("/enderecos-upload")
async def write_imported_csv(file: UploadFile = File(...)):
    print("Entrou na funcao")
    via_cep_url = 'https://viacep.com.br/ws/{}/json/'
    
    # Lê o conteúdo do arquivo CSV (em formato binário)
    contents = await file.read()
    # Converte o conteúdo binário para uma string usando StringIO
    stringio = StringIO(contents.decode()) 
    # Usa a biblioteca csv para ler os dados
    csv_reader = csv.DictReader(stringio)
    # Processa as linhas do CSV e as coloca em uma lista
    # rows = [row for row in csv_reader]
    with open('enderecos_upload_completos.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='/')
        csv_writer.writerow(['CEP', 'UF', 'Bairro', 'Logradouro'])
        async with httpx.AsyncClient() as client:
            for row in csv_reader:
                response = await client.get(via_cep_url.format(row['CEP'].replace('-', '')))
                endereco = response.json()
                if response.status_code == 200 and "erro" not in endereco:
                    endereco = response.json()
                    csv_writer.writerow([row['CEP'], endereco['uf'], endereco['bairro'], endereco['logradouro']])
                else:
                    print(f"Erro ao buscar dados do CEP {row['CEP']}: {response.status_code}")            
        

# Endpoint de teste simples
@router_publico.get("/teste")
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
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/auth", status_code=status.HTTP_200_OK)
async def obter_usuario_com_validacao(user = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=401, detail="Usuário não autenticado")
    # crud = UsuarioRepository.UsuarioRepository(db)
    # usuario = await crud.get_usuario_by_id(usuario_id)
    if not user:
        raise HTTPException(status_code=404, detail="Falha na autenticação")
    return user

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
