x = input('Please input a integer:')[::-1]
odd = 0  # 奇数
even = 0  # 偶数
for i in range(1,len(x)+1):
    if i%2==1:
        odd += int(x[i-1])
    else:
        even += int(x[i-1])
print(odd)
print(even)
if (even - odd)%11 == 0:
    print('TRUE')
else:
    print('FALSE')
