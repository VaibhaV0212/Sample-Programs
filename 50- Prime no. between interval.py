'''
Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
 The first few prime numbers are {2, 3, 5, 7, 11, ….}.

The idea to solve this problem is to iterate the val from start to end using a for loop and for every number,
 if it is greater than 1, check if it divides n. If we find any other number which divides, print that value.

'''

start = 1
end = 10
for val in range(start,end):
    if val>1:
        for n in range(2,val):
         if (val % n) == 0:
             break
        else:
            print(val)
'''
start = 11
end = 25

for val in range(start, end + 1):  
    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            print(val)
'''