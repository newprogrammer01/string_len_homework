def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    a=len(s)
    b=a%2
    d=a//2
    e=a//2-1
    if b==1:
       return s[d]
    if b==0:
        return s[e]+s[d]
print(main("jufti"))




