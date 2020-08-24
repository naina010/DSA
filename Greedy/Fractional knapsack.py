
def fractional_knapsack(arr, total_weight, n):
    for i in range(n):
        value_per_weight = arr[i][0] / arr[i][1]
        arr[i] += [value_per_weight]  # arr => [value, weight, value_per_weight]
    arr.sort(key=lambda x: x[2], reverse=True)
    knapsack = 0
    item = 0
    value = 0
    while knapsack < total_weight:
        if arr[item][1] + knapsack <= total_weight:
            knapsack += arr[item][1]
            value += arr[item][0]
        else:
            value += ((total_weight-knapsack)/arr[item][1]) * arr[item][0]
            knapsack = total_weight
        item += 1

    return value
