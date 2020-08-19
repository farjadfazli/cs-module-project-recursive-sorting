# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # compare the first element of each array
    # smaller element goes into merged array

    arrA_idx = 0
    arrB_idx = 0

    for idx in range(elements):
        # check if we are at the end of one of the arrays
        # if so, just use other array
        if arrA_idx >= len(arrA):
            merged_arr[idx] = arrB[arrB_idx]
            arrB_idx += 1
        
        elif arrB_idx >= len(arrB):
            merged_arr[idx] = arrA[arrA_idx]
            arrA_idx += 1
        
        elif arrA[arrA_idx] < arrB[arrB_idx]:
            merged_arr[idx] = arrA[arrA_idx]
            arrA_idx += 1
        else:
            merged_arr[idx] = arrB[arrB_idx]
            arrB_idx += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        # recurse on left half
        left = merge_sort(arr[:mid])
        # recurse on right half
        right = merge_sort(arr[mid:])
        # put things back together (merge)
        arr = merge(left, right)    

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input

def merge_in_place(arr, start, mid, end):
    start2 = mid + 1
    while start <= mid and start2 <= end:
        if arr[start] < arr[start2]:
            start += 1

        else:
            value = arr[start2]
            idx = start2
            while idx != start:
                arr[idx] = arr[idx - 1]
                idx -= 1
            arr[start] = value

            start += 1
            start2 += 1
            mid += 1


def merge_sort_in_place(arr, left, right):
    if right < left:
        return arr

    else:
        middle = (right - left) // 2
        merge_sort_in_place(arr, left, middle)
        merge_sort_in_place(arr, middle + 1, right)
        merge_in_place(arr, left, middle, right)

    return arr
