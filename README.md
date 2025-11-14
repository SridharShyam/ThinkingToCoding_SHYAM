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
while True:
    a = int(input("Enter Starting range: "))
    z = int(input("Enter Ending range: "))

    if a < z:
        break
    else:
        print("Error: Starting range must be less than ending range.\n")

while True:
    n = int(input("Enter Divisor: "))

    if(n != 0):
        break
    else:
        print("Error: Divisor cannot be zero. Please enter a valid divisor.\n")

print("\nChoose the operation:")
print("1. Sum")
print("2. Product")
print("3. Average")
print("4. Count")

choice = int(input("Enter your choice (1/2/3/4): "))
print(f"\nNumbers divisible by {n} between {a} and {z}")

nums = []

for i in range(a, z + 1):
    if i % n == 0:
        print(i, end=" ")
        nums.append(i)

# No divisible numbers
if len(nums) == 0:
    print("\nNo numbers divisible by", n)
else:
    if choice == 1:  # Sum
        print(f"\nSum = {sum(nums)}")

    elif choice == 2:  # Product
        product = 1
        for x in nums:
            product *= x
        print(f"\nProduct = {product}")

    elif choice == 3:  # Average
        avg = sum(nums) / len(nums)
        print(f"\nAverage = {avg}")

    elif choice == 4:  # Count
        print(f"\nCount = {len(nums)}")

    else:
        print("\nInvalid choice!")
```

## Output:
Enter Starting range: 2
Enter Ending range: 105
Enter Divisor: 4

Choose the operation:
1. Sum
2. Product
3. Average
4. Count
Enter your choice (1/2/3/4): 3

Numbers divisible by 4 between 2 and 105
4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80 84 88 92 96 100 104
Average = 54.0

<img width="1186" height="484" alt="image" src="https://github.com/user-attachments/assets/cc36a492-a5a4-4fad-b974-63faf875ee89" />

## Result:
The program successfully validates inputs, identifies all numbers divisible by the user-provided divisor, performs the selected computation, displays the complete list of divisible numbers, and prints the final calculated value.
