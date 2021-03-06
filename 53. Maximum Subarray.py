class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        else:
            cur = prev = 0
            res = float('-inf')
            for i in range(len(nums)):
                cur = nums[i] + (prev if prev > 0 else 0)
                prev = cur
                res = max(cur, res)
            return res
