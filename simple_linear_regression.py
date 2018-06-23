import math
def reg():
    x1=[]
    y=[]

    f=open('reg.txt','r')
    x=f.read().split('\n')
    lines=[]
    del x[-1]
    for i in x:
        lines.append(map(int,i.split('\t')))
    print lines
        
    for i in lines:
        x1.append(i[0])
        y.append(i[1])
      

    n=len(lines)
    sumx1=sum(x1)
    sumy=sum(y)

    sx=0
    sy=0
    sxm=sumx1/float(n)
    sym=sumy/float(n)
    top=0
    bottom=0
    for i in range(n):
        top+=(x1[i]-sxm)*(y[i]-sym)
        bottom+=(x1[i]-sxm)**2
    b=top/float(bottom)
    a=sym-b*sxm
    print top
    print bottom


    print a
    print b
    newx1=int(raw_input("enter value for x1"))
    ydash=a+b*newx1
    print ydash
reg()
