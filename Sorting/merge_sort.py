def merge(arr, low, mid, high):
    n1, n2 = mid-low+1, high-mid
    l, r = [None]*n1, [None]*n2
    for i in range(n1):
        l[i] = arr[i+low]
    for j in range(n2):
        r[j] = arr[mid+j+1]
    i,j,k = 0,0,low
    while i<n1 and j<n2:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k]=r[j]
            j+=1
        k+=1
    while i<n1:
        arr[k] = l[i]
        i += 1; k+=1
    while j<n2:
        arr[k] = r[j]
        j += 1; k+=1

def merge_sort(arr,low,high):
    if low<high:
        mid=(low+high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)
    return arr