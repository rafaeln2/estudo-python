from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from models.entities.BrasilApiCep import BrasilApiCep

class BrasilApiCepSyncRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_brasil_api_cep(self, brasil_api_cep: BrasilApiCep):
        self.db.add(brasil_api_cep)
        self.db.commit()
        self.db.refresh(brasil_api_cep)
        return brasil_api_cep

    def get_brasil_api_cep_by_id(self, cep_id: int):
        return self.db.query(BrasilApiCep).filter(BrasilApiCep.id == cep_id).first()

    def get_brasil_api_cep_by_cep(self, cep: str):
        return self.db.query(BrasilApiCep).filter(BrasilApiCep.cep == cep).first()

    def get_all_brasil_api_ceps(self, skip: int = 0, limit: int = 100):
        return self.db.query(BrasilApiCep).offset(skip).limit(limit).all()

    def update_brasil_api_cep(self, cep_id: int, cep_data: dict):
        self.db.execute(
            update(BrasilApiCep)
            .where(BrasilApiCep.id == cep_id)
            .values(**cep_data)
        )
        self.db.commit()
        return self.get_brasil_api_cep_by_id(cep_id)

    def delete_brasil_api_cep(self, cep_id: int):
        self.db.execute(
            delete(BrasilApiCep).where(BrasilApiCep.id == cep_id)
        )
        self.db.commit()
