'''
The idea to solve this problem is to iterate through all the numbers starting
from 2 to (N/2) using a for loop and for every number check if it divides N.
If we find any number that divides, we return false.
If we did not find any number between 2 and N/2 which divides N then it means that N is prime and we will return True.

Input:  n = 11
Output: true

Input:  n = 15
Output: false

'''

n = int(input("Enter no.= "))
if n>1:
    for i in range(2,n//2):
     if n%i ==0:
        print("False")
        break
    else:
        print("True")