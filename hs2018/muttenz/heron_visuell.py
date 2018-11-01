# Michael Seeberger
# 16.10.2018

from graph import *
import time

# Verfügbare Funktionen:
#   initGraph(width, height)
#       Erzeugt den Graphen mit der Breite width und Höhe height
#   setColor(rgbList)
#       Setzt die Farbe. Übergabeparameter ist eine Liste mit RGB-Werten (0-255).
#       Vordefinierte Werte sind: Graph.BLUE, Graph.RED, Graph.Green, Graph.BLACK, Graph.CYAN
#       Beispiel:
#            setColor(Graph.BLACK)
#            setColor(100, 100, 100) # (grau)
#   drawAxis(xOrigin, yOrigin)
#       Zeichnet die Achsen. Die Achsen kreuzen sich bei (xOrigin, yOrigin). xOrigin und yOrigin müssen Integer sein!
#   drawLine(x0, y0, x1, y1)
#       Zeichnet eine Linie von (x0, y0) zu (x1, y1). Alle Koordinaten müssen Integer-Werte sein!
#   display()
#       Gibt den Graphen auf dem Bildschirm aus. Diese Funktion kann mehrmals aufgerufen werden.
#   saveGraph(path, format)
#       Den Graphen als Bild speichern. Beispiel: saveGraph("/my/path/file.jpg", "jpg")
plotWidth, plotHeight = 1400, 1000
initGraph(plotWidth, plotHeight)

axisOffset = 20
drawAxis(axisOffset, axisOffset)
display()

number = 18
a = 1

scale = (plotWidth-(axisOffset+10))/(0.5*(1+number))

colors = [Graph.RED, Graph.GREEN, Graph.BLUE, Graph.CYAN]
steps = 5
for i in xrange(1, steps+1):
    setColor(colors[i % len(colors)])
    a = 0.5*(a + number/a)
    print(a)
    
    # Pixels must be integers
    height = int(round(scale*number/a))
    width = int(round(scale*a))
    
    drawLine(axisOffset+width, axisOffset, axisOffset+width, axisOffset+height)
    drawLine(axisOffset+width, axisOffset+height, axisOffset, axisOffset+height)
    
    display()
    time.sleep(1)

setColor(Graph.BLACK)
display()
#saveGraph("/Users/michaelseeberger/Desktop/out.jpg")