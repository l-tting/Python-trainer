# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.

# x = float(input("Enter x: "))
# y = float(input("Enter y: "))
# z = float(input("Enter z: "))

# if x > y and x > z:
#     print("x is the largest")
# elif y > x and y > z:
#     print("y is the largest")
# else:
#     print("z is the largest")



# 5. Write a Python program that checks if a variable student_score is greater than 90. 
# If true, check if the attendance is greater than 80. If both conditions are true, 
# print "Excellent student", otherwise print "Good score, but attendance needs improvement"
#method 1
# student_score = float(input("Enter score: "))
# attendance = float(input("Enter attendance: "))

# if student_score > 90 and attendance > 80:
#     print("Excellent student")
# elif student_score > 90 and attendance < 80:
#     print("Good score, but attendance needs improvement")
# else:
#     print("Invalid score - score below 90")

# #method 2
# if student_score > 90:
#     if attendance > 80:
#         print("Excellent student")
#     else:
#         print("Good score, but attendance needs improvement")
# else:
#     print("Invalid score - score below 90")


# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."


account_type = input("Enter account type: ")
amount = float(input("Enter amount: "))


if account_type == "Standard":
    if amount > 500:
        print("Transaction exceeds limit for standard account")
    else:
        print("Transaction approved")
elif account_type == "Premium":
    if amount > 1000:
        print("transaction limit exceeded for premium account")
    else:
        print("Transaction approved")
else:
    print("Account type filled is neither Standard nor Premium")




