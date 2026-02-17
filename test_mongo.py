from pymongo import MongoClient

print("Program started")

client = MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB")

client.close()
print("Program ended")
