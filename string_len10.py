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
    if a==3 and  x==y:
        return "True"
    if a==3 and x!=y:
        return "False"
    if a>3 and x==y:
        return "False"
    if a<3 and x==y:
        return "False"
    if a<3 and x!=y:
        return "False"
print(main("wew0090"))

