from pymongo import MongoClient
import config

print("Program started")

client = MongoClient(config.MONGODB_URI)
print("Connected to MongoDB")

client.close()
print("Program ended")