f=open('d1.txt')
dict1={}
list1=[]
for i in f:
    (a,b)=i.split(' ',1)
    if 90<=eval(b):
        dict1[a]='A'
    elif 80<=eval(b)<90:
        dict1[a]='B'
    elif 70<=eval(b)<80:
        dict1[a]='C'
    elif 60<=eval(b)<70:
        dict1[a]='D'
    else:
        dict1[a]='E'
list1=list(dict1.items())
list1.sort(key=lambda x:(eval(x[0]),x[1]))
new=open('d2.txt','w')
count=0
for i in list1:
    print(i[0]+' '+i[1])
    if i[1]=='E':
        count+=1
new.writelines(str(count))
new.close()
f.close()