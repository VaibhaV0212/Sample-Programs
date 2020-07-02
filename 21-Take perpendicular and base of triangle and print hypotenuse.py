import math
p= int(input('Enter perpendicular: '))
b= int(input('Enter base: '))
#h*h=p*p+b*b
h=math.sqrt(p*p+b*b)  #p**2+b**2
print(f'Hypotenuse is : {h}')