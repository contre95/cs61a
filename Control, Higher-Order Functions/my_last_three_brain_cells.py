# A k-memory function takes in a single input, prints whether that input was seen exactly k function calls ago, and returns a new k-memory function. For example, a 2-memory function will display “Found" if its input was seen exactly two function calls ago, and otherwise will display “Not found".
# Implement three_memory, which is a three-memory function. You may assume that the value None is never given as an input to your function, and that in the first two function calls the function will display “Not found" for any valid inputs given.
def three_memory(n):
    """
    >>> f = three_memory('first')
    >>> f = f('first')
    Not found
    >>> f = f('second')
    Not found
    >>> f = f('third')
    Not found
    >>> f = f('second')
    Not found
    >>> f = f('second')
    Found
    >>> f = f('third') 
    Found
    >>> f = f('third')
    Not found
    """
    def f(x, y, z):
        def g(i):
            # print(x,y,z)
            if i==x:
                print("Found")
            else:
                print("Not found")
            return f(y,z,i)
        return g
    return f(None, None, n)

