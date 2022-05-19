from numpy import double
file = open('jisuan.txt', 'r')
list =[""]
l=[]
for line in file:
    list.append(line.replace('\n', '') )
file.close()
for i in list:
    c=0
    if i.find("+")!=-1:
       poi= i.index("+");
       a1=double(i[0:poi])
       a2=double(i[poi+1:len(i)])
       l.append('{:.2f}'.format(a1+a2))
       c+=1
    if i.find("-")!=-1:
       poi= i.index("-");
       a1=double(i[0:poi])
       a2=double(i[poi+1:len(i)])
       l.append('{:.2f}'.format(a1-a2))
       c+=1
    if c==0:
        l.append(i)
f = open('jieguo.txt', 'w')
for ss in range(1,len(l)):
    f.write(str(l[ss]+'\n'))
f.close()
