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

def for_power(a, b):
    """
    Function for_power returns the number a raised to the power of b using a for loop

    Parameters:
        a: the base number of which to take the power
        b: the exponent to be applied to a
    
    Returns: The number a raised to the power of b
    """

    # Start with 1 in case b = 0
    result = 1

    # Raise result to each power until it reaches the power of b
    for i in range(b):
        result *= a

    return result

def while_power(a, b):
    """
    Function for_power returns the number a raised to the power of b using a while loop

    Parameters:
        a: the base number of which to take the power
        b: the exponent to be applied to a
    
    Returns: The number a raised to the power of b
    """

    # Save the initial value to reapply it each iteration
    result = 1

    # Raise a to each power until it reaches the power of b
    while (b > 0):
        result *= a
        b -= 1

    return result

def for_sum_to(n):
    """
    Function for_sum_to returns the sum of the first n reciprocals using a for loop

    Parameters:
        n: the number of reciprocals to add
    
    Returns: The sum of the first n reciprocals
    """

    # Create base number to which to iteratively add
    result = 0.0

    # Shift the range to make use of i easier in the calculation
    for i in range(1, n + 1):
        result += 1 / i

    return result

def while_sum_to(n):
    """
    Function while_sum_to returns the sum of the first n reciprocals using a while loop

    Parameters:
        n: the number of reciprocals to add
    
    Returns: The sum of the first n reciprocals
    """

    # Create base number to which to iteratively add
    result = 0.0

    # Iteratively add reciprocals to result
    while (n > 0):
        result += 1 / n
        n -= 1

    return result

def for_repeat(string, num):
    """
    Function for_repeat returns the given string repeated num amount of times using a for loop

    Parameters:
        string: The given string to repeat
        num: The amount of times to repeat the string
    
    Returns: A string containing the given string repeated num amount of times
    """

    # Create empty string with which to iteratively concatenate
    result = ""

    # Iteratively concatenate with result
    for i in range(num):
        result += string

    return result

def while_repeat(string, num):
    """
    Function while_repeat returns the sum of the first n reciprocals using a while loop

    Parameters:
        string: The given string to repeat
        num: The amount of times to repeat the string
    
    Returns: A string containing the given string repeated num amount of times
    """

    # Create empty string with which to iteratively concatenate
    result = ""

    # Iteratively concatenate with result
    while (num > 0):
        result += string
        num -= 1

    return result

def main():
    """
    Function main calls each other function in this file for testing and display

    Parameters: None
    
    Returns: None
    """

    # Calls for_power and while_power for testing & display
    print(f"for_power(3, 0) == {for_power(3, 0)}")
    print(f"for_power(2, 3) == {for_power(2,3)}")
    print(f"for_power(-4, 5) == {for_power(-4, 5)}")
    print(f"while_power(3, 0) == {while_power(3, 0)}")
    print(f"while_power(2, 3) == {while_power(2, 3)}")
    print(f"while_power(-4, 5) == {while_power(-4, 5)}\n-----")

    # Calls for_sum_to and while_sum_to for testing & display
    print(f"for_sum_to(3) == {for_sum_to(3)}")
    print(f"for_sum_to(5) == {for_sum_to(5)}")
    print(f"for_sum_to(0) == {for_sum_to(0)}")
    print(f"while_sum_to(3) == {while_sum_to(3)}")
    print(f"while_sum_to(5) == {while_sum_to(5)}")
    print(f"while_sum_to(0) == {while_sum_to(0)}\n-----")

    # Calls for_repeat and while_repeat for testing & display
    print(f"for_repeat('hello', 3) == {for_repeat('hello', 3)}")
    print(f"for_repeat('goodbye ', 5) == {for_repeat('goodbye ', 5)}")
    print(f"while_repeat('hello', 3) == {while_repeat('hello', 3)}")
    print(f"while_repeat('goodbye ', 5) == {while_repeat('goodbye ', 5)}\n")

# Ensures that code is only ran if it's being directly executed
if __name__ == "__main__":
    main()