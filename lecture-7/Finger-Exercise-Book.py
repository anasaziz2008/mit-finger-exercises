# def mult(int1, int2=None):
#     """"If called with two arguments, the function
#         prints the product of the two arguments. If called with one argument,
#         it prints that argument."""

#     if int2 is None:
#         return(int1)
#     else:
#         return(int1 * int2)

# print(mult(3))

# def mult(*args):
#     total = 1
#     for arg in args:
#          total *= arg
#     return total


# print(mult(3, 5, 7, 9))

def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon
    of x."""
    # Find lower bound on ans using a separate variable name
    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1
        
    low = lower_bound - 1
    high = lower_bound + 1
    
    # Perform bisection search
    ans = (high + low)/2
    while abs(base**ans - x) >= epsilon:
        if base**ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
        
    return ans

print(log(20, 8, 0.01))