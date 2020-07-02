p=float(input('Enter principle : '))
r=float(input('Enter rate : '))
t=float(input('Enter time : '))
si=p*r*t/100
ci=p*(pow((1+r/100),t))
print('Simple Interest:',si,'\nCompound Interest',ci)