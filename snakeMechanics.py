from turtle import Turtle

STARTING_POSITIONS= [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    
    #Create a constructor to initialize a list of all segments
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]
    
    #Create  a snake segment and append it to the list of all_segments
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    #Function to add a new segment each time snake consumes food
    def add_segment(self, position):
        segments = Turtle("square")
        segments.color("white")
        segments.penup()
        segments.goto(position)
        self.all_segments.append(segments)
        
    #Function to extend the snake with the new segments
    def extend(self):
        self.add_segment(self.all_segments[-1].position())
        
    #Function to move each segment by overlapping each part with the next segmnets coordinates
    def move(self):
        for i in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[i - 1].xcor()
            new_y = self.all_segments[i - 1].ycor()
            self.all_segments[i].goto(new_x, new_y)
            
        self.head.forward(MOVE_DISTANCE)
    
    #Creating the directional movements
    def up(self):
        #To prevent the head moving back on itself
        if int(self.head.heading()) == 270: 
            pass
        else:
            self.head.setheading(90)
        
    def down(self):
        if int(self.head.heading()) == 90:
            pass
        else:
            self.head.setheading(270)
        
    def left(self):
        if int(self.head.heading()) == 0:
            pass
        else:
            self.head.setheading(180)
        
    def right(self):
        if int(self.head.heading()) == 180:
            pass
        else:
            self.head.setheading(0)
            
    def reset_snake(self):
        for seg in self.all_segments:
            seg.goto(1000, 1000)
            
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]
