file=open("listin.txt","r")
m=file.readlines()
f=open('listout.txt', 'w')
n=int(input("表示冒号固定位置的整数为：\n"))
num=[]
list=[]
for l in m:
    n = l.find(':')
    l1 = ' '.join(l[:n].split())
    l2 = ' '.join(l[n + 1:].split())
    f.write(l1.rjust(40, ' ') + ' : ' + l2+ '\n')
