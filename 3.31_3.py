a=input('please input text:')
for S1 in a:
    if 65<=ord(S1)<=85 or 97<=ord(S1)<=117:
        n=ord(S1)+5
        new=chr(n)
    elif 86<=ord(S1)<=90 or 118<=ord(S1)<=122:
        n=ord(S1)-21
        new=chr(n)
    else:
        new=S1
    print(new,end="")
