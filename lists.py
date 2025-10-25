items = ["Mango","Apple","Banana",1,2,3]
print(items)
print(items[5])

items[0] = "Pear"
print(items)

print(items[1][2])

values = [1,2,3,[4,5,6,["x","y"]],[7,8,9],10]
print(values[3][3][0])

print(len(values))

#append
items = ["Mango","Apple","Banana",1,2,3]
items.append("Orange")
items.append(100)
items.append([80,90])
print(items)

#extend
items.extend([200,300,"peach"])
print(items)

#insert
items.insert(3,"One")
print(items)

#remove
items.remove("Mango")
print(items)

#pop
items.pop()
items.pop()
print(items)

items.pop(3)
print(items)

#clear
items.clear()
print(items)

#count
numbers = [10,20,20,30,40,50,20,5,12,1,3]
count = numbers.count(20)
print(count)

#index
i = numbers.index(20)
print(i)

#SORT
numbers.sort()
print(numbers)

letters = ["aa","xy","bb","f","d"]
letters.sort()
print(letters)

numbers.sort(reverse=True)
print(numbers)

letters.reverse()
print(letters)

#max & min
max_element = max(letters)
min_element = min(letters)
print(max_element)
print(min_element)

#copy
values = [1,2,3]
values2 = values.copy()
print(values2)


#joining lists
#1.concatenation
num1 = ["Jack","Jill"]
num2 = ["Joyce"]
num3 = num1 + num2
print(num3)

#2.extend
fruits = ["Mango","Pear"]
more_fruits = ["orange","apple"]
fruits.extend(more_fruits)
print(fruits)