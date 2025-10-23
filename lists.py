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