y=input("Таза жалақыны енгізіңіз: ")
a=y.split(',')
s=[]
t=[]
for each in a:
    set_split=set(each)
    sum2=0
    for i in set_split:
        sum2+=1
    if len(set_split)==sum2:
        s.append(each)
print("\n Таза жалақы мөлшері: ---> {}".format(s))
for i in range(len(s)):
    x=(100*int(s[i])-425000)/81
    t.append(int(x))
print("\n Қызметкерлерге берілетін жалақы : ---> {}".format(t))
