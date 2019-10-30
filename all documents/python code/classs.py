##class Name:
##    def __init__(self,name):
##        self.name=name
##c=Name(['Tom','Bob','Alisa'])
##c1=c.name
##for i in c1:
##    print(i)
##print(c1)
##
class Name1:
    def __init__(self,name):
        self.name=name
    def __getitem__(self,item):
        return self.name[item]
    def __len__(self):
        return len(self.name)
    def __str__(self):
        return ','.join(self.name)
    
c2=Name1(['Meiirzhan','Nurzhan','Bekzhan'])
print(c2)

class Name2:
    def __init__(self,number):
        self.number =number
    def __abs__(self):
        return abs(self.number)
c3=Name2(-7)
print(abs(c3))

