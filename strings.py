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
string = "     random string  .    "
print(string)
print(string.strip())

#rstrip & lstrip
print(string.rstrip())
print(string.lstrip())

#split 
sentence = "this is a dog; of brand; German Shepherd"
print(sentence.split(';'))

#title
print(sentence.title())

#replace 
student = "Hello world"
print(student.replace("l","k"))
# print(student.index("x"))
print(student.find("x"))
print(student.count('H'))
print(student.startswith("Helo"))
print(student.endswith("s"))
print(student.isupper())
print(student.islower())
print(student.istitle())

first_name = "Ken"
last_name = "Mugambi"
value = f"{first_name} {last_name} is a student"
print(value)
print("This is a statement from Ken Mugambi ")
print(f"This is a statement from {first_name} {last_name}")


