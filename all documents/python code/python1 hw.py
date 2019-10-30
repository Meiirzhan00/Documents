res=""
name=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        name.append(i)
print(len(name))
for i in range(len(name)-1):
    res+=str(name[i]) + ","
print(res+str(name[-1]))
