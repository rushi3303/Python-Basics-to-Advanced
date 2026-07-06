# This is a comment. It will not be executed.
print("Hello, World!")
print("Hello, Rushi!")

print("my name is Rushi")

# variable :- a variable is a name that refers to a value. In Python, you can create a variable by assigning a value to it using the equals sign (=).

# name,x,price are variables.

x=10
name = "Rushi"
price = 100.50

print("x =", x)
print("name =", name)
print("price =", price)

# data types :- data types are the classification of data items. In Python, there are several built-in data types, including:

print(type(x))
print(type(name))
print(type(price))

age = 25
old = False
a = None
print(type(age))
print(type(old))    
print(type(a))

# addition

a = 2
b = 3
sum = a + b
print("sum =", sum)

# subtraction

a = 2
b = 3
sub = a - b
print("sub =", sub)


# operators :- operators are special symbols that perform operations on variables and values. In Python, there are several types of operators, including:

# 1) Aruthmetic operators: +, -, *, /, %, **, //

a = 5
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b) 
print("Division:", a / b)
print("Modulus:", a % b)           # remainder
print("Exponentiation:", a ** b) 
print("Floor Division:", a // b)
print("Floor Division:", a // b)

# create simple Calculator

print("===== Simple Calculator =====")

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Power          :", a ** b)

# 2) Comparison operators: ==, !=, >, <, >=, <=

a=50
b=20

print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("a > b:", a > b)    # True
print("a < b:", a < b)    # False
print("a >= b:", a >= b)  # True
print("a <= b:", a <= b)  # False

# assignment operators: =, +=, -=, *=, /=, %=, **=, //=

num = 10 
# num = num + 5
num += 5
print("num =", num)  # 15

num *= 2
print("num =", num)  # 30   

num -= 10
print("num =", num)  # 20

num /= 4
print("num =", num)  # 5.0

# bank account 

balance = 10000

balance += 5000      # Salary

balance -= 2000      # Shopping

print(balance)

# logical operators: and, or, not
a = 50 
b = 30

print(not False)  
print(not (a>b)) 

val1 = True
val2 = True
print("AND operator:", val1 and val2) 
val1 = True
val2 = False 
print("OR operator:", val1 or val2)   # True


# Type conversion :- Type conversion is the process of converting one data type to another. In Python, you can use built-in functions to convert between different data types.

a = 2
b = 3.5

sum = a + b
print("sum =", sum)  # 5.5

# type casting :- Type casting is the process of converting a value from one data type to another. In Python, you can use built-in functions to perform type casting.

a = int("2")
b = 3.5

sum = a + b
print("sum =", sum)  # 5.5

a = 3.14
a = str(a)
print(type(a))  # <class 'str'>

# user input :- User input is the process of getting input from the user. In Python, you can use the input() function to get input from the user.



val = int(input("Enter a number: "))
print("You entered:", val)


name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Name:", name)
print("Age:", age)  
print("Marks:", marks)

# pratice question

# write a program to input 2 numbers & print their sum.
a = int(input("enter your first number:"))
b = int(input("enter your second number:"))

sum = a + b 
print("Sum:", sum)

# 2 ] WAP to input side of a square & input its area.

side = float(input("Enter the side of a square: "))
print("Area of square is:", side * side)

# 3] WAP TO INPUT 2 floating point numbers & print their average.

num1 = float(input("enter first float num:"))
num2 = float(input("enter second float num:"))
average = (num1 + num2) / 2
# print("avg:",(num1 + num2) / 2)
print("Average:", average)


# 4] WAP to input 2 int numbers , a and b.
  #  print true if a is greater than or equal to b. if not print false.

a = int(input("Enter first number: ")) # 5
b = int(input("Enter second number: ")) # 10
print(a >= b) # False


# mini project 1 - Employee Salary Eligibility

salary = float(input("Enter Salary: "))
experience = int(input("Enter Experience (Years): "))

eligible = salary >= 30000 and experience >= 2

print("\nBonus Eligibility:", eligible)

# mini-project 2 - Employee Salary Slip

print("===== Employee Salary Slip =====")

name = input("Enter Employee Name: ")

basic = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))
pf = float(input("Enter PF: "))

gross = basic + hra + da
net = gross - pf

print("\n===== Salary Slip =====")
print(f"Employee : {name}")
print(f"Basic    : {basic}")
print(f"HRA      : {hra}")
print(f"DA       : {da}")
print(f"PF       : {pf}")
print(f"Gross    : {gross}")
print(f"Net      : {net}")
