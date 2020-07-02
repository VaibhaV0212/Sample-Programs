l=[41,'nids','vaibs',5.2,587.5464]
str_l=[]
for i in l:
    if isinstance(i,str): #give true or false
        str_l.append(i)
print(str_l)