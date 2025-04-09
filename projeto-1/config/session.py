from sqlalchemy.orm import sessionmaker
from config.engine import engine

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
def get_db():
    db = SessionLocal()
    print("----------------------------------ABRINDO CONEXÃO----------------------------------")
    try:
        yield db
    finally:
        print("----------------------------------FECHANDO CONEXÃO----------------------------------")
        db.close()
    