# Determine whether an integer is a palindrome

def is_palindrome(x):
    """
    >>> is_palindrome(123)
    False
    >>> is_palindrome(121)
    True
    >>> is_palindrome(-121)
    False
    """

    return str(x) == str(x)[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()