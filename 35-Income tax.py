ann_sal=int(input("Enter your salary="))
if ann_sal<250000:
    tax=0   #new variable
elif ann_sal<500000:
    tax=ann_sal*5/100
elif ann_sal<1000000:
    tax=12500+((ann_sal-500000)*20/100)
else:
    tax=112500+((ann_sal-1000000)*30/100)
print(f'Tax for income {ann_sal} is {tax}')