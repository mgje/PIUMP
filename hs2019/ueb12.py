# ueb1.2
from math import *
inch = 0.0254 # in Meter
fuss = 12 * inch 
yard = 3 * fuss
meile = 1760 * yard
eingabe = 4640 #m
ininch = eingabe / inch
infuss = eingabe / fuss
inyard = eingabe / yard
inmeilen = eingabe / meile
meilengerundet = floor(inmeilen)
rest1 = eingabe - meilengerundet*meile
yardgerundet = floor(rest1/yard)
rest2 = rest1 - yardgerundet*yard
fussgerundet = floor(rest2/fuss)
rest3 = rest2 - fussgerundet*fuss
inchgerundet = floor(rest3/inch)

print("%g m sind %g Meilen %g Yard %g Fuss %.2f Inch"%(eingabe,meilengerundet,yardgerundet,fussgerundet,inchgerundet))