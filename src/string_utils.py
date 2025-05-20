def reverse_string(input_string: str) -> str:
    """
    Reverse the given string using a manual character-by-character approach.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Type checking with additional type hints
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use efficient list comprehension for reversal
    reversed_chars = [input_string[i] for i in range(len(input_string) - 1, -1, -1)]
    
    # Convert list back to string and return
    return ''.join(reversed_chars)