from math import pi
#ueb46 mit Liste
j = 16 

Z = [x**2 for x in range(1,j+1)]
#print(Z)
N = [2*i+1 for i in range(j)]
#print(N)

s = Z.pop()
while (len(Z)>0):
    s = s + N.pop()
    s = Z.pop() / s

s = s + N.pop()

p = 4.0 / s

print(p)
print(pi)
    
    