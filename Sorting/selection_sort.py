def selection_sort(arr, n):
    for i in range(n):
        mn = i
        for j in range(i+1, n):
            if arr[j] < arr[mn]:
                mn = j
        arr[i], arr[mn] = arr[mn], arr[i]
