# Mutable and Immutable Data Types in Python

# Note : In python every datatype is considers as objects...


# Immutable data types are those whose values cannot be changed after creation.
# Immutable types: int, float, str, tuple , boolean...

username = "Mayank"

username = "Rohit"


# print(username) ---> In the first username pointing to "mayank" but after we have change the memory refernce of username to "Rohit" so now it has start pointing to this name --> and after sometime python garbage collector will remove the fist name 



# x = 10
# y = x
# x = 20
# print("Immutable int:", y)  # Output: 10

# s = "hello"
# t = s
# s = "world"
# print("Immutable str:", t)  # Output: hello

# # Mutable types: list, dict, set
# lst = [1, 2, 3]
# lst2 = lst
# lst[0] = 100
# print("Mutable list:", lst2)  # Output: [100, 2, 3]

# d = {'a': 1}
# d2 = d
# d['a'] = 2
# print("Mutable dict:", d2)  # Output: {'a': 2}
