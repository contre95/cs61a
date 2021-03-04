def match_k(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123123)
    False
    """
    def f(x):
        # c = x
        while x>=10**k:
            if x%10**k != (x//10**k)%10**k:
                return False
            x = x // 10**k
        return True
    return f

# def f(x):
    # c = 0
    # while 10 ** (c+k) < x:
        # if (x // 10 ** c) % 10 != (x // 10 ** (c+k)) % 10:
            # return False
        # c = c + 1
    # return True
# return f
