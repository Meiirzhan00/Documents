sett=set(".0123456789")
s=[]
tabis=[]
mzp=42500
while True:
    x=input("Jalaky: ")
    if len(set(x)-sett)!=0:
        if x in ["ok","Ok","OK","oK"]:
            break
        print("kayta engiz")
    elif '.' in x:
        print("Kayta engiz")
    else:
        s.append(x)
    for i in range(len(s)):
         opv=int(s[i])*0.1
         ipn=(int(s[i])-opv-mzp)*0.1
         z=opv+ipn
         y=int(s[i])-(opv+ipn)
    tabis.append(int(y))
print("taza tabis={}\ns={}\nopv={}\nipn={}\njalaky: {}".format(tabis,s,int(opv),int(ipn),int(y)))