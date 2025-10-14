"""
This program converts celcius into Farenheit.
"""

#This variable is to store the temperature in celcius so it can be converted
celcius = 0

#This variable takes the value stored in celcius converts it to farenheit using the formula and then stores the new value in the farenheit variable
farenheit = (celcius * 9/5) + 32

#The print statement below allows the user to see the converted value
print(farenheit)

"""
Changing the value of the celcius variable impacts the results of the outputted value at except for -40
"""

name1 = "Neil"
print("This is a string: ", name1)
print(type(name1))

num = 12
print("This is an integer: ", num)
print(type(num))

num2 = 20.00
print("This is a float: ", num2)
print(type(num2))

yes = True
print("This is a boolean: ", yes)
print(type(yes))

num = str(13)
print("I have changed the data type of this variable: ", num)
print(type(num))


name = "Neil"
course = "Computer Science"
fpl = "Python"
movie = "Star Wars Episode 3: Revenge of the Sith"


border = "{:^48}"
print(border.format("-"*48))
print(f"|{name:^48}|")
print(f"|{course:^48}|")
print(f"|{fpl:^48}|")
print(f"|{movie:^48}|")
print(f"{"-"*48:^48}")

userAge = input("How old are you? ")
number = int(userAge)
if(number < 18):
    print("You are a child.")
elif(number >= 18) and (number < 21):
    print("")