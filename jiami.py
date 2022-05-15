import random
random.seed(10)
def posCode(str_len):
    index_ls = [i for i in range(1, str_len + 1)]
    random.shuffle(index_ls)
    return index_ls
def changeCode(s,poscode):
    poscode = [i-1 for i in poscode]
    result = ''
    for i in poscode:
        result+=s[i]
    return result

s = input()
poscode = posCode(len(s))
pos = ''
for i in poscode:
    pos+=str(i)
print(pos)
result = changeCode(s,poscode)
print(result)
