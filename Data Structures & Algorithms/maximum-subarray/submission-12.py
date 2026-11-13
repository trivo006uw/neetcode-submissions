class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in range(len(nums)):
            if curSum < 0:
                curSum = 0
                
            curSum += nums[n]
            maxSum = max(maxSum, curSum)
        
        return maxSum