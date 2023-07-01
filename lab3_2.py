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
    Function main prompts the user to design a polygon and then displays the resulting polygon to the screen

    Parameters: None
    
    Returns: None
    """
    side_amount = int(input("Please enter the number of sides: ")) # Prompts the user to enter the number of sides and stores the value as an int
    side_length = int(input("Please enter the length of each side: ")) # Prompts the user to enter the length of each side and stores the value as an int
    edge_color = input("Please enter the color for the edges: ") # Prompts the user to enter the color for the edges and stores the value as a string
    fill_color = input("Please enter the color for the body of the shape: ") # Prompts the user to enter the color for the main body and stores the value as a string

    angle_degrees = 360 / side_amount # Calculates the amount of degrees by which to turn based on the amount of sides entered

    turtle_instance = turtle.Turtle() # Initializes a new turtle object with which to create the graphics
    turtle_instance.color(edge_color) # Sets the polygon's edge color to the entered value
    turtle_instance.fillcolor(fill_color) # Sets the polygon's body color to the entered value
    
    turtle_instance.begin_fill() # Tells the turtle instance to begin drawing before sending the actual instructions

    for i in range(side_amount): # Iterates over however many sides the user entered
        turtle_instance.forward(side_length) # Draws a straight line forward with the user's entered length
        turtle_instance.left(angle_degrees) # Turns left by the calculated amount of degrees after drawing each line
        
    turtle_instance.end_fill() # Tells the turtle instance to stop drawing once the polygon is finished

if __name__ == "__main__": # Checks if code is being directly executed or imported
    main() # Ensures that function main is only called if code is being directly executed