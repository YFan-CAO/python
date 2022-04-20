#n<=num n%3=2 n%5=1 n%7=0 
num=int(input())
for n in range(1,num):
    if n%3==2  and n%5==1 and n%7==0:
        print(n,end=' ') 