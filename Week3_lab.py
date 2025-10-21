"""
This file is the code for the Week 3 seminar exercises
which focuses on for loops, while loops and GitHub integration.
"""

for i in range (1,11):
    print(i)
#This loop prints the numbers 1-10, to modify it change the numbers in the parenthesis

cost = [15.00, 12.50, 3.75, 40.25]
total_cost = 0
for total in cost:
    total_cost = total_cost + total
print(f"The total cost is {total_cost:.2f}")

for i in range(1,6):
    print()
    for f in range(i):
        print('*', end=' ')

q = False

while q == False:
    print("---Calculator Menu---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("q. Quit")
    choice = input("Please input a selection: ")
    if (choice == "1"):
        print("You have selected addition.")
        num1 = input("Please input your first number: ")
        float_num1 = float(num1)
        num2 = input("Please input your second number: ")
        float_num2 = float(num2)
        answer = float_num1 + float_num2
        print(f"{float_num1} + {float_num2} = {answer}")
    elif (choice == "2"):
        print("You have chosen subtraction.")
        num1 = input("Please input your first number: ")
        float_num1 = float(num1)
        num2 = input("Please input your second number: ")
        float_num2 = float(num2)
        answer = float_num1 - float_num2
        print(f"{float_num1} - {float_num2} = {answer}")
    elif (choice == "3"):
        print("You have chosen multiplication.")
        num1 = input("Please input your first number: ")
        float_num1 = float(num1)
        num2 = input("Please input your second number: ")
        float_num2 = float(num2)
        answer = float_num1 * float_num2
        print(f"{float_num1} x {float_num2} = {answer}")
    elif (choice == "4"):
        print("You have chosen division.")
        num1 = input("Please input your first number: ")
        float_num1 = float(num1)
        num2 = input("Please input your second number: ")
        float_num2 = float(num2)
        answer = float_num1 / float_num2
        print(f"{float_num1} / {float_num2} = {answer}")
    elif (choice == "q"):
        print("You have chosen to quit, goodbye.")
        q = True
    else:
        print("Your choice is invalid, please choose one of the options and try again.")