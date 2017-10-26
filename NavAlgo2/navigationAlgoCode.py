#Buggy code below
import math
def getAllPoints(vertexList, distance):
    #main function: takes in initial input and returns final output
    perimeterPoints = getPerimeterPoints(vertexList, distance)
    return getOutputPoints(vertexList, perimeterPoints, distance)

def getPerimeterPoints(vertexList, distance):
#takes in ordered list of vertices, and horizontal distance between every two
#points where a photo should be taken
    perimeterPoints = []
    for index1 in range(len(vertexList)):
        index2 = (index1 + 1) % len(vertexList)
        vertex1, vertex2 = vertexList[index1], vertexList[index2]
        perimeterPoints += getPointsBtwVertices(vertex1, vertex2, distance)
    return perimeterPoints

def getPointsBtwVertices(v1, v2, dx):
    #gets points to take photo at between every pair of vertices, along the
    #perimeter
    points = []
    v1x, v2x = v1[0], v2[0]
    v1y, v2y = v1[1], v2[1]
    if math.isclose(v1x, v2x):
        return getPointsonVerticalLine(v1x, v1y, v2y, dx)
    if v2x-v1x<0: dx = -dx
    xPoints = (v2x - v1x) // dx
    dy = (v2y - v1y) / (v2x - v1x) * dx
    x, y = v1x, v1y
    for pointNo in range(xPoints):
        points.append((x, y))
        x += dx
        y += dy
    return points

def getOutputPoints(vertexList, perimeterPoints, distance):
    #returns final list of points at which to take a photo
    outputPoints = []
    for pPoint in perimeterPoints:
        x = pPoint[0]
        y0 = pPoint[1]
        y1 = getLineEnd(x, y0, perimeterPoints)
        if y1 == None: continue
        y0, y1 = min(y0, y1), max(y0, y1)
        outputPoints += getPointsonVerticalLine(x, y0, y1, distance)
    return outputPoints

def getLineEnd(x, yStart, perimeterPoints):
    #gets the end of a vertical line of photos given the xcoordinate and the
    #starting point; if no such line, returns None
    pointBelowExists = False
    yEnd = None
    for index1 in range(len(perimeterPoints)):
        index2 = (index1 + 1)%len(perimeterPoints)
        if (x, yStart) == perimeterPoints[index1] \
        or (x, yStart) == perimeterPoints[index2]:
            continue
        x0, x1 = perimeterPoints[index1][0], perimeterPoints[index2][0]
        if min(x0, x1)<= x <= max(x0, x1):
            y0, y1 = perimeterPoints[index1][1], perimeterPoints[index2][1]
            if math.isclose(x0, x1):
                y = min(y0, y1)
            else:
                y = (y1-y0)/(x1-x0) * (x-x0) + y0
            if y > yStart and (yEnd == None or y < yEnd):
                pointBelowExists, yEnd = True, y
    return yEnd

def getPointsonVerticalLine(x, y0, y1, distance):
    #gets points along a vertical line where a photo should be taken
    upToDown = True
    if y1<y0:
        distance = -distance
        upToDown = False
    points = []
    y = y0
    while (y<y1 and upToDown) or (y>y1 and not upToDown):
        points.append((x, y))
        y += distance
    return points

#print(getAllPoints([(0, 0), (2, 0), (2, 2), (0, 2)], 1))