class shishu:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def  add(self):
        return self.x+self.y
    def  sub(self):
        return self.x-self.y


s1=input()
s2=input()
start1=s1.find('+')
end1=s1.find('i')
start2=s2.find('+')
end2=s2.find('i')
a=shishu(int(s1[0:start1]),int(s2[0:start2]))
b=shishu(int(s1[start1+1:end1]),int(s2[start2+1:end2]))
print(str(a.add())+'+'+str(b.add())+'i')
if(b.sub()<0):
    print(str(a.sub())+'-'+str(b.sub())[1:]+'i')
else:
    print(str(a.sub())+'+'+str(b.sub())+'i')
    
