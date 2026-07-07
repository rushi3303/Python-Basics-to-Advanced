# Dictionary & Set

# Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

# dict = {
    
#     "name": "Rushi",
#     "age": 22,
#     "city": "Pune",
#     "subjects": ["Maths", "Science", "English"],
#     "Topics": ("dictionary", "set"),
#     "is_student": True
# }
# print(dict)
# print(type(dict))
# print(dict["name"])  # Accessing the value associated with the key "name"
# print(dict.get("age"))  # Accessing the value associated with the key "age"
# print(len(dict))  # Length of the dictionary

# nasted_dict 

# student = {
#     "name": "Rushi",
#     "subjects": {
#         "Maths": 85,
#         "Science": 90,
#         "English": 78
#     }
# }
# print(student)
# print(student["subjects"]["Maths"])  # Accessing the value associated with the key "Maths" in the nested dictionary

#  dictionary methods

# print(student.keys())  # Getting all the keys in the dictionary
# print(student.values())  # Getting all the values in the dictionary
# print(student.items())  # Getting all the key-value pairs in the dictionary
# print(student.get("name"))  # Accessing the value associated with the key "name"
# print(student.pop("name"))  # Removing the key-value pair with the key "name"   


# SET IN PYTHON 
# SET is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.
# not allow duplicate values

# COLLECTION = {"apple", "banana", "cherry",1,2,2}
# print(COLLECTION)   


# collection = set()  # empty set

# print(type(collection))

# set methods

# collection = set()

# collection.add(1)
# collection.add(2)
# collection.add("Rushi")
# collection.add((1,2,3))

# print(collection)


# set1 = {1,2,3}
# set2 = {2,3,4}

# print(set1.union(set2))
# print(set1)
# print(set2)

# dictionary = {
#   "cat": "a small animal",
#   "table": ["a piece of furniture", "list of facts & figures"]
# }

# print(dictionary)


# subjects = {
#     "python","java","c++","python","javascript","java","python",
#     "java","c++","c"
# }

# print(subjects)


marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)