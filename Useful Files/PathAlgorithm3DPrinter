def getSlope(pointA,pointB):
    # print(pointB[0],pointA[0])
    if(pointB[0] == pointA[0]):
        return None
    return (pointB[1] - pointA[1])/(pointB[0] - pointA[0])

def getIntersects(horizontal,line):
    exes = (line[0][0],line[1][0])
    ys = (line[0][1],line[1][1])
    slope = getSlope(line[0],line[1])
    if(slope == 0): return None
    # print("SLOPE:",slope)
    if(slope == None and
           (horizontal < max(ys) and horizontal > min(ys))):
        return (line[0][0],float(horizontal))
    elif(slope == None and
            not (horizontal < max(ys) and horizontal > min(ys))): return None
    offset = line[0][1] - slope*line[0][0]
    # print("OFFSET:",offset)
    xPoint = (horizontal - offset)/slope
    # print("X:",xPoint)
    if(xPoint < max(exes) and xPoint > min(exes) and
       horizontal < max(ys) and horizontal > min(ys)):
        # print("Pass")
        return (xPoint,float(horizontal))
    return None

# initialize the gcode with certain parameters
def initGcode(speed, temp):
    gcode = ""
    gcode += "G1 F%d\n" %speed #In mm/minute
    gcode += "M109 S%d T0\n" %temp #In degrees celsius

# finds distance between two points
def distance(pointA,pointB):
    partA = (pointB[0]-pointA[0])**2
    partB = (pointB[1]-pointA[1])**2
    return (partA + partB)**(1/2)

# test distance function
def distanceTester():
    assert(distance((0,0),(1,1)) == (2)**(1/2))
    assert(distance((1,0),(0,1)) == (2)**(1/2))
    assert(distance((2,0),(0,1)) == (5)**(1/2))

# finds the amount of filament to extrude
def extrudeAmount(pointA, pointB,exPerMm):
    return distance(pointA,pointB) * exPerMm

def createPerimeter(points,exPerMm,buffer):
    gcode = ""
    for index in range(len(points)):
        this = points[index]
        lastIndex = index - 1
        extrude = extrudeAmount(points[lastIndex],this,exPerMm)
        gcode += "G1 X%.2f Y%.2f E%.2f\n" % (points[index][0], points[index][1], extrude)
    gcode+="G1 X%.2f Y%.2f E%.2f\n" % (points[0][0], points[0][1],
                                       extrudeAmount(points[-1], points[0], exPerMm))
    return gcode

def createInfill(points,exPerMm,buffer,bedHeight):
    height = 0
    gcode = ""
    while height < bedHeight:
        gPoints = []
        for index in range(len(points)):
            this = points[index]
            last = points[index - 1]
            polyLine = (this,last)
            intersect = getIntersects(height,polyLine)
            if intersect != None:
                gPoints.append(intersect)
            if len(gPoints) == 2:
                gcode += "G1 X%.2f Y%.2f E%.2f\n" % (gPoints[0][0], gPoints[0][1],0)
                gcode += "G1 X%.2f Y%.2f E%.2f\n" % (gPoints[1][0], gPoints[1][1],
                                                     extrudeAmount(gPoints[0], gPoints[1], exPerMm))
                gPoints = []
        height += buffer
    return gcode

def getGCode(points,exPerMm,verticalBuffer,buffer,bedHeight,profileHeight,verticalStart=0):
    finalGcode = ""
    layerGcode = ""
    layerGcode += createPerimeter(points,exPerMm,buffer)
    layerGcode += createInfill(points,exPerMm,buffer,bedHeight)
    height = 0 + verticalStart
    while height < (profileHeight+verticalStart):
        finalGcode += "G1 Z%.2f\n" %height
        finalGcode += layerGcode
        height += verticalBuffer
    return finalGcode

def getProfilesGCode(profiles,exPerMm,verticalBuffer,buffer,bedHeight):
    gcode = "G1 F3000\n"
    vert = 0
    for i in range(len(profiles)):
        vert += profiles[i-1][0] if i > 0 else 0
        gcode += getGCode(profiles[i][1],exPerMm,verticalBuffer,buffer,bedHeight,profiles[i][0],
                          vert)
    return gcode

#Taken from strings notes
def writeFile(path,contents):
    with open(path, "wt") as f:
        f.write(contents)
