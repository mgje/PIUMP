# Wachstum von Geld auf einer Schweizer Bank
# (c) Martin Guggisberg 2018

p=1.5  # %
A=1000.0 # Franken
n = 160 # Jahre

guthaben = A*(1.0 + p/100.0)**n

print ("Ihr Anfangsguthaben von %g wächst nach %d Jahre\
 auf den Wert von %g Fr" % (A,n,guthaben))