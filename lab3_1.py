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
    Function main initalizes a list of ints, prints them out, then prints them again with their respective squared values

    Parameters: None
    
    Returns: None
    """
    a_list = [12,10,32,3,66,17,42,99,20] # Initializes list of values from exercise
    
    for i in a_list: # Iterates directly over items in a_list
        print(i) # Prints each item to the shell on different lines

    print('-' * 5) # Prints a spacer of 5 hyphens for output readability

    for i in a_list: # Iterates directly over items in a_list again
        print(f"{i}\u00B2 = {i ** 2}") # Prints out a message containing each item's squared value
        
if __name__ == "__main__": # Checks if code is being directly executed or imported
    main() # Ensures that function main is only called if code is being directly executed