x = 100
y = 20

if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is lesser than {y}")


number = 4
if number%2 == 0:
    print("Number is even")
else:
    print("Number is odd")


value = float(input("Enter a number: "))
if value%2 == 0:
    print('Number is even')
else:
    print("Number is odd")


grade = float(input("Enter grade: "))
if grade >= 70 and grade <= 100:
    print("Grade is A")
elif grade >= 60 and grade <= 69:
    print("Grade is B")
elif grade >=50 and grade <= 59:
    print("Grade is C")
elif grade >=40 and grade <= 49:
    print("Grade is D")
elif grade >=0 and grade <= 39:
    print("Grade is E")
else:
    print("Invalid grade-Enter a no between 0 and 100")


password = input("Enter password: ")

correct_password = "123456"

if len(password) == 6:
    if password == correct_password:
        print("Correct Password")
    else:
        print("Wrong Password")
else:
    print("Password too short or too long")