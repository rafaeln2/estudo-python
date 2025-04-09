from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./projeto-1.db"  # ou PostgreSQL, MySQL, etc
engine = create_engine(DATABASE_URL)