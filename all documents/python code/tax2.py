class Company:
    mem=0
    y=0
    nall1=0
    def __init__(self):
        sett=set(".0123456789")
        s=[]
        jalaky=[]
        tabis=[]
        mzp=42500
        sum=0
        nall=[]
        sum2=0
        while True:
            x=input("Өтінемін жалақыңызды енгізіңіз: ")
            a=x.split(" ")
            print(a)
            if len(set(x)-sett)!=0:
                if x in ["stop"]:
                    break
                print("/Қате шықты/ қайта енігізіңіз ")
            elif '.' in x:
                print("/Қате шықты/ қайта енігізіңіз ")
            else:
                s.append(int(x))
            for i in range(len(s)):
                 opv=int(s[i])*0.1
                 ipn=(int(s[i])-opv-mzp)*0.1
                 so=(s[i]-opv)*0.035
                 sn=(s[i]-opv)*0.095
                 ms=s[i]*0.015
                 Company.y=int(s[i])-(opv+ipn)
                 nald=so+sn+ms
            print("\nҚызметкер таза жалақысы: {}\t опв={}\t ипн={}\t со={}\t сн={}\t мед.стр={}\t Компания налогы: {}\n ".format(int(Company.y),int(opv),int(ipn),int(so),int(sn),int(ms),int(nald)))
            nall.append(int(nald))
            tabis.append(int(Company.y))
        for item1 in range(len(nall)):
            Company.nall1+=int(nall[item1])
        for item in range(len(tabis)):
            Company.mem+=int(tabis[item])
        print("\nҚызметкерлердің жалақысы: {}\t Қызметкерлерге берілетін жалақы: {}\t|  Компания жалпы налогы: {}\n ".format(s,Company.mem,Company.nall1))
    def method(task):
        t=int(input("\nКомпания табысы: "))
        sh=int(input("\nКомпания шығыны: "))
        nal=t*0.03
        nal1=(t-sh)*0.1
        jsh=(nal+nal1+Company.nall1+Company.mem)
        jt=t-jsh-sh
        print("\nКомпания шығыны: {}\t| Жалпы компания табысы: {} ".format(int(jsh),int(jt)))

c=Company()
c.method()
