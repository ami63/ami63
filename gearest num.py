num1= int(input("Enter the first number"))
num2= int(input("Enter the second number"))
num3= int(input("Enter the third number"))

if(num1> num2) and(num1> num3):
    print("greatest number", num1)
elif(num2>num3) and (num2> num1):
    print("second number is greatest number",num2)
else:
    print("third is greatest", num3)