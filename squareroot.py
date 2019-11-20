# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    res = x ** 0.5
    res = int(res)
    return res
print(mySqrt(8))