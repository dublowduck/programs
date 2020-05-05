#import stuff that may be needed
#from math import *
#ask the user what they are trying to do
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
operator = input("Enter an operator: ")

#then calculate what the user entered

#if times, then times
if operator == "*":
    result = float(num1) * float(num2)
#if division, then divide
if operator == "/":
    result = int(num1) / int(num2)
#if addition, that add it together
if operator == "+":
    result = float(num1) + float(num2)
# if subtraction, then take the numbers away from each other
if operator == "-":
    result = float(num1) - float(num2)
# show them all the hardwork, they could`nt be bothered to do
print(float(result))