class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2
            
            v_l = nums[left]
            v_m = nums[mid]
            v_r = nums[right]

            # print(v_l, v_m, v_r)
            if v_l == v_m == v_r:
                left += 1
            elif v_m > v_r and v_m >= v_l:
                left = mid + 1
            else:
                right = mid

        return nums[min(left, right)]

instance = Solution()
nums_mass =  [[3,4,5,1,1,1,2], [4,5,6,7,0,1,2,4], [11,13,15,17], [0]]
for nums in nums_mass:
    res = instance.findMin(nums)
    print(res)
    print()