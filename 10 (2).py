
num=int(input())
for a in range(1,num):
    b=0;
    for i in range(1,a//2+1):
        if(a%i==0):
            b+=i
    c=0
    for j in range(1,b//2+1):
        if(b%j==0):
            c+=j
    if  a==c and a<b:
        print(a,b);
