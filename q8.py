# Write a program that takes as input the speed of a car e.g 80. 
# If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s 
# above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. 
# If the driver gets more than 12 points, the function should print: “License suspended”.

# 71 - 70 = 1 / 5 = 0.2 -> 0 + 1 12/5 -> 2.4 - 2 + 1 = 3


speed = float(input("Enter speed: "))
speed_limit = 70

if speed < 70:
    print("OK")
else:
    speed_exceeded = speed - speed_limit
    demerit_points = speed_exceeded // 5

    if speed_exceeded%5 != 0:
        demerit_points += 1
    if demerit_points > 12:
        print(f"Demerit points -> {demerit_points}")
        print("License suspended")
    else:
        print(f"Demerit points -> {demerit_points}")


   


