# list

marks = [85, 90, 78, 92, 88]
print(marks)
print(type(marks))
print(marks[0])  # Accessing the first element
print(len (marks))  # Length of the list

students = ["Rushi", 95.5, 19, "Pune"]
print(students[0])  # Accessing the first element
print(students[1])  # Accessing the second element
print(students[2])  # Accessing the third element
print(students[3])  # Accessing the fourth element
students[0] = "Sneha"  # Modifying the first element
print(students[0])  # Accessing the modified first element

print(students)

# list slicing

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5])  # Slicing from index 2 to 4


# list methods

marks = [85, 90, 78, 92, 88]
print(marks)
marks.append(95)  # Adding an element to the end of the list
print(marks)
marks.insert(2, 80)  # Inserting an element at index 2
print(marks)
marks.remove(78)  # Removing the first occurrence of 78
print(marks)
marks.pop()  # Removing the last element
print(marks)    
marks.sort()  # Sorting the list in ascending order
print(marks)
marks.reverse()  # Reversing the list
print(marks)

# tuple

# tuple is immutable, meaning its elements cannot be changed after creation

tuple = (1, 2, 3, 4, 5)
print(tuple)
print(type(tuple))
print(tuple[0])  # Accessing the first element

# tuple slicing
print(tuple[1:4])  # Slicing from index 1 to 3
print(len(tuple))  # Length of the tuple
print(tuple.count(2))  # Counting occurrences of 2

# q] WAP to ask the user to enter name of 3 favorite movies & store them in a list.

movies = []
movies.append(input("enter 1st movie name: "))
movies.append(input("enter 2nd movie name: "))
movies.append(input("enter 3rd movie name: "))
print(movies)

# q] WAP to check if a list contrains a palindrome of elements.

list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 4, 5]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("list1 is a palindrome")
print(list1)
