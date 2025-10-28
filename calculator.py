from random import choice
from unittest import case

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
choice=input("enter the choice(+,-,*,/):")
match choice:
    case "+":
        print(num1 + num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case "-":
        print(num1 - num2)
