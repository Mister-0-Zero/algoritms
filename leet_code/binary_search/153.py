class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        
        while right - 1 != left:

            mid = (right + left) //2

            val_l = nums[left]
            val_mid = nums[mid]
            val_r = nums[right]

            # print(val_l, val_mid, val_r)
            if val_mid > val_l and val_mid > val_r:
                if nums[mid + 1] < val_mid:
                    return nums[mid + 1]
                else:
                    left = mid + 1
            else:
                if nums[mid - 1] > val_mid:
                    return nums[mid]
                else:
                    right = mid - 1
        
        return nums[right]


instance = Solution()
nums_mass =  [[3,4,5,1,2], [4,5,6,7,0,1,2], [11,13,15,17]]
for nums in nums_mass:
    res = instance.findMin(nums)
    print(res)