
file=open("d1.txt","r")
m=file.readlines()
num=[]
for i in range(0,len(m)):
    m[i]=m[i].strip()
    m[i]=m[i].split()
for i in range(0,len(m)-1):
    for j in range(0,len(m)-1-i):
        if int(m[j][0])>int(m[j+1][0]):
            temp=m[j]
            m[j]=m[j+1]
            m[j+1]=temp
a=0
for i in range(0,len(m)):
    if 90 <= int(m[i][1]) <= 100:
        print( str(m[i][0])+" "+'A')
        continue
    if 80 <=  int(m[i][1]) < 90:
        print( str(m[i][0])+" "+'B')
        continue
    if 70 <=  int(m[i][1]) < 80:
        print( str(m[i][0])+" "+'C')
        continue
    if 60 <=  int(m[i][1]) < 70:
        print( str(m[i][0])+" "+'D')
        continue
    if int(m[i][1]) < 60:
        print( str(m[i][0])+" "+'E')
        a+=1
f=open("d2.txt","w")
f.write(str(a))
