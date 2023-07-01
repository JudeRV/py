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
    Function main prompts the user to enter a temperature in Fahrenheit and prints the resulting conversion to Celsius

    Parameters: None
    
    Returns: None
    """
    degrees_fahrenheit = float(input("Please enter the temperature in Fahrenheit: ")) # Prompts the user to enter a temperature in F and stores it as a float
    
    degrees_celsius = (degrees_fahrenheit - 32) * 5 / 9 # Calculates the temperature in Celsius given the entered value
    print(f"{degrees_fahrenheit}\u00B0F converted to Celsius is {degrees_celsius}\u00B0C") # Prints a message containing the value in Celsius
    
if __name__ == "__main__": # Checks if code is being directly executed or imported
    main() # Ensures that function main is only called if code is being directly executed