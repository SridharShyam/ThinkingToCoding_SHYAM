import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB Configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "sum_of_multiples_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "sum_of_multiples_collection")
