f1=1
f2=1
n=int(input(">"))
i=0
while i<n-2:
    a=f1+f2
    f1=f2
    f2=a
    i=i+1
print(f2)