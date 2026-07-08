# # ===== FOR LOOP EXAMPLES =====

# # For loop with range
# print("For loop with range:")
# for i in range(5):
#     print(i)

# print()

# # For loop with list
# print("For loop with list:")
# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(fruit)

# print()

# # For loop with string
# print("For loop with string:")
# word = "Python"
# for letter in word:
#     print(letter)

# print()

# # ===== WHILE LOOP EXAMPLES =====

# # Simple while loop
# print("Simple while loop:")
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# print()

# # While loop with condition
# print("While loop with condition:")
# num = 10
# while num > 0:
#     print(num)
#     num -= 2

# print()

# # ===== LOOP CONTROL =====

# # Break statement
# print("Break statement (stop loop):")
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# print()

# # Continue statement
# print("Continue statement (skip iteration):")
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)


# while loop 
# count = 1
# while count <=5 :
#     print("hello")
#     count += 1

# i = 1
# while i <= 10:
#     print("I LOVE YOU SNEHA") 
#     i+=1

# print numbers from 1 to 5
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# print("end")    

# 1 -- print numbers from 1 to 100.

# i = 1 
# while i <= 100:  # stopping condition
#     print(i)
#     i += 1

# print numbers from 100 to 1.

# i = 100
# while i >= 1 :  # stopping condition
#     print(i)
#     i -= 1

# # print the multiplication table of a numbers n.
# n = int(input("enter num: "))
# i =1 
# while i <= 10:
#     print(n*i)
#     i += 1

# print list 
# nums = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(nums):
#   print(nums[idx])
#   idx += 1

# search for a number x in this tuple using loop.

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0 

# while i < len(nums):
#     if(nums[i] == x):
#         print("found at idx",i)
#     else:
#         print("finding...")    
#     i += 1    
 

# keyword - break and continue

# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break 
#     i += 1

# print("end the loop")    

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0 

# while i < len(nums):
#     if(nums[i] == x):
#         print("found at idx",i)
#         break 
#     else:
#         print("finding...")
#     i += 1
# print("end loop")            
     
# continue

# i = 0 
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue # skip
#     print(i)
#     i += 1


# for loop -- for loops are used sequential traversal.list,tuple ,string etc.

# nums = [1,2,3,4,5]

# for val in nums:
#     print(val)

# tup = (1,2,3,4,5,2,4,8,9)

# for num in tup:
#     print(num)

# str = "RushiBhosale"

# for char in str:
#     if(char == 'o'):
#         print("o found")
#         break
#     print(char)

# else:
#     print("end")    

# q] print the elements of the following list using a loop .
# [1,4,9,16,25,36,49,64,81,100]

# ele = (1,4,9,16,25,36,49,64,81,100)
# for val in ele:
#     print(val)
   
#  q2 linear search 

#     ele = (1,4,9,16,25,36,49,64,81,100)
# x = 49
# idx = 0
# for val in ele:
#     if(val == x):
#         print("number found at idx",idx)
#     print(val)
#     idx += 1

# range() - range function returns a sequence of numbers.

# seq = range(5)

# for i in seq:
#     print(i)
   
# for i in range(10):   # range(stop)
#     print(i)

  
# for i in range(2,10):   # range(start,stop)
#     print(i)


# for i in range(2,100,2):   # range(start,stop,step)
#      print(i)

# multiplication table 
# n = int(input("enter number: "))

# for i in range(1,11):
#     print(n*i)


# pass statement 

# for i in range(5):
#     pass
# print("end")

# wap to find the sum of first n numbers .(using while)

# n = 56
# sum = 0 
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# for i in range(1,n+1):
#     sum += i

# print("total sum",sum)  

# wap to find the factorial of first n numbers,(using for)

# using for loop 

# n = 5 
# fact = 1
# 
# for i in range(1,n+1):
#      fact *= i
#      i += 1
# print("factorial = ",fact)  


# using while loop 

# n = int(input("enter num : "))
# fact = 1
# i = 1
# while i <= n:
#      fact *= i
#      i += 1

# print("factorial = ",fact)     