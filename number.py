x = 13
y = 5
add = x + y
print(add)
sub = y - x
print(sub)
div = x / y
print("Division: ",div)
floor = x // y
print("Floor: ",floor)
multi = x * y
print(multi)

expo = x ** y
expo2 = 2**3
print(expo)
print(expo2)

mod = x % y
print(mod)

temp = 56.8926

# 1) Convert to integer (rounded)
int_result = round(temp)   # 57
print(int_result)

# 2) Convert to 56.89 (2 decimal places)
two_decimals = round(temp, 2)   # 56.89
print(two_decimals)

# 3) Convert to 56.893 (3 decimal places, rounding)
three_decimals = round(temp, 3)  # 56.893
print(three_decimals)

# 4) Convert 56.8926 -> 8.926 using string slicing + concatenation, final result as float
s = str(temp)       # "56.8926"
# indices: 0:'5', 1:'6', 2:'.', 3:'8', 4:'9', 5:'2', 6:'6'
new_s = s[3] + '.' + s[4:7]   # '8' + '.' + '926' -> "8.926"
four_result = float(new_s)
print(four_result)
     # 8.926



