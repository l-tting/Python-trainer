# Write a program that displays a numbers 1 to 50 inside a list.
numbers = []
for i in range(1,51):
   numbers.append(i)
print(numbers) 
    

list2 = []
for number in numbers:
   if number%5 == 0 or number%7 ==0:
      list2.append(number)
print(list2)


list3 = []
for x in list2:
   
   if x%2 == 0:
      list3.append(x)
print(list3)




ls1 = [ ("Jay", "20"), ("Mo", "30"), ("Mya", "32") ]
sum = 0
for i in ls1:
   sum += int(i[1])

print(sum)
    
even = []
for x in range(1,51):
   if x%2 == 0:
      even.append(x)

print(even)
count = len(even)
print(count)
   



   


