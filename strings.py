#string concatting
first_name = "Jane"
second_name = "Doe"
full_name = first_name + " " + second_name
print(full_name)

#indexing
actor = "Jack  Nicholson"
print(actor[7])
print(actor[-2])

#slicing
portion = actor[0:8]
print(portion)
print(actor[-4:-1])
print(actor[11:])

#length of a string
text = "This is a random string"
length = len(text)
print(length)


y = "Name"
print(y.upper())

b = "TEXT"
print(b.lower())

#strip - remove whitespaces
string = "     random string"
print(string)
print(string.strip())
