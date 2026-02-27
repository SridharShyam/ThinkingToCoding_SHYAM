import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

if not MONGODB_URI:
    raise ValueError("No MONGODB_URI provided in environment variables")
if not DATABASE_NAME:
    raise ValueError("No DATABASE_NAME provided in environment variables")
if not COLLECTION_NAME:
    raise ValueError("No COLLECTION_NAME provided in environment variables")