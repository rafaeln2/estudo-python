from sqlalchemy import create_engine, text

# DATABASE_URL = "sqlite:///./projeto-1.db"
HOST="localhost" #"172.17.0.1" #localhost
DATABASE_URL = f"postgresql://postgres:1234@{HOST}:5432/estudo_db"
engine = create_engine(DATABASE_URL, echo=True)