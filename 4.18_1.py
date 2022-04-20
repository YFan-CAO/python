def happy1(num):
    numStr=str(num)
    sum=0
    for i in numStr:
        sum += int(i)**2
    return sum


n = input() 
happy2 = eval(n)
while happy2 != 1 and happy2 != 4: 
    happy2 = happy1(happy2)
else:
    if happy2 == 1:
        print("yes")
    else:
        print("no")
