# Übung K3.03
#   x1 y1 x2 y2 x3 y3
# [[0,0],[1,0],[2,0]
def berechne_dreieck(inp):
    x1 = inp[0][0]
    y1 = inp[0][1]
    x2 = inp[1][0]
    y2 = inp[1][1]
    x3 = inp[2][0]
    y3 = inp[2][1]
    
    return  1/2 * abs(x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1)

koord = [[2,3],[1,0],[4,2]]
print (berechne_dreieck(koord))



def berechne_dreieck2(x1,y1,x2,y2,x3,y3): 
    A = 1/2 * abs(x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1)
    return A

print (berechne_dreieck2(2,3,1,0,4,2))






