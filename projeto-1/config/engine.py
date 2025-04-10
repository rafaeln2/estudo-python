from sqlalchemy import create_engine, text

# DATABASE_URL = "sqlite:///./projeto-1.db"
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/estudo_db"
engine = create_engine(DATABASE_URL, echo=True)