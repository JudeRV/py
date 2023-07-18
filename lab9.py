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

def separate_characters(s):
    """
    Function separate_characters splits a single string into a list of all of its characters in order
    
    Parameters:
        s: The string to split into a list
        
    Returns: A list containing each character from the string in order
    """
    
    # Appends each character from s into result separately
    result = []
    
    for i in s:
        result.append(i)
        
    return result

def has_duplicates(a_list):
    """
    Function has_duplicates returns True if the given list has any duplicate values
    
    Parameters:
        a_list: The list to check for any duplicate values
        
    Returns: True if the list has any duplicate values, else False
    """
    
    # Returns True if a duplicate value is found, or False if no duplicates are found
    previous_values = []
    for i in a_list:
        if i in previous_values:
            return True
        else:
            previous_values.append(i)
    return False

def remove_duplicates(a_list):
    """
    Function remove_duplicates returns the given list with any duplicate values removed
    
    Parameters:
        a_list: The list of values from which to remove duplicates
        
    Returns: the updated list, free of duplicates
    """
    
    # Add each item in a_list to result if the value isn't already in result
    result = []
    
    for i in a_list:
        if i not in result:
            result.append(i)
            
    return result

def union(aList, bList):
    """
    Function union returns a list containing all the items contained in either aList or bList (with no duplicates)
    
    Parameters:
        aList: The first list to check for new values
        bList: The second list to check for new values
        
    Returns: A list containing all the items contained in either aList or bList (with no duplicates)
    """
    
    # Iterate through both aList and bList, adding any non-duplicate values to result
    return remove_duplicates(aList + bList)

def intersect(aList, bList):
    """
    Function intersect returns a list of all the items that occur in BOTH aList and bList (with no duplicates)
    
    Parameters:
        aList: One of the lists to check for shared items
        bList: The other list to check for shared items
        
    Returns: A list containing all the items contained in BOTH aList and bList  (with no duplicates)
    """
    
    # Iterate through both aList and bList, appending any non-duplicate shared items to result
    result = []
    
    for i in aList:
        if i in aList and i in bList and i not in result:
            result.append(i)
            
    for i in bList:
        if i in aList and i in bList and i not in result:
            result.append(i)
            
    return result

def difference(aList, bList):
    """
    Function difference returns a list of all the items in aList but NOT in bList (with no duplicates)
    
    Parameters:
        aList: The list to check if each item is in it
        bList: the list to check if each item is NOT in it
        
    Returns: A list containing all the items in aList but NOT in bList (with no duplicates)
    """
    
    # Checks each item in aList and appends it to result if it's not in bList and it's not a duplicate
    result = []
    
    for i in aList:
        if i not in bList and i not in result:
            result.append(i)
            
    return result

def is_letter(c):
    """
    Function is_letter returns True if c is a valid English letter, or it returns False otherwise
    
    Parameters:
        c: The character to check
        
    Returns: True if c is a valid English letter, else False
    """
    
    # Return True if the character's ASCII value is within the limits for letters
    value = ord(c)
    if value <= 90 and value >= 65:
        return True
    return value <= 122 and value >= 97

def separate_words(s):
    """
    Function separate_words splits a string of space-separated words into a list of those words in order
    
    Parameters:
        s: The string to separate into a list
        
    Returns: A list containing all of the words in the string, in order
    """
    
    # Initialize the resulting list and a string for each word
    result = []
    current_word = ""
    
    for i in range(len(s)):
        # If the current character is a valid letter, add it to the current word
        if is_letter(s[i]):
            current_word += s[i]
            
            # Append the current word to the end of result if the final character is a valid letter
            if i == len(s) - 1:
                result.append(current_word)
        else:
            # Append the current word to the end of result if the current word is finished being built, then reset it for the potential next word
            if current_word != "":
                result.append(current_word)
            current_word = ""
    
    return result

def join_words(glue_symbol, a_list):
    """
    Function join_words joins a list of words together with a string in between each word into a single string
    
    Parameters:
        glue_symbol: The string that will be inserted between each word
        a_list: A list of strings to join together
        
    Returns: A string containing the words in the list joined by the glue_symbol
    """
    
    # Add each word and the glue symbol to a string
    result = ""
    for i in a_list:
        result += i + glue_symbol
        
    # There shouldn't be a glue symbol after the final word, so return the string with the final symbol omitted
    return result[:-len(glue_symbol)]

def is_anagram(s1, s2):
    """
    Function is_anagram returns True if s1 and s2 are valid anagrams, or returns False otherwise
    
    Parameters:
        s1: The first string to check
        s2: The second string to check
        
    Returns: True if s1 and s2 are anagrams, else False
    """
    
    # Remove each letter in s1 from s2, then just check to see if s2 is empty. If it is, then the words are valid anagrams.
    for i in s1:
        c = s2.find(i)
        if c != -1:
            s2 = s2[:c] + s2[c+1:]
            
    return s2 == ""

def main():
    """
    Function main calls the other functions in this file for testing and display
    
    Parameters: None
    
    Returns: None
    """
    print(f"separate_characters('king kong') == {separate_characters('king kong')}")
    print(f"separate_characters('whirlwind') == {separate_characters('whirlwind')}\n-----")
    
    print(f"has_duplicates([1,2,4,3,5,2,3, 3]) == {has_duplicates([1,2,4,3,5,2,3, 3])}")
    print(f"has_duplicates([1,2,3,5,4,6,8,10,12]) == {has_duplicates([1,2,3,5,4,6,8,10,12])}\n-----")
    
    print(f"remove_duplicates([1,2,4,3,5,2,3, 3]) == {remove_duplicates([1,2,4,3,5,2,3, 3])}")
    print(f"remove_duplicates([1,2,3,5,4,6,8,10,12]) == {remove_duplicates([1,2,3,5,4,6,8,10,12])}\n-----")
    
    print(f"union([1,2,4,4], [5,5,6,8,9]) == {union([1,2,4,4], [5,5,6,8,9])}")
    print(f"union([6,13,7,28], [28,17,11,0]) == {union([6,13,7,28], [28,17,11,0])}\n-----")
    
    print(f"intersect([1,2,4,4], [5,5,6,8,9]) == {intersect([1,2,4,4], [5,5,6,8,9])}")
    print(f"intersect([6,13,7,28], [28,17,11,0]) == {intersect([6,13,7,28], [28,17,11,0])}\n-----")
    
    print(f"difference([1,2,4,4], [5,5,6,8,9]) == {difference([1,2,4,4], [5,5,6,8,9])}")
    print(f"difference([6,13,7,28], [28,17,11,0]) == {difference([6,13,7,28], [28,17,11,0])}\n-----")
    
    print(f"separate_words('king kong') == {separate_words('king kong')}")
    print(f"separate_words('This short      sentence   has                 several words in it') == {separate_words('This short      sentence   has                 several words in it')}\n-----")
    
    print(f"join_words(':-:', ['This', 'is', 'a', 'list','of', 'words']) == {join_words(':-:', ['This', 'is', 'a', 'list','of', 'words'])}")
    print(f"join_words('hello', ['This', 'is', 'a', 'second', 'list', 'of', 'words']) == {join_words('hello', ['This', 'is', 'a', 'second', 'list', 'of', 'words'])}\n-----")
    
    print(f"is_anagram('racecar', 'driving') == {is_anagram('racecar', 'driving')}")
    print(f"is_anagram('players', 'parsley') == {is_anagram('players', 'parsley')}")
    
# Ensures that code is only ran if it's being directly executed
if __name__ == "__main__":
    main()