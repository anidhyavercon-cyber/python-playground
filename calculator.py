import math
operator = input ("Which operator you want to use?(ADD/SUB/MULTIPLY/DIVIDE) : ")
num1 = float (input("Enter the first number? : "))
num2 = float (input("Enter the second number? : "))

if operator == "ADD":
    result = num1+num2
    print (result)
elif operator == "SUB":
    result = num1-num2
    print (result)
elif operator == "MULTIPY":
    result = num1*num2
    print (result)
elif operator == "DIVIDE":
    result = num1/num2
    print (result)
else: 
    print ("Operator not defined")