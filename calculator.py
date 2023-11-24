import math as mp
print("This Calculator made by Abhishek Ujale")
print("1. Addition\n2. Subtraction\n3. Multilication\n4. Division\n5. Modulo\n6. Power")
while (True):
 in_number=int(input("Enter The number for operation.........."))

 if (in_number==1):
    num1=int(input("Enter first number for addition"))
    num2 = int(input("Enter second number for addition"))
    print(f"The Sum of numbers is {num1+num2}")

 elif (in_number==2):
    num1=int(input("Enter first number for subtraction"))
    num2 = int(input("Enter second number for subtraction"))
    print(f"The Subtraction of numbers is {num1-num2}")

 elif (in_number==3):
    num1=int(input("Enter first number for Multiplication"))
    num2 = int(input("Enter second number for Multiplication"))
    print(f"The Multiplication of numbers is {num1-num2}")

 elif (in_number==4):
    num1=float(input("Enter first number for Divider"))
    num2 = float(input("Enter second number for Divisor"))
    print(f"The Division of numbers is {num1/num2}")

 elif (in_number==5):
    num1=int(input("Enter first number "))
    num2 = int(input("Enter second number "))
    print(f"The Modulo of numbers is {num1%num2}")

 elif (in_number==6):
    num1=int(input("Enter the Number"))
    num2 = int(input("Enter the power"))
    print(f"The Output Number  is {int(mp.pow(num1,num2))}")
 else:
    print("Invalid Input")