from traceback import print_tb


list = []
flag=0
nums=input()
for i in nums:
    for j in list:
        if j==i:
            flag=1
            break
    list.append(i)
if(flag==1):
    print("yes")
else:
    print("no")
