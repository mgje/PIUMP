#ueb23 Funktionstabelle für den vertikalen Wurf

g = 9.81  # Gravitation
t = 0     # t ist die Variable für die verändernde Zeit
N = 11    # N definiert die Anzahl Berechnungsschritte
v0 = 20   # v0 Anfangsgeschwindigkeit
tot_z = 2*v0/g # tot_z  ist die Zeit die beobachtet werden soll
               # v0/g entspricht der Zeit zum höchsten Punkt
dt = tot_z / N # dt ist der Zeitschritt

while t <= tot_z:
    y = v0*t - 0.5*g*t**2  # y beinhaltet die aktuelle Höhe
    print("h=%.2fm \t \t nach t=%.2fs"%(y,t))
    t = t + dt