# String hashing

def compute_hash(s):
    p = 31
    hash = 0
    mod = 10**9+7
    p_pow = 1
    for c in s:
        hash = (hash + (ord(c)-96)*p_pow)%mod
        p_pow = (p_pow*p)%mod
    return hash
