# Michael Seeberger
# 16.10.2018

from gpanel import *

class Graph:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    CYAN = (0,255,255)
    TEAL = (0,128,128)
    globalGraph = None
    
    def __init__(self, width = 500, height = 500):
        self._height, self._width = height, width
        makeGPanel(Size(self._width, self._height))
        self._bm = GBitmap(width, height)
        for x in xrange(0, width-1):
            for y in xrange(0, height-1):
                self._bm.setPixelColor(x, y, makeColor(255, 255, 255))
        self.setColor(self.BLACK)
    
    def setColor(self, rgbList):
        self._color = makeColor(rgbList[0], rgbList[1], rgbList[2])
    
    def display(self):
        clear()
        image(self._bm, 0, 0)
    
    def drawAxis(self, xOrigin, yOrigin):
        self.drawLine(0, yOrigin, self._width-1, yOrigin)
        self.drawLine(xOrigin, 0, xOrigin, self._height-1)
        self.drawLine(self._width-7, yOrigin+5, self._width-1, yOrigin)
        self.drawLine(self._width-7, yOrigin-5, self._width-1, yOrigin)
        self.drawLine(xOrigin-5, self._height-7, xOrigin, self._height-1)
        self.drawLine(xOrigin+5, self._height-7, xOrigin, self._height-1)
    
    def sortAscending(self, x0, x1):
        return (x0, x1) if x0 < x1 else (x1, x0)
    
    def plotPixel(self,x, y):
        self._bm.setPixelColor(x, y, self._color)
    
    def _drawLineLow(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        yi = 1
        if dy < 0:
            yi = -1
            dy = -dy
        D = 2*dy - dx
        y = y0

        for x in xrange(x0, x1):
            self.plotPixel(x,y)
            if D > 0:
                y = y + yi
                D = D - 2*dx
            D = D + 2*dy
    def _drawLineHigh(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        xi = 1
        if dx < 0:
            xi = -1
            dx = -dx
        D = 2*dx-dy
        x = x0
        for y in xrange(y0, y1+1):
            self.plotPixel(x, y)
            if D > 0:
                x = x + xi
                D = D - 2*dy
            D = D + 2*dx
    
    def drawLine(self, x0, y0, x1, y1):
        y0 = self._height-y0-1
        y1 = self._height-y1-1
        if abs(y1 - y0) < abs(x1 - x0):
            if x0 > x1:
                self._drawLineLow(x1, y1, x0, y0)
            else:
                self._drawLineLow(x0, y0, x1, y1)
        else:
            if y0 > y1:
                self._drawLineHigh(x1, y1, x0, y0)
            else:
                self._drawLineHigh(x0, y0, x1, y1)
    
    def save(self, path, fileType="jpg"):
        save(self._bm, path, fileType)
    
    @classmethod
    def getSharedGraph(self):
        if self.sharedGraph == None:
            print("creating graph")
            self.initSharedGraph()
        return self.sharedGraph
    
    @classmethod
    def initSharedGraph(self):
        if self.sharedGraph == None:
            raise Exception("No graph created! Call initGraph() first.")
        self.sharedGraph = Graph(width, height)

def initGraph(width = 500, height = 500):
    Graph.sharedGraph = Graph(width, height)
    return Graph.sharedGraph

def drawLine(x0, y0, x1, y1):
    Graph.getSharedGraph().drawLine(x0, y0, x1, y1)

def drawAxis(xOrigin = 50, yOrigin = 50):
    Graph.getSharedGraph().drawAxis(xOrigin, yOrigin)

def plotPixel(x, y):
    sharedGraph = Graph.getSharedGraph()
    sharedGraph.plotPixel(x, sharedGraph._height-y)

def setColor(rgbList):
    Graph.getSharedGraph().setColor(rgbList)

def display():
    Graph.getSharedGraph().display()

def saveGraph(path, fileType="jpg"):
    Graph.getSharedGraph().save(path, fileType)
    