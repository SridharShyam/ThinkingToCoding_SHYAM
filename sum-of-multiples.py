total = 0
print("Numbers divisible by 5 between 1 and 100\n")
for i in range(1,101):
    if i%5==0:
        print(i, end=" ")
        total+=i

print("\nSum of all numbers divisible by 5: ",total)