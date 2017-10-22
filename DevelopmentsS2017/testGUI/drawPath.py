
#an interface that allows the visualizer to draw the paths of the algorithm
class DrawPath_t:

    def __init__(self,pointArr,imageWidth,imageHeight):
        self.pointArr = pointArr
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.coordinates = []

    #Get,Set for points of the polygon
    def getPoints(self): #Gets the points given by the shape
        return self.pointArr

    def setPoints(self,newPoints): #Sets the points in the shape
        self.pointArr = newPoints

    #Get,Set for image dims
    def getHeight(self):
        return self.imageHeight

    def getWidth(self):
        return self.imageWidth

    def setHeight(self,height):
        self.imageHeight = height

    def setWidth(self,width):
        self.imageWidth = width

    #calculates the coordinates at which a picture will be taken
    def calculateCoordinates(self):
        raise Exception("calculateCoordinates not implemented")

    def getCoordinates(self): #Return the coordinates
        return self.coordinates

    def setCoordinates(self,newCoordinates): #set all the coordinates
        self.coordinates = newCoordinates

    def appendCoordinates(self,coordinate): #append a coordinates
        self.coordinate.append(coordinate)
