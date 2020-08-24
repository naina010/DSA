
def minimum_platforms(arrival, departure, n):
    arrival.sort()
    departure.sort()
    platform = temp = 0
    i = j = 0
    while i < n and j < n:
        if arrival[i] <= departure[j]:
            temp += 1
            i += 1
        else:
            temp -= 1
            j += 1
        platform = max(platform, temp)
    return platform

