def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (a>=10 and a<=99) or (a<=-10 and a>=-99)
print (main(91))