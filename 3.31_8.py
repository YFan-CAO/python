list1=input().split()
list1=[eval(i) for i in list1]
dict1={}
 
for i in range(1,10):
    dict1[i]=0
    
for i in list1:
    dict1[i]=dict1.get(i,0)+1
    
list1=list(dict1.items())
 
for i in list1:
    print(i[0],i[1])
