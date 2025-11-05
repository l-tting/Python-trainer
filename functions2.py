maths = float(input("Enter your Score: "))
eng = float(input("Enter your Score: "))
swa = float(input("Enter your Score: "))
sci = float(input("Enter your Score: "))
sos = float(input("Enter your Score: "))

def get_total(a,b,c,d,e): 
    return a + b + c + d + e

def get_average(value):
    return value / 5

def get_grade(avg):
    if avg > 70 and avg < 100:
        return "A"
    elif avg > 60 and avg < 79:
        return "B"
    elif avg > 50 and avg < 59:
        return "C"
    elif avg > 40 and avg < 49:
        return "D"
    elif avg < 40:
        return "E"
    else:
        return "Invalid Mark"

total_mark = get_total(maths,eng,swa,sci,sos)
average = get_average(total_mark)
# grade = get_grade(average)

print("Total mark is: ",total_mark)
print("Average mark is: ",average)
# print("Final grade is: ",grade)

