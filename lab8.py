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

def reverse(string):
    """
    Function reverse returns a given string with its characters in reverse order

    Parameters:
        string: the string to return in reverse order

    Returns: The given string with its characters in reverse order
    """
    result = ""
    for i in range(len(string) - 1, -1, -1):
        result += string[i]
    return result

def remove_letter(string, remove):
    """
    Function remove_letter returns a given string with all instances of a given letter removed

    Parameters:
        string: the string to check
        remove: the letter to remove from the string

    Returns: The given string with all instances of the given letter removed
    """
    result = ""
    for i in string:
        if i != remove:
            result += i
    return result

def palindrome(string):
    """
    Function palindrome returns True or False depending on if a given string is a palindrome

    Parameters:
        string: the string to check if its a palindrome

    Returns: True if the given string is a palindrome, else False
    """
    return string == reverse(string)

def remove_string(string, remove):
    """
    Function remove_string returns a given string with all instances of a second given string removed from it

    Parameters:
        string: the string to check
        remove: the string to remove from the main string

    Returns: The given string with all instances of the second given string removed
    """
    return string.replace(remove, '')

def encrypt(string, key):
    """
    Function encrypt returns an encrypted string based off a given normal string and a cipher key

    Parameters:
        string: the string to encrypt
        key: the cipher key with which to encrypt the given string

    Returns: The given string, encrypted using the cipher key
    """
    return

def decrypt(string, key):
    """
    Function decrypt returns a decrypted string based off a given encrypted string and a cipher key

    Parameters:
        string: the encrypted string to decrypt
        key: the cipher key with which to decrypt the given string

    Returns: They given string, decrypted using the cipher key
    """
    return

def main():
    print(remove_string)

# Executes the main function only if the file is being executed directly
if __name__ == "__main__":
    main()