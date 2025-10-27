numbers = {100,34,34,67,78,"twenty"}
print(numbers)
print(type(numbers))

print(100 in numbers)
#add()
numbers.add("five")
print(numbers)

#update()
numbers.update([1000,2000])
print(numbers)

#remove()
numbers.remove(100)
print(numbers)

#discard()
numbers.discard(1000)
print(numbers)

numbers.discard(10000)
print(numbers)

#clear
numbers.clear()
print(numbers)

fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
new_fruits = set(fruits)
print(new_fruits)

tuple_fruits = tuple(new_fruits)
print(tuple_fruits)