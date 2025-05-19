<<<<<<< HEAD
def reverse_string(input_string):
    """
    Reverse the given input string manually, without using slice notation or reverse().
=======
def reverse_string(input_string: str) -> str:
    """
    Reverse a given string without using built-in reversal methods.
>>>>>>> pr-23-labrocadabro-task-tester

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
<<<<<<< HEAD
    # Convert string to list of characters
    chars = list(input_string)
    
    # Manually reverse the list of characters
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters from both ends
=======
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert string to list of characters for manipulation
    chars = list(input_string)
    
    # Reverse the list using two-pointer technique
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
>>>>>>> pr-23-labrocadabro-task-tester
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
<<<<<<< HEAD
    # Convert list back to string and return
=======
    # Convert back to string
>>>>>>> pr-23-labrocadabro-task-tester
    return ''.join(chars)