# run function taken from 15-112 course website events-example0.py

from tkinter import *
from navigationAlgoCode import *

####################################
# customize these functions
####################################

def init(data):
    data.pointList = []
    data.drawing = True
    data.photoSize = 20 #size of each photo
    overlap = 1.05 #overlap factor
    data.distance = data.photoSize/overlap #distance between photo points
    data.photoPoints = []
    # load data.xyz as appropriate
    pass

def mousePressed(event, data):
    if data.drawing: data.pointList.append((event.x, event.y))
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym == "r": data.drawing = False
    elif event.keysym == "space":
        init(data)
        data.photoPoints = []
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    rPoint = 5
    drawPointsInList(canvas, data.pointList, rPoint)
    if data.drawing:
        connectPointsInList(canvas, data.pointList, len(data.pointList)-1)
    else:
        connectPointsInList(canvas, data.pointList, len(data.pointList))
        if data.photoPoints == []:
            data.photoPoints = getAllPoints(data.pointList, data.distance)
        for point in data.photoPoints:
            x, y = point[0], point[1]
            halfLen = data.photoSize/2
            canvas.create_rectangle(x-halfLen, y-halfLen, x+halfLen, y+halfLen, 
            fill = "red")

def drawPointsInList(canvas, pointList, rPoint, color = "white"):
    for index in range(len(pointList)):
        x, y = pointList[index][0], pointList[index][1]
        canvas.create_oval(x-rPoint, y-rPoint, x+rPoint, y+rPoint, fill = color)

def connectPointsInList(canvas, pointList, lenPoints):
    for index in range(lenPoints):
        index2 = (index+1)%len(pointList)
        canvas.create_line(pointList[index], pointList[index2])

        

####################################
# use the run function as-is
####################################

def run(width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run()