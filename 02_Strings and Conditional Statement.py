# str1 = 'Hello, World!'
 # str2 = "hii Rishi"
# str3 = '''This is a multi-line string.   # escape characters can be used in multi-line strings.
# It can span multiple lines.'''


# concatenation of strings
# str4 = str1 + " " + str2    
# print(str4)  # Output: Hello, World! hii Rishi

#  length of a string
# length = len(str4)  
# print(length)  # Output: 27

# string indexing
# str = "Hello, World!"
# print(str[0])  # Output: H

# string slicing
# print(str[0:5])  # Output: Hello

# str[ starting_index : ending_index : step ]

# str5 = "Python Programming"
# print(str5[0:6])  # Output: Python
# print(str5[7:18])  # Output: Programming
# print(str5[::2])  # Output: Pto rgamn

# negative indexing
# print(str5[-1])  # Output: g    
# print(str5[-11:-1])  # Output: Programming

# string functions
# str6 = "   Python is a powerful programming language.   "
# print(str6.strip())  # Output: Python is a powerful programming language.
# print(str6.lstrip())  # Output: Python is a powerful programming language.   
# print(str6.rstrip())  # Output:    Python is a powerful programming language.
# print(str6.capitalize())  # Output:   python is a powerful programming language.  
# print(str6.replace("Python", "Java"))  # Output:    Java is a powerful programming language.

# WAP to take input from user and print the length of the name entered by user.
# name = input("Enter your name: ")
# print("length of your name is:", len(name))

# WAP to find  the occurrence of '$' in a string.

# str = "Hello, $World! This is a $test string with $dollar signs."
# print(str.count('$'))


# CONDITIONAL STATEMENTS

# if- elif-else(syntax)
# if condition:
#     # code to execute if condition is true


# age = 16

# if(age >= 18):
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# light  = input("Enter the color of the traffic light (red, yellow, green): ")

# if (light == "green"):
#     print("You can go.")

# elif (light == "red"):
#     print("You should stop.")  

# else:
#     print("You should slow down.")

# num = 5 

# if(num > 2):
#     print("Number is greater than 2.")  

# elif(num == 2):
#     print("Number is equal to 2.")

# else:
#     print("Number is less than 2.")   # indentation is important in python. It is used to define the blocks of code.

# print("end of the program.") 
 
        
# Student result system

# marks = int(input("Enter your marks: "))

# if (marks >= 90):
#     print("Grade: A")
# elif (marks >= 80 and marks < 90):
#     print("Grade: B")
# elif (marks >= 70 and marks < 80):
#     print("Grade: C")
# elif (marks >= 60 and marks < 70):
#     print("Grade: D")
# elif (marks >= 50 and marks < 60):
#     print("Grade: E")
# elif (marks >= 0 and marks < 50):
#     print("Grade: F")    

# else:
#     print("End of the program.")    

# nested if-else statements

# age = int(input("Enter your age: "))    

# if (age >= 18):
#     if (age >= 21):
#         print("You are eligible to vote and drink alcohol.")
#     else:
#         print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# Q) WAP  to check if a number entered by the user is odd or even.

# num = int(input("Enter a number: "))

# if (num % 2 == 0):
#     print("The number is even.")
# else:
#     print("The number is odd.")

# WAP to find the greatest of 3 numbers entered by the user.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: ")) 
# c = int(input("Enter third number: "))

# if (a >= b) and (a >= c):
#     print("The greatest number is:", a)
# elif (b >= a) and (b >= c):
#     print("The greatest number is:", b)
# else:
#     print("The greatest number is:", c)

# wap to check if a number is multiple of 7 or not.

# x = int(input("Enter a number: "))

# if (x % 7 == 0):
#     print("The number is a multiple of 7.")
# else:
#     print("The number is not a multiple of 7.")

#  match - case 
# day = int(input("Enter Day Number: "))

# match day:

#     case 1:
#         print("Monday")

#     case 2:
#         print("Tuesday")

#     case 3:
#         print("Wednesday")

#     case 4:
#         print("Thursday")

#     case 5:
#         print("Friday")

#     case 6:
#         print("Saturday")

#     case 7:
#         print("Sunday")

#     case _:
#         print("Invalid")


# match - case using choice

# choice = int(input("Enter Choice: "))

# match choice:

#     case 1:
#         print("Deposit")

#     case 2:
#         print("Withdraw")

#     case 3:
#         print("Balance")

#     case 4:
#         print("Exit")

#     case _:
#         print("Invalid Choice")

# smart ATM system

pin = int(input("Enter PIN: "))

if pin == 1234:

    print("""
    1. Balance
    2. Withdraw
    3. Deposit
    """)

    choice = int(input("Enter Choice: "))

    balance = 50000

    match choice:

        case 1:
            print("Balance =", balance)

        case 2:
            amount = int(input("Amount: "))

            if amount <= balance:
                print("Transaction Successful")
            else:
                print("Insufficient Balance")

        case 3:
            amount = int(input("Deposit Amount: "))
            balance += amount
            print("Updated Balance =", balance)

        case _:
            print("Invalid Choice")

else:
    print("Invalid PIN")