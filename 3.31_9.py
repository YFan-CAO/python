a=input()
dict1={}
for t in a:
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a=a[:i]+a[i+1]+a[i]+a[i+2:]
for i in a:
    dict1[i]=dict1[i]+1 if i in dict1 else 1
max1=0
for i in dict1:
    if dict1[i]>max1:
        max1=dict1[i]
for i in dict1:
    if dict1[i]==max1:
        print(i,dict1[i])
