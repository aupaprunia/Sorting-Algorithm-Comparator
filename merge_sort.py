
def merge(arr1, arr2):
    final_arr = []

    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] > arr2[0]:
            final_arr.append(arr2[0])
            arr2.pop(0)
        else:
            final_arr.append(arr1[0])
            arr1.pop(0)
        
    while len(arr1) != 0:
        final_arr.append(arr1[0])
        arr1.pop(0)
    
    while len(arr2) != 0:
        final_arr.append(arr2[0])
        arr2.pop(0)
    
    return final_arr

def mergesort(arr):
    n = len(arr)

    if n == 1:
        return arr
    
    l1 = arr[:(n//2)]
    l2 = arr[(n//2):]

    l1 = mergesort(l1)
    l2 = mergesort(l2)

    return merge(l1,l2)
