_ = input()
a = input()
a = a.split()
mydict = {i:0 for i in a}  # 创建一个字典，用来统计第几次出现，将次数放在ans列表中
ans = []  # 创建一个列表，和输入的数据一一对应
for i in a:
    mydict[i]+=1  # 元素开始出现啦
    ans.append(str(mydict[i]))  # 将第几次出现放在字典里
print(' '.join(ans))
