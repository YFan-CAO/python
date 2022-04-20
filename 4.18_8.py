a=eval(input())
b=1
c=1
if a!=int(a) or a<0:
    print('illegal data')
elif a==0:
    print(0)
else:
    for c in range(1,a):
        b=2*b+2
    print(b)
