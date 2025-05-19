def reverse_string(input_string):
    """
    Reverse the given string using a manual character-by-character approach.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Enhanced type checking with more explicit validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Efficient string reversal using list comprehension
    reversed_chars = [input_string[i] for i in range(len(input_string) - 1, -1, -1)]
    
    # Convert list back to string
    return ''.join(reversed_chars)