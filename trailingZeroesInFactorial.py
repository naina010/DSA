# 12may2020

def trailing_zeroes_in_factorial(n):
    z=0
    while n:
        z+=n//5
        n=n//5
    return z

# print(trailing_zeroes_in_factorial(200))