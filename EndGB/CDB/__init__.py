from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

mongo = MongoClient("mongodb+srv://keshavalpha:keshavalpha@cluster0.p7qz4.mongodb.net/?retryWrites=true&w=majority")
db = mongo.AFK
