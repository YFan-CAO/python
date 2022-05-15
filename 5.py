def fac(n):
    if n==1:
        return 1;
    else:
        return fac(n-1)*n

def fac1(n):
    s=1.0
    for i in range(n):
        s*=i+1
    return s
    
n=int(input(""))
m=int(input(""))
print("result:"+str(fac(n)/(fac(m)*fac(n-m))))
#print(str(fac1(n)/(fac1(m)*fac1(n-m))))3