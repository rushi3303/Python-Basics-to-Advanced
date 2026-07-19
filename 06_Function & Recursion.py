# function - block of statements that perform a specific task.
# syntax: 

# def func_name(param1,param2...):
#     # some work 
#     return val 

# func_name(arg1,arg2...)  # function call 

# def sum(a,b): 
#     sum = a + b
#     return sum 
# print(sum(2,3))

# def calc_sum(a,b): # parameters
#     return a + b

# sum = calc_sum(2,3)  # 5 # function call
# print(sum)

# def print_hello():
#     print("Hello")

# print_hello()    
# print_hello()    
# print_hello()    
# print_hello()    
# print_hello()    

# def calc_avg(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg 
# calc_avg(98,95,90)

# function in python - 1) built  in function 
                      #2) user defined function 

 # built-in function - print(),len(),type(),range()


# print("Hello",end=" ")  # sep = " "
# print("Rushi")  # end = "\n"

# default parameter 

# waf to print the length of a list .(list ids the parameter)
# cities = ["pune","nashik","chennai","mumbai"]
# heroes = ["thor","ironman","captain america","shaktiman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)    

# waf to print the elements of a list in a single line .(list is the parameter)
# cities = ["pune","nashik","chennai","mumbai"]
# heroes = ["thor","ironman","captain america","shaktiman"]

# def print_len(list):
#    print(len(list))

# def print_list(list):
#    for item in list:
#       print(item,end=" ")

# print_list(heroes)
# print_list(cities)

# waf to find the factorial of n .(n is the parameter )


# def cal_fact(n):
#    fact = 1 
#    for i in range(1,n+1):
#       fact *= i 
#    print(fact)

# cal_fact(6)

# waf to convert USD to INR.

# def converter(usd_val):
#    inr_val = usd_val * 83
#    print(usd_val, "USD =", inr_val, "INR")

# converter(2)


# recursion - when a function calls itself repeatedly.
# recursive functionn

# def show(n):
#     if(n == 0):  # base case 
#         return
#     print(n)
#     show(n-1)

# show(5)  
#   
# factorial 

# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     return fact(n-1) * n
# print(fact(4))

# write recursive function to calculate the sum of first n natural numbers .
# def calc_sum(n):
#     if(n == 0):
#         return 0

#     return calc_sum(n-1) + n


# sum = calc_sum(5) 
# print(sum)   

# write a recursive function to print all element in a list ( hint use list & index as parameter )

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","litchi","apple","banana"] 

print_list(fruits)