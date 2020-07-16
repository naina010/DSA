
def partition(arr,low,high):
    pivot=arr[high]
    i=j=low
    for i in range(low,high):
        if arr[i]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    arr[j],arr[high]=arr[high],arr[j]
    return j

def quick_sort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
        return arr
