from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
import os


# DATABASE_URL = "sqlite:///./projeto-1.db"
# docker run -d   --name meu-postgres   
# -e POSTGRES_USER=postgres   
# -e POSTGRES_PASSWORD=1234   
# -e POSTGRES_DB=meubanco   
# -v postgres_data:/var/lib/postgresql/data   
# -p 5999:5432   postgres:latest
HOST="localhost" #"172.17.0.1" #localhost
HOST_DOCKER="db"
usuario = "postgres"
senha = "1234"
porta = "5400" #5432 do docker
porta_docker = "5432"
nome_banco = "meubanco" #estudo_db
DATABASE_URL = f"postgresql+asyncpg://{usuario}:{senha}@{HOST}:{porta}/{nome_banco}" #os.environ.get("DATABASE_URL") 
DATABASE_ASYNC_URL = f"postgresql://{usuario}:{senha}@{HOST_DOCKER}:{porta_docker}/{nome_banco}" #conexao sync pro celery
engine = create_async_engine(DATABASE_URL) #, echo=True
engine_sync = create_engine(DATABASE_ASYNC_URL)