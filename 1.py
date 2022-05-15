f=open("score1.txt","r")
tf=open("score2.txt","w")
tf.write("stuno \tname\tscore")
tf.write("\n")
line1=f.readline()
line = (f.readline()).strip()
n=0
ssum=0
s=[0,0,0,0,0]
while len(line)!=0:
    l=line.split()
    n+=1
    score=int(int(l[2])*0.3+int(l[3])*0.7)
    ssum+=score
    if score>90:
        s[0]+=1
    elif score>=80:
        s[1]+=1
    elif score>=70:
        s[2]+=1
    elif score>=60:
        s[3]+=1
    elif score<60:
        s[4]+=1
    tf.write(l[0]+"\t"+l[1]+"\t"+str(score)+"\n")
    line=f.readline()
print("total:{}".format(n))
print(">90:{}".format(s[0]))
print("80-89:{}".format(s[1]))
print("70-79:{}".format(s[2]))
print("60-69:{}".format(s[3]))
print("<60:{}".format(s[4]))
print("aver of class:{}".format(ssum//n))
f.close()
tf.close()
