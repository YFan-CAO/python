def fac(n):
    if n == 0:
        return 1
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum



a, b = map(int, input().split())
c = fac(a)/(fac(b)*fac(a-b))
print("result:",round(c,1))

