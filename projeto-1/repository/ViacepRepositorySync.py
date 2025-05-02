from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from models.entities.ViaCep import ViaCep

class ViacepRepositorySync:
    def __init__(self, db: Session):
        self.db = db

    def create_viacep(self, viacep: ViaCep):
        self.db.add(viacep)
        self.db.commit()
        self.db.refresh(viacep)
        return viacep

    def get_viacep_by_id(self, viacep_id: int):
        return self.db.query(ViaCep).filter(ViaCep.id == viacep_id).first()

    def get_viacep_by_cep(self, cep: str):
        return self.db.query(ViaCep).filter(ViaCep.cep == cep).first()

    def get_all_viaceps(self, skip: int = 0, limit: int = 100):
        return self.db.query(ViaCep).offset(skip).limit(limit).all()

    def update_viacep(self, viacep_id: int, viacep_data: dict):
        self.db.execute(
            update(ViaCep)
            .where(ViaCep.id == viacep_id)
            .values(**viacep_data)
        )
        self.db.commit()
        return self.get_viacep_by_id(viacep_id)

    def delete_viacep(self, viacep_id: int):
        self.db.execute(
            delete(ViaCep).where(ViaCep.id == viacep_id)
        )
        self.db.commit()
