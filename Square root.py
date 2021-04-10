import math

number= int(input("Enter a number higher than 0: "))

if number<0:
    print("Is impossible to do a square root whit a negative number")

else:
    print(math.sqrt(number))