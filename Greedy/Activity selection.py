
def activity_selection(arr, n):
    for i in range(n):
        arr[i] = (*arr[i], i+1)  # set meeting ids
    arr.sort(key=lambda x:x[1])
    poss_activities = [1]
    for i in range(1, n):
        prev_activity = poss_activities[-1]-1
        if arr[i][0] > arr[prev_activity][1]:
            poss_activities.append(i+1)
    for e in poss_activities:
        print(arr[e-1][2], end=' ')   # print meeting ids


arr = [(5, 7), (1, 2), (3, 4), (0, 6), (8, 9), (5, 9)]
activity_selection(arr, len(arr))
