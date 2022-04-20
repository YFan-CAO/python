def isVaildPassword(str):
    numfalg=0
    charflag=0
    fuhaoflag=0
    for n in str:
        if(n.isalpha()):
            charflag=1
        if(n.isdigit()):
            numfalg=1
        if n.isalpha()==False and n.isdigit()==False:
            fuhaoflag=1
    if 6<=len(str)<=12 and numfalg==1 and charflag==1 and fuhaoflag==1:

        print("True")
    else:
        print("False")


str=input()
isVaildPassword(str)

