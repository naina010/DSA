# Rabin-karp Pattern searching algorithm : O(M.N)

def val(char):
    return ord(char) - 65

def rabin_karp(text, pattern, q):
    n = len(text)
    m = len(pattern)
    d = 128
    h = pow(d, m-1, q)
    p = 0
    t = 0

    for i in range(m):
        p = (d*p + val(pattern[i])) % q
        t = (d*t + val(text[i])) % q

    for s in range(n-m+1):
        if p == t:
            if pattern == text[s:s+m]:
                print('Pattern found at index :', s)
        if s<n-m:
            t = (d*(t - val(text[s])*h) + val(text[s+m])) % q


text = 'ABABDABACDABABCABABCA'
pattern = 'ABABCA'
q = 101  # prime number
rabin_karp(text, pattern, q)


