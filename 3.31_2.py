n=int(input())
max=0
if n<=1:
    print("illegal input")
else:
    for i in range(1,n+1):
        if i*(n-i)>max:
            max=i*(n-i)
    print(max)
