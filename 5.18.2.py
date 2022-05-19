from pickle import FALSE
file = open('in.txt', 'r')
list=[]
for line in file:
    list.append(line.replace('\n', '') )
n=input()
m=int(float(n))
if m <0 or n.find(".")!=-1 or float(n)!=float(int(n)):
    print("illegal input")
else:
    w=0
    for i in range(0,int(n)):
        if list[i][0]=='A':
            print(list[i])
            w+=1
    if w==0:
        print("not found")
