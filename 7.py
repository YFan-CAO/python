f=open("in162.txt","r")
data=f.read().split(' ')
n=0
for i in data:
    n+=float(i)
n*=0.454
tf=open("out162.txt","w")
tf.write(str(n))
f.close()
tf.close()
