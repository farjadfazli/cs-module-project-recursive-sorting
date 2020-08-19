# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, low, high):
    # base case
    middle = (low + high) // 2
    
    if len(arr) == 0:
        return -1
    
    # move toward the base case

    if low >= high:
        return - 1

    if arr[middle] == target:
        return middle

    else:
        if target > arr[middle]:
            low = middle - 1 # get rid of right side

        if target < arr[middle]:
            high = middle + 1 # get rid of left side

        return binary_search(arr, target, low, high)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

