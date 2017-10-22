#1) Make all lines - list (list of tuples (v,w))
#2) Make line of split between vertices with lowest y and highest y
#3) Split list into L & R (one of both of vertices of line will be L or R
#                          of x-value of line vertices)
#4) Horizontal line test - adjust L and R
#5)Traverse left to right, right to left, ...
#6)Travel through the centers of the squares in the same order as #5


"""
Make a line between the highest point and the lowest point on the shape.
Break down the shape to left and right from there (left side of shape vs
right side f shape).
Add boxes to each side until they are out of bounds
Manipulate the array of all the boxes to get the final array of points
