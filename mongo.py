import contextlib
from typing import AsyncGenerator

import motor.motor_asyncio

import settings


class MongoDBException(Exception):
    pass


client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_DSN_TEMPLATE)
db = client["test_db"]


@contextlib.asynccontextmanager
async def _session() -> AsyncGenerator[motor.motor_asyncio.AsyncIOMotorClient, None]:
    try:
        yield db.messages
    except Exception as e:
        raise MongoDBException(e) from None


async def insert(values: list) -> None:

    async with _session() as ses:
        await ses.insert_many(values)


async def get_city_data(city: str) -> None:

    async with _session() as ses:
        return await ses.find_one({"city": city}, {"_id": 0})


async def get_all_cities(city: str) -> None:
    async with _session() as ses:
        return await ses.find(
            {"city": {"$regex": city}},
            {"city": 1, "_id": 0}
        ).to_list(length=None)

