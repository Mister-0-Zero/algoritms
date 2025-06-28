from itertools import chain

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        one_dimensional = list(chain.from_iterable(matrix))

        right = len(one_dimensional) - 1
        left = 0

        while right >= left:
            
            mid = (right + left) // 2
            num = one_dimensional[mid]

            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 2
instance = Solution()
res = instance.searchMatrix(matrix=matrix, target=target)
print(res)