items = ("Monday","Tuesday",12,False,100.78,"monday")
print(items)
print(type(items))

#accessing items in a tuple
print(items[1])
print(items[-2])

#determining the no of values in a tuple - length
print(len(items))

#index method - returns the position of a value
i = items.index(100.78)
j = items.index("Monday")
print(i)
print(j)

#count - returns the no of occurrences of an item in a tuple
no = items.count("Monday")
print(no)

