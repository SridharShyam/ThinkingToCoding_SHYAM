while True:
    a = int(input("Enter Starting range: "))
    z = int(input("2Enter Ending range: "))

    if a < z:
        break
    else:
        print("Error: Starting range must be less than ending range.\n")

n = int(input("Enter Divisor: "))

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
