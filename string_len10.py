def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    a=len(s)
    x=s[0]
    y=s[2]
    z=s[1]
    if a==3 and  x==y and x!=z:
        return "True"
    else:
     return "False"
print(main("222"))

