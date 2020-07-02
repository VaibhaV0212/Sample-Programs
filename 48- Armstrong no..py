'''
abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
Example:

Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9
'''

a = 153
c = 0
while a>0:
    b = a%10
    c = a + pow(a)  #integer division
    a = a//10
if a=c:
    
