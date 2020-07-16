# Time complexity - O(N^2)

def count_distinct_substrings(s, n):
    p = 31
    hash = [0]
    mod = 10 ** 9 + 7
    p_pow = [1]*n
    for i in range(1, n):
        p_pow[i] = (p_pow[i - 1] * p) % mod

    for i in range(n):
        hash.append((hash[i] + (ord(s[i]) - 96) * p_pow[i]) % mod)

    substrings = set()
    h = []
    for l in range(1, n+1):
        for i in range(n-l+1):
            substrings.add((((hash[i+l] - hash[i] + mod) % mod) * p_pow[n-1-i]) % mod)
            h.append((s[i:i+l], (((hash[i+l] - hash[i] + mod) % mod) * p_pow[n-1-i]) % mod))

    return len(substrings)
