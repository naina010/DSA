# Returns number of trailing zeroes in n!

def trailing_zeroes_in_factorial(n):
    z=0
    while n:
        z+=n//5
        n=n//5
    return z
