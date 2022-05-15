from calendar import isleap

def days(year,month):
    Feb=0
    if month==1 :
        return 31
    if month==0:
        return 0
    if isleap(year):
        Feb=60
    else:
        Feb=59
    

    if month==2:
        return Feb
    if month%2==1:
        return (month//2)*31+(month//2-1)*30+Feb
    if month%2==0:
        return (month//2-1)*31+(month//2-1)*30+Feb




def isLeap(year):
    if year%4==0:
        return 29
    else:
        return 30

a=input()
nums = [int(i) for i in a.split('/')]
if nums[0]!=2000:
    print(days(nums[0],nums[1]-1)+nums[2])
else:
    print(days(nums[0],nums[1]-1)+nums[2]+1)

