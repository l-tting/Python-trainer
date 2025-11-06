x = 123
y = 2
z = x + y
print(z)

a = 12
b = 20
c = a + b
print(c)


def add_numbers():
    x = 10
    y = 9
    z = x + y
    return z

sum = add_numbers()
print(sum)

def add_numbers(x, y):
    return x + y

sum1 = add_numbers(1,2)
sum2 = add_numbers(3,4)
sum3 = add_numbers(5,6)
sum4 = add_numbers(7,8)
sum5 = add_numbers(10,20)
print(sum1)
print(sum2)
print(sum3)
print(sum4)
print(sum5)


def string():
    return "Hello Martin!"
message = string()
print(message)

def string2():
    return "Tech camp kenya"


name = (input("Enter name: "))
if name == string2:
    print(name)
else:
    print("error")




