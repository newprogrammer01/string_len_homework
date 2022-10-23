def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a=len(s1)
    b=len(s2)
    c=len(s3)
    if a%2==1 and b%2==1 and c%2==1:
        return [s1, s2, s3]
    if a%2==0 and b%2==0 and c%2==0:
        return 
    if a%2==0 and b%2==1 and c%2==0:
         return [s2]
    if a%2==0 and b%2==0 and c%2==1:
        return [s3]
    if a%2==1 and b%2==0 and c%2==0:  
        return [s1]
    if a%2==1 and b%2==1 and c%2==0:
        return [s1,s2]
    if a%2==1  and b%2==0 and c%2==1:
        return [s1,s3]
    if a%2==0 and b%2==1 and c%2==1:
        return [s2,s3]
print(main('code ', 'coder' , 'python'))


