from gpanel import *


def getIterationColor(it):
    color = makeColor((30 * it) % 256, 
                      (4 * it) % 256, 
                      (255 - (30 * it)) % 256)
    return color

def mandel(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    i = 0
    c = complex(x,y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i

    return 255


maxIterations = 150
R = 2
N = 100
xmin = -2
xmax = 0.6
ymin = -0.8
ymax = 0.8


#xmin = -1.5
#xmax = -1.3

#ymin = -0.05
#ymax = 0.05

#xmin = -1.41
#xmax = -1.408

##ymin = -0.0005
#ymax = 0.0005


ystep = (ymax-ymin)/N
xstep = (xmax-xmin)/N



makeGPanel(xmin, xmax, ymin, ymax)
#line(xmin, 0, xmax, 0)  # real axis
#line(0, ymin, 0, ymax) # imaginary axis
title("Mandelbrot set")
y = ymin
while y <= ymax:
    x = xmin
    while x <= xmax:
        v = mandel(x, y, maxIterations)
        
        if v<255:
            move(x,y)
            setColor(getIterationColor(v))
            fillRectangle(xstep,ystep)
        x += xstep
    y += ystep
