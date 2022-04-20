(a,b,c,d)=eval(input('four scores:'))
sum=a+b+c+d
if a<60 or b<60 or c<60 or d<60 or sum<340:
    print('not')
else:
    if sum>=370:
        print('free')
    else:
        print('pay')
