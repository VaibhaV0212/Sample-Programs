'''
Compound Interest = P(1 + R/100)r
Where,
P is principle amount
R is the rate and
T is the time span
'''

#import math
P=int(input('Enter the principle amount = '))
R=int(input('Enter the rate = '))
T=int(input('Enter the time = '))
CI= P*(pow((1 + R / 100), T))
print("Compound Interest is = ", CI)