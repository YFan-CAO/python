def isHui(s):
    f=True
    n=len(s)
    for i in range(n):
        j=n-1-i                #j为i的对称位置
        if s[i:i+1]!=s[j:j+1]: #当前位置i与对称位置j
            f=False
            break
    return f
    
n=input("")
if isHui(n):
    print("True")
else:
    print("False")
