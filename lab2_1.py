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

import math # Imports the Python math module to allow use of math.pi

def main(): # Creates a new function called main
    """
    Function main prompts the user for a radius and prints the area of its circle

    Parameters: None
    
    Returns: None

    """
    radius = float(input("Please enter the radius for the circle: ")) # Prompts the user to type in a radius and stores the value as a float
    area = math.pi * radius ** 2 # Computes the area of the circle using the inputted radius
    print(f"The area of your cicle is {area} units") # Prints a message containing the area of the circle

if __name__ == "__main__": # Checks to see if file is being exected or imported
    main() # Ensures that code is only ran if file is being directly executed