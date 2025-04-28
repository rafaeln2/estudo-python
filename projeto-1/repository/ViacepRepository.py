from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from models.entities import ViaCep

class ViacepRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_viacep(self, viacep: ViaCep):
        self.db.add(viacep)
        await self.db.commit()
        await self.db.refresh(viacep)
        return viacep

    async def get_viacep_by_id(self, viacep_id: int):
        result = await self.db.execute(select(ViaCep).where(ViaCep.id == viacep_id))
        return result.scalars().first()

    async def get_viacep_by_cep(self, cep: str):
        result = await self.db.execute(select(ViaCep).where(ViaCep.cep == cep))
        return result.scalars().first()

    async def get_all_viaceps(self, skip: int = 0, limit: int = 100):
        result = await self.db.execute(select(ViaCep).offset(skip).limit(limit))
        return result.scalars().all()

    async def update_viacep(self, viacep_id: int, viacep_data: dict):
        await self.db.execute(
            update(ViaCep)
            .where(ViaCep.id == viacep_id)
            .values(**viacep_data)
        )
        await self.db.commit()
        return await self.get_viacep_by_id(viacep_id)

    async def delete_viacep(self, viacep_id: int):
        await self.db.execute(
            delete(ViaCep).where(ViaCep.id == viacep_id)
        )
        await self.db.commit()

