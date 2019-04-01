from sr1 import *
import random


def getPossibleValues(pixels):
    array = []
    step = 2 / pixels
    start = -1
    while start < 1:
        array.append(start)
        start = start + step
    return array


def blackImageRandomPoint():
    glInit()
    glCreateWindow(100, 100)
    glViewPort(0, 0, 100, 100)
    glClearColor(1, 1, 1)
    glClear()
    glColor(1, 1, 1)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    glVertex(x, y)
    glFinish()


def cornerPoints():
    glInit()
    glCreateWindow(100, 100)
    glViewPort(0, 0, 100, 100)
    glClearColor(1, 1, 1)
    glClear()
    glColor(1, 1, 1)
    glVertex(-1, -1)
    glVertex(-1, 1)
    glVertex(1, -1)
    glVertex(1, 1)
    glFinish()


def cubeRender():
    glInit()
    glCreateWindow(200, 200)
    glViewPort(0, 0, 200, 200)
    glClearColor(1, 1, 1)
    glClear()
    glColor(1, 1, 1)

    arrayX = getPossibleValues(200)

    for x in range(50, 151):
        glVertex(arrayX[x], 0.5)

    for x in range(50, 151):
        glVertex(arrayX[x], -0.5)

    for x in range(50, 150):
        glVertex(0.5, arrayX[x])

    for x in range(50, 150):
        glVertex(-0.5, arrayX[x])

    glFinish()


def whiteMargin():
    width = 100
    height = 100
    glInit()
    glCreateWindow(width, height)
    glViewPort(0, 0, width, height)
    glClearColor(1, 1, 1)
    glClear()
    glColor(1, 1, 1)
    step = 2 / width
    start = -1
    while start < 1:
        glVertex(start, 1)
        start = start + step
    start = -1
    while start < 1:
        glVertex(start, -1)
        start = start + step
    step = 2 / height
    start = -1
    while start < 1:
        glVertex(1, start)
        start = start + step
    start = -1
    while start < 1:
        glVertex(-1, start)
        start = start + step
    glFinish()


def diagonal():
    glInit()
    glCreateWindow(100, 100)
    glViewPort(0, 0, 100, 100)
    glClearColor(1, 1, 1)
    glClear()
    glColor(1, 1, 1)
    start = -1
    step = 2 / 100
    while start < 1:
        glVertex(start, start)
        start = start + step
    glFinish()


def blackAndWhitePoints():
    width = 100
    height = 100
    glInit()
    glCreateWindow(width, height)
    glViewPort(0, 0, width, height)
    glClearColor(0, 0, 0)
    glClear()
    glColor(1, 1, 1)

    arrayX = getPossibleValues(width)
    arrayY = getPossibleValues(height)

    for x in range(width):
        for y in range(height):
            n = random.uniform(-1, 1)
            if (n > 0):
                glVertex(arrayX[x], arrayY[y])
    glFinish()


def colorRandomPoints():
    width = 100
    height = 100
    glInit()
    glCreateWindow(width, height)
    glViewPort(0, 0, width, height)
    glClearColor(0, 0, 0)
    glClear()
    arrayX = getPossibleValues(width)
    arrayY = getPossibleValues(height)

    for x in range(width):
        for y in range(height):
            r = random.uniform(0, 1)
            g = random.uniform(0, 1)
            b = random.uniform(0, 1)
            glColor(b, g, r)
            glVertex(arrayX[x], arrayY[y])
    glFinish()


def starryNight():
    width = 800
    height = 800
    glInit()
    glCreateWindow(width, height)
    glViewPort(0, 0, width, height)
    glClearColor(0, 0, 0)
    glClear()
    glColor(1, 1, 1)

    arrayX = getPossibleValues(width)
    arrayY = getPossibleValues(height)

    for x in range(width):
        for y in range(height):
            n = random.uniform(-1, 1)
            if (n > 0.997):
                glVertex(arrayX[x], arrayY[y])
    glFinish()


def atariGameScene():
    width = 192
    height = 160
    glInit()
    glCreateWindow(width, height)
    glViewPort(0, 0, width, height)
    glClearColor(1, 1, 1)
    glClear()
    glColor(1, 1, 1)

    arrayX = getPossibleValues(width)
    arrayY = getPossibleValues(height)

    y = 0
    step = 2

    #middle line
    while y < height:
        glVertex(arrayX[int(width/2)], arrayY[y])
        glVertex(arrayX[int(width/2)], arrayY[y + 1])
        glVertex(arrayX[int(width/2)], arrayY[y + 2])
        y = y + 7

    #drawing scoreboard
    for x in range(40,60):
        glVertex(arrayX[x], arrayY[150])
        glVertex(arrayX[x], arrayY[151])
        glVertex(arrayX[x], arrayY[152])
        glVertex(arrayX[x], arrayY[130])
        glVertex(arrayX[x], arrayY[131])
        glVertex(arrayX[x], arrayY[132])

    for y in range(130, 150):
        glVertex(arrayX[40], arrayY[y])
        glVertex(arrayX[41], arrayY[y])
        glVertex(arrayX[42], arrayY[y])
        glVertex(arrayX[57], arrayY[y])
        glVertex(arrayX[58], arrayY[y])
        glVertex(arrayX[59], arrayY[y])

    for x in range(135,155):
        glVertex(arrayX[x], arrayY[150])
        glVertex(arrayX[x], arrayY[151])
        glVertex(arrayX[x], arrayY[152])
        glVertex(arrayX[x], arrayY[130])
        glVertex(arrayX[x], arrayY[131])
        glVertex(arrayX[x], arrayY[132])

    for y in range(130, 150):
        glVertex(arrayX[135], arrayY[y])
        glVertex(arrayX[136], arrayY[y])
        glVertex(arrayX[137], arrayY[y])
        glVertex(arrayX[152], arrayY[y])
        glVertex(arrayX[153], arrayY[y])
        glVertex(arrayX[154], arrayY[y])

    #drawing pong sticks

    for y in range(50, 70):
        glVertex(arrayX[20], arrayY[y])
        glVertex(arrayX[21], arrayY[y])
        glVertex(arrayX[22], arrayY[y])

    for y in range(80, 100):
        glVertex(arrayX[172], arrayY[y])
        glVertex(arrayX[173], arrayY[y])
        glVertex(arrayX[174], arrayY[y])

    #drawing ball
    for y in range(67, 70):
        glVertex(arrayX[60], arrayY[y])
        glVertex(arrayX[61], arrayY[y])
        glVertex(arrayX[62], arrayY[y])



    glFinish()


# ------------Main program starts here------------#
print('Tarea 1 - Sebastián Galindo 15452')
print("El resultado lo puede ver en el archivo output.bmp")

while True:
    print("1. Punto blanco en posicion random")
    print("2. Puntos blancos en esquinas")
    print("3. Cubo de 100px X 100px")
    print("4. Margen Blanco")
    print("5. Diagonal")
    print("6. Puntos blancos y negros")
    print("7. Puntos de colores random")
    print("8. Noche estrellada")
    print("9. Escena juego de Atari")

    op = int(input("Ingrese el número de item que desea ver: "))
    if op == 1:
        # item 1
        blackImageRandomPoint()

    if op == 2:
        # item 2
        cornerPoints()

    if op == 3:
        # item 3
        cubeRender()

    if op == 4:
        # item 4
        whiteMargin()

    if op == 5:
        # item 5
        diagonal()

    if op == 6:
        # item 6
        blackAndWhitePoints()

    if op == 7:
        # item 7
        colorRandomPoints()

    if op == 8:
        # item 7
        starryNight()

    if op == 9:
        # item 7
        atariGameScene()
