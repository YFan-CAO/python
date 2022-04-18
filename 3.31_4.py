a=eval(input('number:'))
list1=[]
for i in range(2,a):
    if a%i==0:
        list1.append(int(i))
        list1.append(int(a/i))
list1=list(set(list1))
if len(list1)==0:
    print('%d is prime'%a)
else:
    print(list1)
