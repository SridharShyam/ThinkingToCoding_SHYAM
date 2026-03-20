from fastapi import FastAPI, HTTPException, Body, Form
from typing import Optional
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from pymongo import MongoClient
from bson import ObjectId
from enum import Enum
import datetime
import config

app = FastAPI(
    title="Number Operations API",
    description="An API to perform operations on numbers divisible by a divisor in a given range and save the run to MongoDB."
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Connect to MongoDB
try:
    client = MongoClient(config.MONGODB_URI)
    db = client[config.DATABASE_NAME]
    collection = db[config.COLLECTION_NAME]
    print("FastAPI connected to MongoDB successfully!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")

class OperationChoice(str, Enum):
    SUM = "Sum"
    PRODUCT = "Product"
    AVERAGE = "Average"
    COUNT = "Count"

class CalculationRequest(BaseModel):
    start_range: int = Field(..., description="The starting range (must be less than ending range)", example=1)
    end_range: int = Field(..., description="The ending range", example=20)
    divisor: int = Field(..., description="The divisor to check divisibility (cannot be 0)", example=2)
    choice: OperationChoice = Field(..., description="Select the operation: Sum, Product, Average, or Count", example=OperationChoice.SUM)

class CalculationResponse(BaseModel):
    numbers: list[int]
    operation: str
    result: float
    message: str

@app.post("/calculate", response_model=CalculationResponse)
def calculate_operation(
    start_range: int = Form(..., description="The starting range (must be less than ending range)", example=1),
    end_range: int = Form(..., description="The ending range", example=20),
    divisor: int = Form(..., description="The divisor to check divisibility (cannot be 0)", example=2),
    choice: OperationChoice = Form(..., description="Select the operation: Sum, Product, Average, or Count", example=OperationChoice.SUM)
):
    a = start_range
    z = end_range
    n = divisor

    if a >= z:
        raise HTTPException(status_code=400, detail="Starting range must be less than ending range")
    if n == 0:
        raise HTTPException(status_code=400, detail="Divisor cannot be zero")
    
    # Find numbers divisible by n in range a to z inclusive
    nums = [i for i in range(a, z + 1) if i % n == 0]

    if not nums:
        return {
            "numbers": [],
            "operation": choice.value,
            "result": 0.0,
            "message": f"No numbers divisible by {n} between {a} and {z}"
        }

    result_amount = 0.0
    op_type = ""

    if choice == OperationChoice.SUM:
        result_amount = float(sum(nums))
        op_type = "Sum"
    elif choice == OperationChoice.PRODUCT:
        product = 1
        for x in nums:
            product *= x
        result_amount = float(product)
        op_type = "Product"
    elif choice == OperationChoice.AVERAGE:
        result_amount = float(sum(nums) / len(nums))
        op_type = "Average"
    elif choice == OperationChoice.COUNT:
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

@app.get("/history")
def get_history():
    """Retrieve all calculation history from MongoDB."""
    try:
        history = list(collection.find())
        for doc in history:
            doc["_id"] = str(doc["_id"])
        return history
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.put("/history/{record_id}")
def update_history(
    record_id: str,
    start_range: Optional[int] = Form(None, description="The starting range"),
    end_range: Optional[int] = Form(None, description="The ending range"),
    divisor: Optional[int] = Form(None, description="The divisor"),
    operation: Optional[OperationChoice] = Form(None, description="The operation type"),
    result: Optional[float] = Form(None, description="The result value")
):
    """Update a specific calculation record in MongoDB by its ID."""
    if not ObjectId.is_valid(record_id):
        raise HTTPException(status_code=400, detail="Invalid record ID format")
    
    # Map form fields to the dictionary
    update_data = {
        "start_range": start_range,
        "end_range": end_range,
        "divisor": divisor,
        "operation": operation.value if operation else None,
        "result": result
    }
    
    # Filter out None values to perform partial update
    update_dict = {k: v for k, v in update_data.items() if v is not None}
    
    if not update_dict:
        raise HTTPException(status_code=400, detail="No update data provided")

    try:
        result = collection.update_one({"_id": ObjectId(record_id)}, {"$set": update_dict})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Record not found")
        return {"message": "Record updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.delete("/history/{record_id}")
def delete_history(record_id: str):
    """Delete a specific calculation record from MongoDB by its ID."""
    if not ObjectId.is_valid(record_id):
        raise HTTPException(status_code=400, detail="Invalid record ID format")

    try:
        result = collection.delete_one({"_id": ObjectId(record_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Record not found")
        return {"message": "Record deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")