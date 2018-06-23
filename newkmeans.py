import math,csv
import copy
def dist(a,b):
    x=b[1]-a[1]
    y=b[2]-a[2]
    return math.sqrt(x*x+y*y)


def calcmean(i,curcluster,curmean,points):
    xsum=0
    ysum=0
    cou=0
    for x in range(len(curcluster)):
        if curcluster[x]==i:
            cou+=1
            xsum+=points[x][1]
            ysum+=points[x][2]
    curmean[i][1]=xsum/cou
    curmean[i][2]=ysum/cou

#x=int(raw_input())

def km(points,x):
    k=x+1
    while(k>x):
        try:
            k=int(raw_input("Enter number of clusters to be created (<"+str(x)+")  : "))
        except NameError:
            print "FIELD EMPTY!"
        except ValueError:
            print "WRONG VALUE!"
        if k > x:
            print "The maximum number of clusters that can be made is ",x


    curcluster=[]
    curmean=[]
    for i in range(x):
        curcluster.append(-1)
    s=[]
    for i in range(k):
        s.append(i)
        curcluster[i]=i
        curmean.append(list(points[i]))
    while True:    
        prevcluster=copy.deepcopy(curcluster)
        prevmean=copy.deepcopy(curmean)
        for i in range(x):
            mindist=9999
            dists=[]
            for j in range(k):
                dists.append(dist(list(points[i]),list(curmean[j])))
            
            ind=dists.index(min(dists))
            curcluster[i]=ind
            calcmean(ind,curcluster,curmean,points)
        if curmean==prevmean:
            break
    print "current mean: "
    
    print curmean
    print "current clusters: "
    print curcluster
            

with open("kmeansdata.csv") as dataset:
    trans=list(csv.reader(dataset,delimiter=','))
districts={}

for i in trans:
    districts[i[1]]=[]

for i in trans:
    p_temp=[]
    if( i[-1]=='0' and i[-2]=='0'):
        continue

    p_temp.append(float(i[-2]))
    p_temp.append(float(i[-1]))
    districts[i[1]].append(p_temp)
"""
for i in districts:
    
    print ("printing for district: ",i)
    km(districts[i],len(districts[i]))
"""
dsts=[]
for i in districts:
    jj=0
    jd=0
    for j in districts[i]:
        jj+=j[0]
        jd+=j[1]
    jj/=len(districts[i])
    jd/=len(districts[i])
    dsts.append([i,jj,jd])
    

km(dsts,len(districts))
print dsts


