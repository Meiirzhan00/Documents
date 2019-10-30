class Company:
    sum=0
    d=0
    def __init__(self):
        sett=set(".0123456789")
        s=[]
        mzp=42500
        sum=0
        x=input("Jalaky engiziniz: ")
        if len(set(x)-sett)!=0:
            print("kayta engiz")
        elif '.' in x:
            print("Kayta engiz")
        else:
            s.append(int(x))
            for i in range(len(s)):
                 opv=int(s[i])*0.1
                 ipn=(int(s[i])-opv-mzp)*0.1
                 so=(s[i]-opv)*3.5
                 sn=(s[i]-opv)*9.5
                 ms=s[i]*1.5
                 z=opv+ipn
                 Company.d=so+sn+ms
                 y=int(s[i])-(opv+ipn)
            tabis.append(int(y))
        for item in range(len(tabis)):
            Company.sum+=int(tabis[item])
        print("taza tabis={} \ttaza tabistin sum={} ".format(tabis,Company.sum))

    def method(task):
        t=int(input("Компания табысы: "))
        sh=int(input("Компания шығыны: "))
        nal=t*0.03
        nal1=(t-sh)*0.1
        jsh=(nal+nal1)
        jt=t-jsh-Company.sum-Company.d
        print("налог: {}\nЖалпы компания табысы: {} sum ={}".format(int(jsh),int(jt),int(Company.sum)))

c=Company()
c.method()