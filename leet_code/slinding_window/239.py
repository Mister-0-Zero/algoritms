from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = deque()
        
        for ind, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)

            if ind >= k and nums[ind - k] == q[0]:
                q.popleft()
            
            if ind >= k - 1:
                res.append(q[0])
        
        return res

nums = [3, 1, 2, -1, -2, 4, 2, 4, 6]
k = 3

instance = Solution()
res = instance.maxSlidingWindow(nums=nums, k=k)

print(res)