s=["Meiirzhan"]
j=[]
for item in s:
    f=len(item)
    for i in range(1,f+1):
        d=s[0][i-1:i].split()
        j.append(d)
    print(j)
