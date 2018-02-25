#Add test cases and check code with more convex polygons

import math
import copy
import numpy as np

def getAllPoints(vertexList, distance):
    #main function
    """
    :param vertexList: ordered list of vertices, the fewest needed to describe the region
    :param distance: stride length
    :return: ordered list of points at which to take a photo
    """
    perimeterPoints = getPerimeterPoints(vertexList, distance)
    print(perimeterPoints)
    return getOutputPoints(vertexList, perimeterPoints, distance)

def getPerimeterPoints(vertexList, distance):
    """
        accepts: 
            vertexList: ordered list of vertices of the region
            distance: stride length between points where a photo should be taken
        returns:
            ordered list of points along the perimeter where a picture needs to be taken

    """
    perimeterPoints = []
    for index1 in range(len(vertexList)):
        index2 = (index1 + 1) % len(vertexList)
        vertex1, vertex2 = vertexList[index1], vertexList[index2]
        perimeterPoints += getPointsBtwnVertices(vertex1, vertex2, distance)
    return perimeterPoints

def getPointsBtwnVertices(v1, v2, dx):
    """
        accepts:
            v1: the position of one vertex
            v2: the position of the other vertex
            dx: stride length
        returns:
            points: ordered list of points between v1 and v2 at which to take a photo

    """
    points = []
    v1x, v2x = v1[0], v2[0]
    v1y, v2y = v1[1], v2[1]
    if np.isclose(v1x, v2x):
        return getPointsonVerticalLine(v1x, v1y, v2y, dx)
    if v2x-v1x<0: dx = -dx
    xPoints = int((v2x - v1x) / dx+1)
    print(xPoints)
    dy = (v2y - v1y) / (v2x - v1x) * dx
    x, y = v1x, v1y
    for pointNo in range(xPoints):
        points.append((x, y))
        x += dx
        y += dy
    return points

def getOutputPoints(vertexList, perimeterPoints, distance):
    """
        accepts: 
            vertexList: ordered list of vertices of the region
            perimeterPoints: ordered list of points on the perimeter where a photo is to be taken
            distance: the stride length between photos
        returns:
            ordered list of points at which to take a photo
    """
    #
    outputPoints = []
    for pPoint in perimeterPoints:
        x = pPoint[0]
        y0 = pPoint[1]
        y1 = getLineEnd(x, y0, perimeterPoints)
        #print(pPoint, ": ", (x,y1))
        if y1 == None:
            additionalPoints = [pPoint]
        else:
            additionalPoints = getPointsonVerticalLine(x, y0, y1, distance) + [(x, y1)]
        additionalPointsCopy = copy.deepcopy(additionalPoints)
        for point in additionalPointsCopy:
            if point in outputPoints:
                additionalPoints.remove(point)
        outputPoints += additionalPoints
    return outputPoints

def getLineEnd(x, yStart, perimeterPoints):
    """accepts:
            (x,yStart): position of perimeter point
            perimeterPoints: list of perimeter points, used to check which one is immediately below (x,yStart)
         returns:
            yEnd: when combined into (x,yEnd), it is the coordinates of the point on the perimeter immediately below (x,yStart)
                NOTE: yEnd is None if there is no such point
    """
    pointsBelow = 0
    yEnd = None
    for index1 in range(len(perimeterPoints)):
        index2 = (index1 + 1)%len(perimeterPoints)
        if (x, yStart) == perimeterPoints[index1] \
        or (x, yStart) == perimeterPoints[index2]:
            continue
        x0, x1 = perimeterPoints[index1][0], perimeterPoints[index2][0]
        if min(x0, x1)<= x <= max(x0, x1) and x0 != x1:
            #print(x0, x1)
            y0, y1 = perimeterPoints[index1][1], perimeterPoints[index2][1]
            #if math.isclose(x0, x1):
            #    y = max(y0, y1)
                #print(y,"!")
            #else:
            y = (y1-y0)/(x1-x0) * (x-x0) + y0
            if y > yStart and (yEnd == None or y < yEnd):
                pointsBelow += 1
                yEnd = y
    if pointsBelow % 2 == 0: yEnd = None
    return yEnd

def getPointsonVerticalLine(x, y0, y1, distance):
    """
        accepts: 
            (x,y0) and (x,y1) are the points closest to each other on a vertical line crossing the shape
            distance: the stride length between photos
        returns:
            list of points along a vertical line where a photo should be taken
    """
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

#TEST CASES
print("testing navigationAlgoCode")
#print(getAllPoints([(0, 0), (3, 0), (1.5, 3**0.5 * 1.5)], 1))
print("test seems to be a success!")
#print(getPointsBtwnVertices((50,50),(200,50),19.2))