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

import math
import turtle

def area_of_circle(radius):
    """
    Function area_of_circle calculates the area of a circle, given its radius

    Parameters:
        radius: The radius of the circle
    
    Returns: The calculated area of the circle
    """
    
    return math.pi * radius ** 2

def draw_square(t, center_x, center_y, side_length):
    """
    Function draw_square draws a square of the desired size and location

    Parameters:
        t: an instance of turtle through which to access the drawing methods
        center_x: the x-coordinate of the center of the square
        center_y: the y-coordinate of the center of the square
        side_length: the length of each side of the square

    Returns: None
    """
    
    t.penup()

    # Moves the pen to one corner of square calculated from its center & side length
    t.goto((center_x, center_y))
    t.left(90)
    t.forward(side_length / 2)
    t.right(90)
    t.back(side_length / 2)

    # Draws the actual square
    t.pendown()
    for i in range(4):
        t.forward(side_length)
        t.right(90)
    t.penup()

def draw_nested_squares(t, center_x, center_y, side_length, number_of_squares):
    """
    Function draw_nested_squares draws a series of concentric squares

    Parameters:
        t: an instance of turtle through which to access the drawing methods
        center_x: the x-coordinate of the center of the squares
        center_y: the y-coordinate of the center of the squares
        side_length: the length of each side of the innermost square
        number_of_squares: the amount of squares to draw, going outwards from the center
    
    Returns: None
    """
    
    # Draws each square, increasing the side length by 20 after each square is drawn
    for i in range(number_of_squares):
        draw_square(t, center_x, center_y, side_length)
        side_length += 20

def draw_twisted_squares(t, center_x, center_y, side_length, number_of_squares):
    """
    Function draw_twisted_squares draws a series of twisting square around a single point

    Parameters:
        t: an instance of turtle through which to access the drawing methods
        center_x: the x-coordinate of the center of the squares
        center_y: the y-coordinate of the center of the squares
        side_length: the length of each side of the squares
        number_of_squares: the amount of squares to draw, with equal angles between each square
    
    Returns: None
    """
    
    angle = 90 / number_of_squares

    # Draws each square with its respective angle offset
    for i in range(number_of_squares):
        draw_square(t, center_x, center_y, side_length)
        t.goto((center_x, center_y))
        t.right(angle)

def square_root(number, num_guesses):
    """
    Function square_root returns the approximate square root of a number as according to Newton's method

    Parameters: 
        number: the number of which to find the square root
        num_guesses: the amount of iterations to go through to better approximate the result
    
    Returns: The approximate square root of the given number
    """
    
    # Perform the first iteration separately
    guess = number / 2

    # Iteratively updates value of guess according to Newton's method until value of num_guesses is reached
    for i in range(num_guesses - 1):
        guess = 1 / 2 * (guess + (number / guess))
    return guess

def main():
    """
    Function main calls other functions in this file for testing and display

    Parameters: None

    Returns: None
    """

    t = turtle.Turtle()

    # Executes each function and displays their respective results
    print(f"1. area_of_circle(5) = {area_of_circle(5)}\n")
    
    print("2. draw_square(t, 0, 0, 30) will be displayed in Turtle's window")
    draw_square(t, 0, 0, 30)

    print("3. draw_nested_squares(t, 250, 250, 20, 5) will be displayed in Turtle's window")
    draw_nested_squares(t, 250, 250, 20, 5)

    print("4. draw_twisted_squares(t, -250, -250, 100, 4) will be displayed in Turtle's window\n")
    draw_twisted_squares(t, -250, -250, 100, 4)

    print(f"5. square_root(3, 5) = {square_root(3, 5)} --- math.sqrt(3) = {math.sqrt(3)}")

# Ensures that code is only ran if it's being directly executed
if __name__ == "__main__":
    main()
