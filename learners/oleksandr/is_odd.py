def is_odd(number):
    """
    Check if a number is odd.

    Parameters:
    - number: The number to check. Should be an integer.

    Returns:
    - bool: True if the number is odd, False otherwise.
    - str: "Invalid input" if the input is not an integer.
    """
    try:
        # Attempt to convert the input to an integer
        num = int(number)

        # Check if the number is odd
        return num % 2 != 0
    except ValueError:
        # Handle the case where the input is not an integer
        return "Invalid input"

assert is_odd(4) == False

assert is_odd(1) == True

assert is_odd(1)

assert is_odd('hello') == "Invalid input"

assert is_odd('@')
