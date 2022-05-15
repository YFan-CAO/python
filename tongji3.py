#【问题描述】输入任意一个正整数，从1开始到这个数字的奇数序列里，统计一共出现了多少个3。
#编写函数sumThree()，实现功能是，输入一个正整数，返回该数中3出现的个数。
def sumThree(n):
    a=0
    for i in range(1,int(n)+1):
        if i % 2 != 0:
            a+=str(i).count("3")
    return a
x=input("number:")
print(sumThree(x))

