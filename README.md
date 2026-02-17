# Multiples Analyzer with User-Defined Operations

## Objective:
The goal of this assignment is to find the sum of all numbers between 1 and 100 that are divisible by 5 using:
- Provide a starting range
- Provide an ending range
- Provide a divisor
- Choose an operation (Sum, Product, Average, or Count) and compute results based on numbers divisible by the given divisor.

## Description:
The program includes input validation (starting range must be less than ending range, divisor cannot be zero), looping through the range, checking divisibility using modulo (%), collecting qualifying numbers, performing the selected operation (1 → Sum, 2 → Product, 3 → Average, 4 → Count), and printing all numbers divisible by the chosen divisor along with the final computed result.

## Python Code:
```
from pymongo import MongoClient
import datetime

print("Program started")
client = MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB")

db = client["sum_of_multiples_db"]
collection = db["sum_of_multiples_collection"]

while True:
    try:
        a = int(input("Enter Starting range: "))
        z = int(input("Enter Ending range: "))
        if a < z:
            break
        else:
            print("Starting range must be less than ending range")
    except ValueError:
        print("Please enter only numbers")

while True:
    try:
        n = int(input("Enter Divisor: "))
        if n != 0:
            break
        else:
            print("Divisor cannot be zero")
    except ValueError:
        print("Please enter only numbers")

print("\nChoose the operation:")
print("1. Sum")
print("2. Product")
print("3. Average")
print("4. Count")

while True:
    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
        if choice in [1, 2, 3, 4]:
            break
        else:
            print("Please choose between 1 and 4")
    except ValueError:
        print("Please enter only numbers")

print(f"\nNumbers divisible by {n} between {a} and {z}")

nums = []

for i in range(a, z + 1):
    if i % n == 0:
        print(i, end=" ")
        nums.append(i)

result_amount = 0
op_type = ""

if len(nums) == 0:
    print("\nNo numbers divisible by", n)
else:
    if choice == 1:
        result_amount = sum(nums)
        op_type = "Sum"
        print(f"\nSum = {result_amount}")

    elif choice == 2:
        product = 1
        for x in nums:
            product *= x
        result_amount = product
        op_type = "Product"
        print(f"\nProduct = {result_amount}")

    elif choice == 3:
        result_amount = sum(nums) / len(nums)
        op_type = "Average"
        print(f"\nAverage = {result_amount}")

    elif choice == 4:
        result_amount = len(nums)
        op_type = "Count"
        print(f"\nCount = {result_amount}")

if op_type:
    print("Inserting data into MongoDB...")
    
    current_now = datetime.datetime.now()

    collection.insert_one({
        "start_range": a,
        "end_range": z,
        "divisor": n,
        "operation": op_type,
        "result": result_amount,
        "date": current_now.strftime("%Y-%m-%d"),
        "time": current_now.strftime("%H:%M:%S")
    })

    print("✅ Data inserted successfully")
```

## Output:
Program started
Connected to MongoDB
Enter Starting range: 2
Enter Ending range: 88
Enter Divisor: 3

Choose the operation:
1. Sum
2. Product
3. Average
4. Count
Enter your choice (1/2/3/4): 3

Numbers divisible by 3 between 2 and 88
3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69 72 75 78 81 84 87
Average = 45.0
Inserting data into MongoDB...
✅ Data inserted successfully

<img width="1974" height="644" alt="image" src="https://github.com/user-attachments/assets/ae298ad3-2b0a-4c78-8a31-ab616497a25a" />

<img width="3200" height="1500" alt="image" src="https://github.com/user-attachments/assets/12d81021-2291-478a-8421-2b51e8921b75" />

## Result:
The program successfully validates inputs, identifies all numbers divisible by the user-provided divisor, performs the selected computation, displays the complete list of divisible numbers, and prints the final calculated value.
