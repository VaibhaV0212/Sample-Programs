print('Enter 3 angles')
#a,b,c=input(),(input(),input()
a=int(input())
b=int(input())
c=int(input())
if a+b+c!=180:
    print('Nahi banega')
else:                               #nested if
    if a>90 or b>90 or c>90:
        print('Obtuse triangle')
    elif a==b==c==60:
        print('Equilateral triangle')
    elif a==b or b==c or c==a:
        print('Isoceles triangle')
    else:
        pass
'''
elif islie nahi lagaya wrna else lagana padta
'''