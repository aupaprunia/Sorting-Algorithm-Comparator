
def heapsort(arr):
    arr.insert(0,0)
    build_heap(arr)
    n = len(arr)-1
    for i in range(n, 0,-1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(arr,1, i-1)
    return arr[1:]

def build_heap(arr):
    n = len(arr)-1
    for i in range((n//2),0, -1):
        arr = heapify(arr,i,n)

def heapify(arr, i, n):
    maximum = i
    left = 2*i
    right = (2*i) + 1
    if (left <= n):
        if (arr[left] > arr[maximum]):
            maximum = left

    if (right <= n):
        if (arr[right] > arr[maximum]):
            maximum = right

    if maximum != i:
        arr[i], arr[maximum] = arr[maximum], arr[i]
        heapify(arr, maximum, n)
    return arr
