from pymongo import MongoClient


class MongoDBService:

    client = MongoClient(
        "mongodb://localhost:27017/"
    )

    db = client["socialflow"]

    scraped_pages = db["scraped_pages"]