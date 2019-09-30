#ueb12
from math import *
l = 3641
inch = 0.0254
fuss = 12*inch
yard = 3*fuss
mile = 1760 * yard
inmiles = l/mile
gm = floor(inmiles)
rest1 = l - gm*mile
inyard = rest1/yard
gy =floor(inyard)
rest2 = rest1-gy*yard
infeet = rest2/fuss
gf = floor(infeet)
rest3 = rest2-gf*fuss

print("Eine Meile sind %g m, %g m sind %g Meilen"%(mile,l,inmiles))
print("%g m sind %g Meilen %g Yard %g Fuss %g Rest in m" %(l,gm,gy,gf,rest3))