#Uebeung 2.6

a = [1,3,5,7,11]
b = [13,17]
c = a+b
print(c)
b[0] = -1
d = [e+1 for e in a]
print(d)
d.append(b[0]+1)
d.append(b[-1]+1)
print(d[-2:])