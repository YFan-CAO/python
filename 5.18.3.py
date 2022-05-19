file=open(r"movie.txt",encoding="UTF8")
m=file.readlines()
num=[]
for i in range(1,len(m)):
    m[i]=m[i].strip()
    m[i]=m[i].split()
    if int(m[i][5])<=90:
        num.append(m[i][0])
file.close()
f=open("out.txt","w")
for i in num:
    f.write(i+"\n")
f.close()
