person = {
    "name":"Alice",
    "age":24,
    "address":"123 Kimathi St",
    "married":False,
    "friends":["Jake","Natalie"],

}
print(person)
print(type(person))

#accessing dict values
print(person["name"])
print(person["age"])
print(person.get("married"))
print(person.get("friends"))

person["id"] = 25539892
person["age"] = 30
# print(person)
# {'name': 'Alice', 'age': 24, 'address': '123 Kimathi St', 
#  'married': False, 'friends': ['Jake', 'Natalie'], 'id': 25539892}

person.update({"name":"John Doe","married":True,"tech_stack":["Python","SQL"]})
# print(person)
# {'name': 'John Doe', 'age': 24, 'address': '123 Kimathi St', 'married': True,
#   'friends': ['Jake', 'Natalie'], 'id': 25539892, 'tech_stack': ['Python', 'SQL']}

print(person.keys())
print(person.values())
print(person.items())

#pop() - removes using key
person.pop("name")
print(person)
# {'age': 30, 'address': '123 Kimathi St', 'married': True, 'friends': ['Jake', 'Natalie'], 'id': 25539892, 'tech_stack': ['Python', 'SQL']}

#popitem() - removes the last item
person.popitem()
print(person)
# {'age': 30, 'address': '123 Kimathi St', 'married': True, 'friends': ['Jake', 'Natalie'], 'id': 25539892}

#clear()
person.clear()
print(person)
# {}


trainees = ["John", [2, ["James","Mary"]]]


print(trainees[1][1])
trainees.remove("John")
print(trainees)

trainees[0][1].remove("Mary")
print(trainees)

