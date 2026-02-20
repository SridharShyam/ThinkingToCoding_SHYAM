from pymongo import MongoClient
import datetime
import config

print("Program started")
client = MongoClient(config.MONGODB_URI)
print("Connected to MongoDB")

db = client[config.DATABASE_NAME]
collection = db[config.COLLECTION_NAME]

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

    print("Data inserted successfully")
