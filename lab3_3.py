########################################################
########################################################
#
#Your name: Jude Vargas
#
#Names of people you consulted
#for this assignment(if None, say None): None
#
#I affirm that I have not violated the
#Academic Integrity policies detailed in the syllabus
#
########################################################
########################################################

import turtle # Imports the turtle module to allow the creation of graphics

def main(): # Creates a new function called main
    """
    Function main draws a clock with a turtle at the end of each hour mark

    Parameters: None
    
    Returns: None
    """
    radius = 200 # Sets radius of the clock
    hour_amount = 12 # Sets the amount of tick marks that will be on the clock
    tick_length = 10 # Sets the length of each tick before its respective stamp

    turtle_instance = turtle.Turtle() # Initializes a new turtle object with which to create the graphics
    turtle_instance.shape("turtle") # Changes the shape of the stamp to a turtle
    start_position = turtle_instance.position() # Saves the initial position of the turtle to which to return

    turtle_instance.penup() # Makes sure to not draw anything before the first tick mark
    for i in range(hour_amount): # Iterates over however many tick marks there should be
        turtle_instance.forward(radius) # Moves the turtle forward to the radius of the clock

        turtle_instance.pendown() # Starts drawing the tick mark
        turtle_instance.forward(tick_length) # Moves forward while drawing to create the tick mark
        turtle_instance.penup() # Stops drawing the tick mark

        turtle_instance.forward(tick_length) # Moves forward slightly past the tick mark to make room for the stamp
        turtle_instance.stamp() # Creates a stamp of the turtle past the tick mark

        turtle_instance.goto(start_position) # Returns the turtle to the center of the clock to prepare it for the next tick mark
        turtle_instance.left(360 / hour_amount) # Turns the turtle to the angle of the next tick mark

if __name__ == "__main__": # Checks if code is being directly executed or imported
    main() # Ensures that function main is only called if code is being directly executed
