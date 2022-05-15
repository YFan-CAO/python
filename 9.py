f=open("temp.txt","r")
l=list()
line=(f.readline()).strip()
while len(line)!=0:
    l.append(line.split())
    line=(f.readline()).strip()
maxn=0
minn=1000
count=0
for i in range(len(l)):
    maxn=int(l[i][1]) if int(l[i][1]) > maxn else maxn
    minn=int(l[i][2]) if int(l[i][2]) < minn else minn
    if (int(l[i][2])+int(l[i][1]))//2<10:
        count+=1
for i in range(len(l)):
    if  int(l[i][1]) == maxn :
        s1=l[i][0]
    elif int(l[i][2]) == minn :
        s2=l[i][0]
print("Highest Temperature:{},{} Celsius".format(s1,maxn))
print("Lowest Temperature:{},{} Celsius".format(s2,minn))
if count<5:
    print("Not in winter")
f.close()
