# ===============================================================
# Name: Jude Vargas
# Date: 11/10/2023
# Algorithm: N/A
# References: N/A
# ===============================================================

def binary_search(list: list, target) -> bool:
    """
    Function binary_search performs a binary search on a list, returning True if the item is contained in the list, and False otherwise
    Parameters:
        list: the list to search through for the item
        target: the item to search for within the list
    Returns: True if the item is contained in the list, and False otherwise
    """
    if len(list) == 0:
        return False
    
    # Set indices for each end of the list to start
    first = 0
    last = len(list) - 1

    # Search the list
    while first <= last:
        # Get the index for the current pivot
        mid = (first + last) // 2
        # If the target comes before the pivot, search only the first half
        if target < list[mid]:
            last = mid - 1
        # If it comes after the pivot, search only the second half
        elif target > list[mid]:
            first = mid + 1
        # If the target is the SAME as the pivot, then it has been found
        else:
            return True
    # If the entire list has been searched, then the item is not in the list
    return False

def sequential_search(list: list, target) -> tuple:
    """
    Function sequential_search performs a sequential search on a list and returns True 
    if the item is contained in the list, otherwise False
    Parameters:
        list: the list to search through for the item
        target: the item to search for within the list
    Returns: a tuple with two items:
        - A boolean value indicating whether or not the item was found in the list
        - An integer representing the index of the item, or None if it isn't found
    """
    if len(list) == 0:
        return (False, None)
    loc = 0
    while loc < len(list):
        if target == list[loc]:
            return (True, loc)
        else:
            loc += 1
    return (False, None)

def smart_sequential_search(list: list, target) -> tuple:
    if len(list) == 0:
        return (False, None)
    
    loc = 0
    while loc < len(list):
        if target <= list[loc]:
            if loc == len(list) or target != list[loc]:
                return (False, None)
            else:
                return (True, loc)
        else:
            loc += 1

def recursive_max(list: list) -> int:
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], recursive_max(list[1:len(list)]))

def hash():
    pass