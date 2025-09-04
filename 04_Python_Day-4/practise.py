

# Mutable Datatype in python :-
# - List 
# - Dictionery
# - Sets
# - ByteArray


# List
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# mylist = ["apple", "banana", "cherry"]
# print(mylist)

# List Items
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.


a = 23

# print(type(a))

# print(type(str(a)))   --> string
# print(type(int("a")))   --> Cannot convert to intefer

# b = input("Enter name") --> It is used to take input from the user...
# print("You entered:", b)

# a = 21 
# b=33
# print("Sum", a+b)


# b = input("Enter the number")
# c = input("Enter z")

# d = int(b)/int(c)

# print(d)

# a = 34
# b = 80


# if( a >= b):
#     print("a is greater")
# else:
#     print("a is smaller")


# a = 'Mayank'
# b = "Mayank"
# c= '''Mayank'''

# print(a)
# print(b)
# print(c)



#  String in Python


# sl = a[2:4]
# print(sl)
# print(a)
# print(a[-2])


# word = "amazing"
# print(word[1:6:1])

# a= "mayank"

# print(a.replace("a","b"))

# name = input("Enter your name") 

# print("Good Afternoon, ", name)


# letter = '''Dear </name />
# '''

# print(letter)


# name = input("Enter you name: ")
# print(f"Good Afternoon, {name}")  --> f is consider as a f string in python using this we can easily add the variables inside the string


# letter = '''
#         Dear <|Name|>,
#         You are selected!
#         <|Date|>
#         '''

# print(letter.replace("<|Name|>", "Mayank").replace("<|Date|>", "25 sep 2025"))


# text ="This is a String"
# doubleSpace = "This is  a  double Spcace str"

# if("  " in doubleSpace):
#   doubleSpace.replace("  "," ")
#   print(doubleSpace)
# else :
#   print("No double space")


# Example of using find() in Python

str1 = "Hello this is mayank"

# find() returns the lowest index of the substring if found, otherwise -1
index = str1.find("is")
print(f"Index of 'is': {index}")  # Output: Index of 'is': 8

index_not_found = str1.find("ro")
print(f"Index of 'ro': {index_not_found}")  # Output: Index of 'ro': -1



#  Replace the double space in a string wih single space

