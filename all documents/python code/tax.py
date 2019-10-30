class Company:
    def method(self):
        sett=set(".0123456789")
        s=[]
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
                y=s[i]-(opv+ipn)
        print("опв={}\nипн={}\nөкіметке берешегі={}\nжалақысы:{}".format(int(opv),int(ipn),int(z),int(y)))
        print(s)

c=Company()
c.method()