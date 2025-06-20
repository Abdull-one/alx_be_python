def safe_divide(numerator, denominator):
    """
    Performs division, handling potential errors such as division by zero
    and non-numeric inputs.

    Args:
        numerator (str): The numerator as a string.
        denominator (str): The denominator as a string.

    Returns:
        str: A message indicating the result of the division or an error message.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."