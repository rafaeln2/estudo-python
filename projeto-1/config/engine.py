from sqlalchemy import create_engine, text
import os


# DATABASE_URL = "sqlite:///./projeto-1.db"
# docker run -d   --name meu-postgres   
# -e POSTGRES_USER=postgres   
# -e POSTGRES_PASSWORD=1234   
# -e POSTGRES_DB=meubanco   
# -v postgres_data:/var/lib/postgresql/data   
# -p 5999:5432   postgres:latest
HOST="localhost" #"172.17.0.1" #localhost
usuario = "postgres"
senha = "1234"
porta = "5400" #5432
nome_banco = "meubanco" #estudo_db
DATABASE_URL = f"postgresql://{usuario}:{senha}@{HOST}:{porta}/{nome_banco}" #os.environ.get("DATABASE_URL") 
engine = create_engine(DATABASE_URL, echo=True)