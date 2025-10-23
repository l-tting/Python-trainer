#slide 27 - no.2
sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:23])
            #only display “Clinton forces”
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])


#no-4
# Clean up and display Full name i.e John Doe
first_name="  Joh.n"  
last_name="   Do,e" 

f_name1 = first_name.strip()
#Joh.n
f_name2 = f_name1[0:3] + f_name1[-1]
print(f_name2)

f_name3 = f_name1.replace(".","")
print(f_name3)
l_name1 = last_name.strip()
print(l_name1)
l_name2 = l_name1.replace(",","")
print(l_name2)

full_name = f_name2 + " " + l_name2
print(full_name)


#Manipulate it to display EW 
r = '["E","W","C"]' 
value = r[2] + r[6]
print(value)


# slide 30
# #no.4
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
# NB: Use string  slice & concatenation, but have result as float 

#method 1
temp=56.8926
x = str(temp)
"56.8926"

y = x[3] + "." + x[4:]
print(y)
print(type(y))
z = float(y)
print(z)
print(type(z))


#method2
temp = 56.8926
x = temp * 10
print(x)
568.926 
y = str(x)
print(type(y))
z = float(y[2:])
print(z)
print(type(z))

a = 10


