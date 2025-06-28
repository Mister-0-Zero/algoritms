class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        right = len(nums) - 1
        left = 0

        #случай исключение
        if len(nums) == 1:
            if target == nums[0]: return True
            return False
        
        #находим где происходит поворот, чтобы отделить отсортированные части массивов
        while right - 1 != left:

            val_r = nums[right]
            val_l = nums[left]

            mid = (right + left) // 2
            val_mid = nums[mid]
            # print(left, mid, right, val_l, val_mid, val_r)
            if val_l == val_mid == val_r and val_l > nums[left + 1]:
                right = left + 1
                break
            elif val_l == val_mid == val_r:
                left +=1
            elif val_mid >= val_l and val_mid > val_r:
                left = mid
            else:
                right = mid
            
        print(left, right)
        
        #настраиваем указатели для бинарного поиска
        if nums[left] < nums[right]: #поворота не было
            left = 0
            right = len(nums) - 1
        elif target == nums[-1]: #одинаковые числа
            return True
        elif target > nums[-1]: # target в левой половине
            right = left
            left = 0
        else:  # target в правой половине
            left = right
            right = len(nums) - 1

        #бинарный поиск
        while right >= left:
            
            mid = (right + left) // 2
            num = nums[mid]

            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


instanse = Solution()
nums = [1,3]
for target in [1,2,3]:
    res = instanse.search(nums, target)
    print(res)