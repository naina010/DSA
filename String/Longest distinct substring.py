def longest_distinct_substring(s, n):
    i, j = 0, 1
    d = {s[0]: 0}
    mx = 0
    while i<n and j<n:
        if s[j] in d and d[s[j]] >= i:
            mx = max(mx, j-i)
            i = d[s[j]] + 1
            d[s[j]] = j

        else:
            d[s[j]] = j
        j += 1
    mx = max(mx, j-i)
    return mx
