value = input("Enter string: ")

def reverse_string(string):
    return string[::-1]

reversed = reverse_string(value)
print(reversed)


list1 = [1,2,3,4,5,6,7,8,9,10]

def get_even(list):
    even = []
    for i in list:
        if i%2 == 0:
            even.append(i)
    return even

even_numbers = get_even(list1)
print(even_numbers)
[2, 4, 6, 8, 10]


def get_squares():
    squares = []
    for i in range(1,31):
        squares.append(i**2)
    return squares

squares = get_squares()
print(squares)

