#ueb_K1_02.py
# Umwandlung in britische Einheiten
# (c) Martin Guggisberg 2018


eingabe = 650   # in [m]
#eingabe = 0.0254*45   # in [m]

inch = 0.0254    # in [m]
fuss = inch*12   # in [m]
yard = fuss*3    # in [m]
meile = yard*1760 # in [m]

miles = eingabe/meile
restyards = (miles - int(miles))*1760
restfuss = (restyards - int(restyards))*3
restinch = (restfuss - int(restfuss))*12

print "%g Meter entspricht %g Miles %g Yards %g Feet %.2f Inches" % (eingabe,int(miles),int(restyards),int(restfuss),restinch)
