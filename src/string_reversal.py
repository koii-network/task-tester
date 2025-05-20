def reverse_string(input_string):
    """
    Reverse the given input string efficiently.

    This implementation provides a performant string reversal method
    that works across different Python versions and string types.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Type checking
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use optimal slice notation for efficiency
    return input_string[::-1]