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

def two_max(a, b):
    """
    Function two_max returns the greater of two numbers

    Parameters:
        a: the first number to compare
        b: the second number to compare

    Returns: the greater of a and b
    """
    
    # Returns the larger value between a and b
    return a if a > b else b

def two_min(a, b):
    """
    Function two_min returns the lesser of two numbers

    Parameters:
        a: the first number to compare
        b: the second number to compare

    Returns: the lesser of a and b
    """
    
    # Returns the lower value between a and b
    return a if a < b else b

def three_max_v1(a, b, c):
    """
    Function three_max_v1 returns the greatest of three numbers

    Parameters:
        a: the first number to compare
        b: the second number to compare
        c: the third number to compare

    Returns: the greatest of a, b, and c
    """
    
    # Return a if it is the largest of the three values
    if a > b and a > c:
        return a
    
    # If a is NOT the largest value, return the larger value between b and c
    return b if b > c else c

def three_max_v2(a, b, c):
    """
    Function three_max_v2 returns the greatest of three numbers

    Parameters:
        a: the first number to compare
        b: the second number to compare
        c: the third number to compare

    Returns: the greatest of a, b, and c
    """
    
    # Get the maximum value between a and b, then return the maximum value between that value and c
    return two_max(two_max(a, b), c)

def is_odd(a):
    """
    Function is_odd returns whether or not a number is odd

    Parameters:
        a: the number to check for parity

    Returns: True if a is odd, else False
    """
    
    # Return True if a is odd, else return False
    return a % 2 != 0

def length(s):
    """
    Function length returns the length of the given string

    Parameters:
        s: the string of which to check the length

    Returns: the length of the given string
    """
    
    # Increment count by 1 for each character in the string, then return count
    count = 0
    for i in s:
        count += 1
    return count

def sum_odd(n):
    """
    Function sum_odd returns the sum of all odd integers between 1 and n exclusive

    Parameters:
        n: the exclusive upper bound of the list of integers to check
        
    Returns: the sum of all odd integers between 1 and n exclusive
    """
    
    # Create a list of numbers within range that are odd, then return the sum of that list
    return sum([x for x in range(n) if x % 2 != 0])

def sum_series(m, n):
    """
    Function sum_series returns the sum of all numbers between 1 and m exclusive that are divisible by n

    Parameters:
        m: the exclusive upper bound of the list of integers to check
        n: the integer by which to check if each integer is divisible

    Returns: the sum of all numbers between 1 and m exclusive that are divisible by n
    """
    
    # Create a list of numbers within range that are divisible by n, then return the sum of that list
    return sum([x for x in range(m) if x % n == 0])

def my_max(aList):
    """
    Function my_max returns the greatest element in a list of numbers

    Parameters:
        aList: the list of numbers of which to get the highest number

    Returns: the greatest element in aList
    """
    
    # Assume a minimum value of 0 for any list given
    largest = 0
    
    # Iterate through list and update largest every time a larger number than largest is encountered
    for i in aList:
        if i > largest:
            largest = i
    return largest

def my_min(aList):
    """
    Function my_min returns the smallest element in a list of numbers

    Parameters:
        aList: the list of numbers of which to get the lowest number

    Returns: the smallest element in aList
    """
    
    # Assume a maximum value of 1000 for any list given
    smallest = 1000
    
    # Iterate through list and update smallest every time a smaller number than smallest is encountered
    for i in aList:
        if i < smallest:
            smallest = i
            
    return smallest


#Definiton of function main that calls and tests the functions above
def main():
    """
    Function main calls other functions in this file for testing and display

    Parameters: None

    Returns: None
    """
    
    # Call each other function in this file and display their respective results
    print(f"1. {two_max(3, 5)}")
    print(f"2. {two_min(3, 5)}")
    print(f"3. {three_max_v1(4, 2, 11)}")
    print(f"4. {three_max_v1(4, 2, 11)}")
    print(f"5. {is_odd(20)}")
    print("6.", length("apple"))
    print(f"7. {sum_odd(13)}")
    print(f"8. {sum_series(20, 5)}")
    print(f"9. {my_max([12,2,32,22])}")
    print(f"10. {my_min([12,2,32,22])}")
    

#Call and execute the function main only if code is being executed directly
if __name__ == "__main__":
    main()
