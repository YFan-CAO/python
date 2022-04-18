a=eval(input())
b=2
n=1
while b<a:
    b=b+(0.98**n)*2
    n=n+1
print(n)
