numbers=[".",'0','1','2','3','4','5','6','7','8','9']
sum2=0
newlist=[]
y=input("input your numbers: ")
a=y.split(',')
for each in a:
    set_split=set(each)
    sum2=0
    for i in set_split:
        if i in numbers:
            sum2+=1
    
    if len(set_split)==sum2:
        newlist.append(each)
    
print(newlist)

        