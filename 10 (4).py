def isRepeated(v):
    x=set(v)
    if len(x)==len(v):
        return False
    return True
n=input()
nums=n[1:len(n)-1]
num = [int(i) for i in nums.split(',')]
print(isRepeated(num))

