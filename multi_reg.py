import math
x1=[]
x2=[]
y=[]

f=open('reg.txt','r')
x=f.read().split('\n')
lines=[]
del x[-1]
for i in x:
    lines.append(map(float,i.split('\t')))
#print lines
    
for i in lines:
    y.append(i[0])
    x1.append(i[1])
    x2.append(i[2])

n=len(lines)
sumx1=sum(x1)
sumy=sum(y)
sumx2=sum(x2)

pro=0

for i in range(n):
    pro+=x1[i]*y[i]
x1y=pro-(sumx1*sumy)/float(n)
#print x1y


pro=0

for i in range(n):
    pro+=x2[i]*y[i]
x2y=pro-(sumx2*sumy)/float(n)
#print x2y

pro=0
for i in range(n):
    pro+=x1[i]*x2[i]
x1x2=pro-(sumx1*sumx2)/float(n)

#print x1x2

pro=0
for i in range(n):
    pro+=x2[i]*x2[i]
x22=pro-(sumx2*sumx2)/float(n)
#print x22

pro=0
for i in range(n):
    pro+=x1[i]*x1[i]
x12=pro-(sumx1*sumx1)/float(n)
#print x12

pro=0
for i in range(n):
    pro+=y[i]*y[i]
y2=pro-(sumy*sumy)/float(n)
#print y2

b1=(x22*x1y-x1x2*x2y)/float(x12*x22-x1x2*x1x2)
#print b1
b2=((x12*x2y)-(x1x2*x1y))/float(x12*x22-x1x2*x1x2)
#print b2

a=sumy/float(n)-b1*sumx1/float(n)-b2*sumx2/float(n)
#print a
newx1=int(input("enter max. rainfall value (in mm): "))
newx2=int(input("enter avg. rainfall value (in mm): "))

ydash=a+b1*newx1+b2*newx2
print 'annual rainfall predicted is :',ydash,'mm'
