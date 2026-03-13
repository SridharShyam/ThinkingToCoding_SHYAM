from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from pymongo import MongoClient
import datetime
import config

app = FastAPI(
    title="Number Operations API",
    description="An API to perform operations on numbers divisible by a divisor in a given range and save the run to MongoDB."
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Connect to MongoDB using existing config
try:
    client = MongoClient(config.MONGODB_URI)
    db = client[config.DATABASE_NAME]
    collection = db[config.COLLECTION_NAME]
    print("FastAPI connected to MongoDB successfully!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")

class CalculationRequest(BaseModel):
    start_range: int = Field(..., description="The starting range (must be less than ending range)", example=1)
    end_range: int = Field(..., description="The ending range", example=20)
    divisor: int = Field(..., description="The divisor to check divisibility (cannot be 0)", example=2)
    choice: int = Field(..., description="1 for Sum, 2 for Product, 3 for Average, 4 for Count", example=1)

class CalculationResponse(BaseModel):
    numbers: list[int]
    operation: str
    result: float
    message: str

@app.post("/calculate", response_model=CalculationResponse)
def calculate_operation(request: CalculationRequest):
    a = request.start_range
    z = request.end_range
    n = request.divisor
    choice = request.choice

    if a >= z:
        raise HTTPException(status_code=400, detail="Starting range must be less than ending range")
    if n == 0:
        raise HTTPException(status_code=400, detail="Divisor cannot be zero")
    if choice not in [1, 2, 3, 4]:
        raise HTTPException(status_code=400, detail="Please choose between 1 and 4")

    # Find numbers divisible by n in range a to z inclusive
    nums = [i for i in range(a, z + 1) if i % n == 0]

    if not nums:
        return {
            "numbers": [],
            "operation": "None",
            "result": 0.0,
            "message": f"No numbers divisible by {n} between {a} and {z}"
        }

    result_amount = 0.0
    op_type = ""

    if choice == 1:
        result_amount = float(sum(nums))
        op_type = "Sum"
    elif choice == 2:
        product = 1
        for x in nums:
            product *= x
        result_amount = float(product)
        op_type = "Product"
    elif choice == 3:
        result_amount = float(sum(nums) / len(nums))
        op_type = "Average"
    elif choice == 4:
        result_amount = float(len(nums))
        op_type = "Count"

    # Insert into MongoDB
    current_now = datetime.datetime.now()
    document = {
        "start_range": a,
        "end_range": z,
        "divisor": n,
        "operation": op_type,
        "result": result_amount,
        "date": current_now.strftime("%Y-%m-%d"),
        "time": current_now.strftime("%H:%M:%S")
    }
    
    try:
        collection.insert_one(document)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    return {
        "numbers": nums,
        "operation": op_type,
        "result": result_amount,
        "message": "Calculation successful and data saved to MongoDB"
    }

@app.get("/")
def read_root():
    return FileResponse("static/index.html")
