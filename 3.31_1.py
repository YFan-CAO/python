def get_tuple(num_list):
    temp_list = []
    for i in num_list:
        if (9 - i) in num_list:
            min_ = (9 - i) if (i >= (9 - i)) else i
            max_ = i if min_ == (9 - i) else (9 - i)
            if (min_, max_) not in temp_list:
                temp_list.append((min_, max_))
    return temp_list


nums = input("numbers:")
# 列表推导式
num_list = [int(i) for i in nums.split(',')]
result_list = get_tuple(num_list)
# 按列表里每个元组的第一个元素从小到大排序
result_list = sorted(result_list, key=lambda x: x[0])
print(result_list)
