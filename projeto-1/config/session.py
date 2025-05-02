from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import AsyncSession
from config.engine import engine, engine_sync

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, class_=AsyncSession)
SessionLocalSync = sessionmaker(bind=engine_sync, autoflush=False, autocommit=False)
async def get_db():
    async with SessionLocal() as db:  # Usando async with para criar e garantir o fechamento da sessão
        print("----------------------------------ABRINDO CONEXÃO ASYNC----------------------------------")
        try:
            yield db
        finally:
            print("----------------------------------FECHANDO CONEXÃO ASYNC----------------------------------")
            # O db.close() não é mais necessário, pois com async with, a sessão será fechada automaticamente

def get_db_sync():
    db = SessionLocalSync()
    print("----------------------------------ABRINDO CONEXÃO----------------------------------")
    try:
        yield db
    finally:
        print("----------------------------------FECHANDO CONEXÃO----------------------------------")
        db.close()
# def get_db():
#     db : Session = SessionLocal()
#     print("----------------------------------ABRINDO CONEXÃO----------------------------------")
#     try:
#         yield db
#     finally:
#         print("----------------------------------FECHANDO CONEXÃO----------------------------------")
#         db.close()

    