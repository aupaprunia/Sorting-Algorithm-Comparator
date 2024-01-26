
def bubblesort(arr):

    for element in arr:
        i = 0
        while i < len(arr)-1:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
    return arr

# arr = [6,4,7,2,1]
# arr = bubblesort(arr)
# print(arr)