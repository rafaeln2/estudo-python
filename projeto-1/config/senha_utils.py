from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash_senha(senha: str):
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash_senha: str):
    return pwd_context.verify(senha, hash_senha)