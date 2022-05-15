def maxWord(s):
    maxword=''
    tempword=''
    n=len(s)
    i=s.find(' ') 
    s=s+' '
    while i>0:
        tempword=s[:i]  
        if len(maxword)<len(tempword):
            maxword=tempword
        s=s[i+1:]       
        i=s.find(' ')
    return maxword

s=input("")
print(maxWord(s))
