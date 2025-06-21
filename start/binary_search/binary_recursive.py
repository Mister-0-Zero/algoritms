def binary_recursive_f(arr: list[int], target: int, left: int, right: int) -> int:

    if left > right:
        return -1
    
    mid = (right + left) // 2
    
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_recursive_f(arr, target, left, mid - 1)
    else:
        return binary_recursive_f(arr, target, mid + 1, right)