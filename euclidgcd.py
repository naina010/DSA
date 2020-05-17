# 12may2020

def euclid_gcd(a, b):
    if a == 0: return b
    return euclid_gcd(b % a, a)

# print(euclid_gcd(14,6))


# find multiplicative inverse
# works when a and b are relatively prime, ans belongs to set{0,1,...,m-1}
def extended_euclid(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_euclid(b % a, a)

    x, y = y1 - b // a * x1, x1

    return gcd, x, y

g, mul_inverse, y = extended_euclid(5, 14)
print(mul_inverse, y)