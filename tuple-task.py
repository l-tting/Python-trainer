fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
new_fruits = list(fruits)
print(new_fruits)
print(type(new_fruits))

# new_fruits.remove("banana")
# new_fruits.remove("banana")
# new_fruits.remove("banana")
# print(new_fruits)

new_fruits.sort()
print(new_fruits)
new_fruits.pop(1)
new_fruits.pop(1)
new_fruits.pop(1)
print(new_fruits)

tuple_fruits = tuple(new_fruits)
print(tuple_fruits)
print(type(tuple_fruits))


names = ("Alice", "Bob", "Charlie", "David") 
new_names = list(names)

new_names.sort(reverse=True)
print(new_names)

tuple_names = tuple(new_names)
print(tuple_names)
print(type(tuple_names))
