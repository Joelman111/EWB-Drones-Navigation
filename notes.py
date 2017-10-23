#1) Make all lines - list (list of tuples (v,w))
#2) Make line of split between vertices with lowest y and highest y
#3) Split list into L & R (one of both of vertices of line will be L or R
#                          of x-value of line vertices)
#4) Horizontal line test - adjust L and R
#5)Traverse left to right, right to left, ...
#6)Travel through the centers of the squares in the same order as #5

class Line(object):
    def __init__(self, x1, y1, x2, y2):
        self.pt1 = (x1,y1)
        self.pt2 = (x2,y2)
        self.slope = (y1-y2)

#List of points in form of [(x1,y1),(x2,y2),...]
def makeAllLines(listOfPoints):
    length = len(listOfPoints)
    result = []
    for i in range(length):
        temp1 = listOfPoints[i]
        for j in range(i + 1, length):
            temp2 = listOfPoints[j]
            result.append([temp1,temp2])
    return result


"""
Make a line between the highest point and the lowest point on the shape.
Break down the shape to left and right from there (left side of shape vs
right side f shape).
Add boxes to each side until they are out of bounds
Manipulate the array of all the boxes to get the final array of points
