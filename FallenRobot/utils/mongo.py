from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

from FallenRobot import MONGO_DB_URI

mongo = MongoCli(MONGO_DB_URI)
db = mongo.FallenRobot

