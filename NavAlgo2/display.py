import tkMessageBox

import numpy as np
import Tkinter as tk
import navigationAlgoCode as nav

class App:
    def __init__(self,master):
        self.master = master

        master.title("Drone Algorithm Displayer")
        frame=tk.Frame(master)
        frame.pack()

        frame1=tk.Frame(frame)
        frame1.pack(side=tk.TOP)
        frame2=tk.Frame(frame)
        frame2.pack(side=tk.TOP)

        self.drawPathButton = tk.Button(frame1, text="Draw Path", command=self.drawPath)
        self.drawPathButton.pack(side=tk.LEFT)
        self.resetButton=tk.Button(frame1,text="Reset",command=self.reset)
        self.resetButton.pack(side=tk.LEFT)
        self.infoButton = tk.Button(frame1,text="Help",command=self.showInfo)
        self.infoButton.pack(side=tk.LEFT)

        self.pxlen=20
        self.cs=self.pxlen*28
        self.canvas=tk.Canvas(frame2,width=self.cs,height=self.cs)
        self.canvas.pack(anchor=tk.CENTER)

        self.master.bind('<Button-1>', self.click)

        self.vertices = []#ordered list of vertices describing the region

        self.reset()

    def showInfo(self):
        tkMessageBox.showinfo('EWB Drone Nav Algo GUI',"""
            Welcome to the EWB Drone Navigation Algorithm GUI!
            
            First, click to set the boundary vertices of your region,
            without clicking on the first vertex again at the end. Then, 
            click 'Draw Path', which will prompt you to enter the stride 
            length in pixels. Enter the desired length (be reasonable!) 
            and hit OK.
            
            The algorithm should display the planned path through the 
            region. Hit 'Reset' to reset the screen.
        """)

    def drawPath(self):
        #TODO this is the part where it doesn't seem to work
        stride = 3
        points = nav.getAllPoints(self.vertices, stride)
        idx=0
        while(idx<len(points)):
            start=points[idx]
            end=points[(idx+1)%len(points)]
            self.canvas.create_line(start[0],start[1],end[0],end[1])
            idx+=1

    def drawArrow(self,start,end):
        """
        This function assumes that start and end are valid,
            ie within the canvas
        :param start: ordered pair representing start point
        :param end: ordered pair representing end point
        :return: void
        """
        (sx,sy)=start
        (ex,ey)=end
        #TODO make this an actual arrow
        self.canvas.create_line(sx,sy,ex,ey)
        """
        size = 3
        length = ((ey-sy)**2+(ex-sx)**2)**(.5)
        slope = (ey-sy)/(ex-sx)
        unit =
        (ax,ay)=(sx)
        """

    def reset(self):
        self.canvas.delete(tk.ALL)
        self.drawBox()
        self.vertices=[]

    def drawpoint(self,x,y):
        if(y<25): return
        radius = 4
        self.canvas.create_oval(x-radius,y+radius,x+radius,y-radius)
        self.vertices.append((x,y))
        if(len(self.vertices)>1):
            start = self.vertices[-2]
            end = self.vertices[-1]
            self.drawArrow(start,end)

    def click(self, event):
        x,y=event.x, event.y
        self.drawpoint(x,y)
        print('{}, {}'.format(x, y))

    #draws the box around the checkered canvas
    def drawBox(self):
        self.canvas.create_line(0,0,self.cs,0)
        self.canvas.create_line(0, 0, 0, self.cs)
        self.canvas.create_line(self.cs, 0, self.cs, self.cs)
        self.canvas.create_line(0, self.cs, self.cs, self.cs)

if __name__=='__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
