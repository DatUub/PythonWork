"""
Name: Ari Cartagena
Date: September 7, 2025
Assignment 1
"""

#Problem 1
word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12 = "All", "work", "and", "no", "play", "make", "Jack", "a", "dull", "boy", "who’s", "tired."
print(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12)

#Problem 2
prob2 = 6 * (1 - 2)
print(prob2)

#Problem 3
bruce = 6
print(bruce + 4)

#Problem 4
t = float(input("Number of years to compound the money: "))

p = 10000
n = 12
r = 0.08

a = p * (1 + r/n)**(n*t)

print(f"The final amount of dollars after {t} years will be: ${a:.2f}")

#Problem 5
"""
1. >>> 5 % 2 = 1
2. >>> 9 % 5 = 4
3. >>> 15 % 12 = 3
4. >>> 12 % 15 = 12
5. >>> 6 % 6 = 0
6. >>> 0 % 7 = 0
7. >>> 7 % 0 = Error
In the last example a divide by zero error occurs and the program stops.
"""

#Program 6
startTime = 2
timetoWait = 51
timetoAdd = timetoWait % 24
newTime = startTime + timetoAdd
print(f"Alarm will go off at {newTime}:00pm")

#Program 7
timeNow = int(input("Current time, in hours: "))
waitTime = int(input("Number of hours to wait: "))

newTime2 = (timeNow + waitTime) % 24
print(f"Alarm will go off at {newTime2}:00")