m=int (input())
n=int (input())
sum=m
for i in range(0,n):
    m=m/4
    sum=sum+m*2

print(round(sum-2*m,2))
print(round(m,2))
