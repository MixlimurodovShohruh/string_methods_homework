def main(s):
    """
    A variable of type str is given. Check that it consists only of numbers.
    Args:
        s: str
    Returns:
        bool: answer
    """
    ans = '12345k6'.isdigit()
    return ans
print(main('s'))