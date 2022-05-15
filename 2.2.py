def isPhoneNum(str):
    for i in str[0:3]:
        if i<='9' and i>='0':
            continue
        else:
            return False
    if str[3]!='-':
        return False
    for i in str[4:8]:
        if i<='9' and i>='0':
            continue
        else:
            return False
    if str[8]!='-':
        return False
    for i in str[9:13]:
        if i<='9' and i>='0':
            continue
        else:
            return False
    return True
message='Call me at 186-7123-4567 tomorrow. 027-8728-1235 is my office. '
for i in range(len(message)):
    chunk=message[i:i+13]
    if isPhoneNum(chunk):
        print('Phone number found: ' +chunk)
print('Done')
