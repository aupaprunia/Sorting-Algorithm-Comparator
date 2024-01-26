
def quick_sort_3_median_main(arr):
    low = 0
    high = len(arr) - 1
    quick_sort_3_median(arr, low, high)
    return arr

def quick_sort_3_median(arr,low,high):
    if low < high:
        pi = partition_3_median(arr, low, high)

        quick_sort_3_median(arr, low, pi-1)
        quick_sort_3_median(arr, pi+1, high)

def find_median(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
    return high-1


def partition_3_median(arr, low, high):
    pivot_index = find_median(arr, low, high)
    pivot = arr[pivot_index]

    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[pivot_index] = arr[pivot_index], arr[i+1]

    return i+1