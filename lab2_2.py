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

def main(): # Creates a new function called main
    """
    Function main prompts the user for amounts of miles driven and gallons used and prints the calculated miles per gallon

    Parameters: None
    
    Returns: None

    """
    miles_driven = float(input("Please enter the number of miles driven: ")) # Prompts the user to type the number of miles driven and stores it as a float
    gallons_used = float(input("Please enter the number of gallons used: ")) # Prompts the user to type the number of gallons and stores it as a float

    miles_per_gallon = miles_driven / gallons_used # Calculates the miles per gallon using the two inputted values
    print(f"Your miles per gallon is {miles_per_gallon}") # Prints a message containing the user's miles per gallon

if __name__ == "__main__": # Checks to see if file is being exected or imported
    main() # Ensures that code is only ran if file is being directly executed