
from datetime import datetime, timedelta, timezone
from typing import Annotated
from passlib.context import CryptContext
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from config.session import SessionLocal, get_db
from sqlalchemy.ext.asyncio import AsyncSession
# from models.schemas.auth_schemas import Token
from models.schemas import usuario_schemas, auth_schemas
from models.entities.Usuario import Usuario
import jwt

from repository.UsuarioRepository import UsuarioRepository


router = APIRouter()

SECRET_KEY = 'rafaelTesteSecret'
ALGORITHM = 'HS256'

bcrpyt_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

async def authenticate_user(nome: str, password: str, db: AsyncSession):
    usuario = await UsuarioRepository(db).get_usuario_by_nome(nome=nome)
    print(usuario.__repr__())
    if not usuario:
        return False
    if not bcrpyt_context.verify(password, hash=usuario.hashed_password):
        return False
    return usuario

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/", response_model=usuario_schemas.UsuarioOut)
async def create_user(usuario_create_req: usuario_schemas.UsuarioCreate, db: AsyncSession = Depends(get_db)) -> usuario_schemas.UsuarioOut:
    # usuario = Usuario(
    #     nome = usuario_create_req.nome, 
    #     email = usuario_create_req.email, 
    #     hashed_password = bcrpyt_context.hash(secret=usuario_create_req.senha))
    repo = UsuarioRepository(db)
    new_usuario = await repo.insert(nome = usuario_create_req.nome, 
        email = usuario_create_req.email, 
        hashed_password = bcrpyt_context.hash(usuario_create_req.hashed_password)
    )
    
    return new_usuario

@router.post("/token", response_model=auth_schemas.Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: AsyncSession = Depends(get_db)):
    usuario = await authenticate_user(form_data.username, form_data.password, db)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Nome ou senha inválidos")
    if not bcrpyt_context.verify(secret=form_data.password, hash=usuario.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Nome ou senha inválidos")
    token = create_access_token(usuario.nome, usuario.id, timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=usuario_schemas.UsuarioOut)
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Nome ou senha inválidos")
        return {"username": username, "id": user_id}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    

