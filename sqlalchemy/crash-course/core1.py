from sqlalchemy import create_engine, MetaData, Table, Column,  Integer, String
import urllib.parse
from sqlalchemy.orm import declarative_base
# import psycopg3

# DB_HOST = "localhost"
# DB_NAME = "estudodatabase"
# DB_USER = "rafael_ubuntu"
# DB_PASSWORD = "1234"
# DB_PORT = "5432"  # Para PostgreSQL

# usuario = urllib.parse.quote("rafael_ubuntu")
# DATABASE_URL = "postgresql://postgres:1234@localhost:5432/teste"
DATABASE_URL = "sqlite:///./teste_inmemory.db"

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)

# try:
#     engine = create_engine(DATABASE_URL, echo=True)
#     with engine.connect() as connection:
#         print("✅ Conexão bem-sucedida!")
# except Exception as e:
#     print(f"❌ Erro ao conectar: {e}")