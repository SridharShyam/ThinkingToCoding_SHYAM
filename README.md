# The logical looper sum of multiples

## Objective:
The goal of this assignment is to find the sum of all numbers between 1 and 100 that are divisible by 5 using:
- Loop iteration
- Conditional checking
- Accumulation

## Description:
This Python program loops through the numbers from 1 to 100 and checks which ones are divisible by 5. Each qualifying number is printed out and added to a running total. At the end, the program displays the complete list of numbers and their sum.

## Python Code:
```
total = 0
print("Numbers divisible by 5 between 1 and 100\n")
for i in range(1,101):
    if i%5==0:
        print(i, end=" ")
        total+=i

print("\nSum of all numbers divisible by 5: ",total)
```

## Output:
Numbers divisible by 5 between 1 and 100

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100

Sum of all numbers divisible by 5:  1050


<img width="602" height="92" alt="image" src="https://github.com/user-attachments/assets/5a69f95a-4500-456a-9519-3d0c557da63d" />

## Result:
The program successfully calculates and displays the sum of all numbers between 1 and 100 that are divisible by 5.
