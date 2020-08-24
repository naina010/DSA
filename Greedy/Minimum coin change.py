
# may not work for all denominations => Prefer DP

def minimum_coins(deno, change, n):
    deno.sort(reverse=True)
    i = 0
    num_of_coins = 0
    while i < n:
        while change >= deno[i]:
            change -= deno[i]
            num_of_coins += 1
        i += 1
    return num_of_coins
