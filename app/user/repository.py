"""
user repository
"""
from config import init_database

model = init_database()["users"]


async def find_by_email(email: str) -> dict:
    return await model.find_one({"email": email})


async def create(payload: dict) -> dict:
    user = await model.insert_one(payload)
    return await model.find_one({"_id": user.inserted_id})
