
def selection(arr):
    n = len(arr)

    for i in range(0,n):
        min = i

        for j in range(i, n):
            if arr[j] < arr[min]:
                arr[min], arr[j] = arr[j], arr[min]
                min = i
    return arr
