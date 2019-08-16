from math import sqrt
k=[[0,0],[3,4],[5,6],[0,2]]
def dist(A,B):
    return sqrt((k[A][0]-k[B][0])**2+(k[A][1]-k[B][1])**2)

def rundreisen(w,l):
    if len(l) < 2:
        w.append(l[0])
        w.append(0)
        print w
        s = 0
        for j in range(len(w)-1):
            s = s + dist(w[j],w[j+1])
        print("dist:", s)
        return 
    
    for s in l:
        cl = l[:]
        cl.remove(s)
        cw = w[:]
        cw.append(s)
        rundreisen(cw,cl)
        
l = [1,2,3]
w = [0]


rundreisen(w,l)