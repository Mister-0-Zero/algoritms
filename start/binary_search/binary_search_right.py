def binary_search_right_f(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] > target:
            right = mid - 1
        else:
            if arr[mid] == target:
                result = mid
            left = mid + 1

    return result