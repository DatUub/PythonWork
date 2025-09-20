"""
Name: Ari Cartagena
Date: September 20, 2025
Assignment 2
"""


#Problem 1
inputDay = int(input("Day (0-6)?"))
if inputDay == 0:
    print("Sunday")
elif inputDay == 1:
    print("Monday")
elif inputDay == 2:
    print("Tuesday")
elif inputDay == 3:
    print("Wednesday")
elif inputDay == 4:
    print("Thursday")
elif inputDay == 5:
    print("Friday")
elif inputDay == 6:
    print("Saturday")
else:
    print("Error: Enter valid day (0-6)")


#Problem 2
leaveDay = int(input("Day (0-6)?"))
sleepNums = int(input("How many nights of sleep?"))
returnDay = (leaveDay + sleepNums) % 7

if returnDay == 0:
    print("Sunday")
elif returnDay == 1:
    print("Monday")
elif returnDay == 2:
    print("Tuesday")
elif returnDay == 3:
    print("Wednesday")
elif returnDay == 4:
    print("Thursday")
elif returnDay == 5:
    print("Friday")
elif returnDay == 6:
    print("Saturday")
else:
    print("Error: Enter valid day (0-6)")


#Problem 3
'''
a <= b
a < b
a < 18 or day != 3
a < 18 or day == 3
'''


#Problem 4
'''
1. (3 == 3) = True
2. (3 != 3) = False
3. (3 >= 4) = False
4. (not (3 < 4)) = False
'''


#Problem 5
'''
Problem 5 Truth Table:

 p   q   r   (not (p and q)) or r
 F   F   F        T
 F   F   T        T
 F   T   F        T
 F   T   T        T
 T   F   F        T
 T   F   T        T
 T   T   F        F
 T   T   T        T
'''


#Problem 6
examMark = int(input("Exam mark: "))
if examMark >= 75:
    print("First")
elif examMark >= 70:
    print("Upper Second")
elif examMark >= 60:
    print("Second")
elif examMark >= 50:
    print("Third")
elif examMark >= 45:
    print("F1 Supp")
elif examMark >= 40:
    print("F2")
else:
    print("F3")
    
#Problem 7
# Determine square root of 2, multiply it by itself and compare to
# 2.0
a = 2.0 ** 0.5
print(a, a*a)
print(a*a == 2.0) # This prints False as the output since a*a is 2.0000000000000004 which isn't exactly 2.0 due to floating point precision limitations.

#Problem 8
a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

lhs = (a**2) + (b**2)
rhs = c**2

if abs(lhs - rhs) < 0.000001:
    print("Triangle is right angled")
else:
    print("Triangle is not right angled")