from gpanel import *

size = 300

makeGPanel(Size(2 * size, size))
window(0, 2 * size, size, 0)    # y axis downwards
img = getImage("sprites/colorfrog.png")
w = img.getWidth()
h = img.getHeight()
image(img, 0, size)



