def fz(n): #计算分子部分
    s=0.0
    for i in range(n):
        s+=i+1
    return s

def fm(n): #计算分母部分
    s=1.0
    for i in range(n):
        s *=i+1
    return s

def sum_(n): #计算公式的值
    s=0.0    
    for i in range(n):
       s+=fz(i+1)/fm(i+1)
    return s
n=int(input(""))
print('{:.4f}'.format(sum_(n)))
