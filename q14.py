# Write a program that takes input of 2 values and adds them. 
# The program should only accept numbers and floats only or otherwise
# display an error “invalid character entered” and take the user to re-enter the inputs .

#"2" "23.54" "-8" ,"-120.34" ------ "12.12.12", "-8-8" "100-"

#""
while True:
    value1 = input("Enter value 1: ")
    value2 = input("Enter value 2: ")

    if value1.count('-') > 1 or ('-' in value1[1:]):
        validity1 = False
    elif value1.count('.') > 1:
        validity1 = False
    else:
        temp1 = value1.replace('-','').replace('.','') 
        validity1 = temp1.isdigit()


    if value2.count('-') > 1 or ('-' in value2[1:]):
        validity2 = False
    elif value2.count('.') > 1:
        validity2 = False
    else:
        temp2 = value1.replace('-','').replace('.','') 
        validity2 = temp1.isdigit()


    if validity1 and validity2:
        num1 = float(value1)
        num2 = float(value2)
        sum = num1 + num2
        print("The sum is : ",sum)
        break #stop looping 
    else:
        print("invalid character entered")

        





