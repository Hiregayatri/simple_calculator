''' Name: Gayatri Hire
    Codesoft Internship: Python Programming

Task 1: Calculator
   Design a somple calculator with basic arithamatic operations.
   Prompt the user to input two numbers and an operation choice.
   Perform the calculation and display the result.'''

task_name="**********CALCULATOR***********"
print(task_name.center(16))

print('''Select an Operation to perform from following list:
          1. Adition
          2. Substraction
          3. Multiplication
          4. Division
          5. Exponential
          6. Modulus 
          ''')

operation=int(input("Enter the choice number:"))

if operation==1:
    no1 = float(input("Enter a first number:"))
    no2 = float(input("Enter a second number:"))
    print("Addition of",no1,"+",no2,"=",no1+no2)

elif operation==2:
    no1 = float(input("Enter a first number:"))
    no2 = float(input("Enter a second number:"))
    print("Substraction of",no1,"-",no2,"=",no1-no2)

elif operation==3:
    no1 = float(input("Enter a first number:"))
    no2 = float(input("Enter a second number:"))
    print("Multiplication of", no1,"*",no2,"=",no1*no2)

elif operation==4:
    no1 = float(input("Enter a first number:"))
    no2 = float(input("Enter a second number:"))
    print("Division of", no1, "/", no2,"=",no1/no2)

elif operation==5:
    no1 = float(input("Enter a first number:"))
    no2 = float(input("Enter a second number:"))
    print("Exponention of", no1,"**",no2,"=",no1**no2)

elif operation==6:
    no1 = float(input("Enter a first number:"))
    no2 = float(input("Enter a second number:"))
    print("Modulus of", no1,"%",no2,"=",no1%no2)

else:
    print("Invalid Choice.....Please Try again!!!")



https://github.com/Hiregayatri/SimpleCalculator.git


ryk
byk
ryk
smrk





