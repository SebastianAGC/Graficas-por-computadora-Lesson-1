from Bitmap import *

screen = None
viewPort = {"x": 0, "y": 0, "width": 0, "heigth": 0}
blue = color(0, 0, 255)
red = color(255, 0, 0)
green = color(0, 255, 0)
colorStandard = 255


def glInit():
    pass


def glCreateWindow(width, heigth):
    global screen
    screen = Bitmap(width, heigth)


def glViewPort(x, y, width, heigth):
    global viewPort
    viewPort["x"] = x
    viewPort["y"] = y
    viewPort["width"] = width
    viewPort["heigth"] = heigth


def glClear():
    screen.clear()


def glClearColor(r, g, b):
    screen.color = color(r, g, b)

#Recibe parametros entre -1 y 1
def glVertex(x, y):
    global viewPort
    global screen
    newX = int((x + 1) * (viewPort["width"] / 2) + viewPort["x"])
    newY = int((y + 1) * (viewPort["heigth"] / 2) + viewPort["y"])
    screen.point(newX, newY, screen.currentColor)


def glColor(r, g, b):
    r = int(r * colorStandard)
    g = int(g * colorStandard)
    b = int(b * colorStandard)
    screen.currentColor = color(r, g, b)


def glFinish():
    screen.write('out.bmp')
