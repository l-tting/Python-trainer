# Write a program that takes the date of birth of a person and the program outputs
# the age in terms of years,months,days TODAY.datetime
dob = input("Enter dob in the format YYYY-MM-DD: ")

dob_parts = dob.split("-")
print(dob_parts)

['1991', '04', '23']
year_born = int(dob_parts[0])
month_born = int(dob_parts[1])
day_born = int(dob_parts[2])

today = input("Enter the date today YYYY-MM-DD: ")
# 2025-11-03

today_parts = today.split("-")
print(today_parts)
['2025', '11', '03']

current_year = int(today_parts[0])
current_month = int(today_parts[1])
current_day = int(today_parts[2])



#e.g dob(2005-12-10) ---- current_date(2025-11-03) ----person 1

years =  current_year - year_born
months = current_month - month_born
days = current_day - day_born
# 2025 - 2005 = 20 #years 
# 11 - 12 = -1 #months
# 3 - 10 = -7 #days

# 1-2-3-4-5-6-7-8-9-10-11-12

if days < 0:
    months -= 1
    #months = -2

    if current_month == 1:
        prev_month = 12
    else:
        prev_month = current_month - 1
    if prev_month in [1,3,5,7,8,10,12]:
        days += 31
        #DAYS = 24

    elif prev_month in [4,6,9,11]:
        days+= 30
    else:
        #ignoring leap years
        days+=28

if months < 0:
    months += 12
    #months = 10
    years -= 1
    #years = 19

print(f"Age is {years} years - {months} months - {days} days")