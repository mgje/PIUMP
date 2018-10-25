#Uebung 2.12 Simpson Regel

s = 0 # Start
e = 2 # End

h = 1/4
n = (e-s)/h
N = int(n)

# function y = x**3 + 1

# f(x0)
r1 = 0**3+1

# sum f(xk)
r2 = 0
for i in range(1,N):
    xk = i*h
    y = xk**3+1
    r2 = r2 + y

#f(xn)
r3 = e**3+1

# sum f((xk-1 + xk)/2)
r4= 0
for i in range(1,N+1):
    xk = i*h
    xk_ = (i-1)*h
    xm = (xk+xk_)/2
    y = xm**3+1
    r4 = r4 + y
# Smpson    

res = h/6 * (r1 + 2 * r2 + r3 + 4 * r4)
print(res)
# 6
# https://www.wolframalpha.com/input/?i=int_0%5E2+(x%5E3%2B1)+dx


