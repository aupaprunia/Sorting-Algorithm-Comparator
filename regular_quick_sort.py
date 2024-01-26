
def quick_sort_main(arr):
    low = 0
    high = len(arr) - 1
    quick_sort(arr, low, high)
    return arr

def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

# arr = [1,3,2,9,6,4]
# low = 0
# high = len(arr) - 1

# quick_sort(arr, low, high)

# print(arr)