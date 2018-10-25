#2.12 Simpson Regel 
# Funktion
def f(x):
    return 1/x

# Andere Funktion

h = 1/32 # Schrittweite
s = 1 #Start
e = 2.73 #End
N = int((e-s)/h+1) # Werte also x0 bis xN-1
x = []

# Trage alle Stützstellen in die List x[] ein
for i in range(N):
    x.append(s+i*h)
print(x)     

# 1. Term f(x0)
t1 = f(x[0])
print(t1)
# 2.Term Sum f(xk)
t2 = 0
for i in range(1,N-1):
    y = f(x[i])  #Funktionswert berechnen
    t2 = t2 + y  #Summe bilden
print(t2)
# 3. Term f(xN)
t3 = f(x[-1])
print(t3)
# 4. Term Summe xk-1 + xk /2
t4 = 0
for i in range (1,N):
    mw = (x[i-1]+x[i])/2 #Mittelwert zwische x_i-1 und x_i
    y = f(mw) # Funktionswert berechnen
    t4 = t4 + y #Summe bilden 
print(t4)
# Simpson-Regel
res = h/6 *( t1 + 2 * t2 + t3 + 4 * t4)
print(res)
