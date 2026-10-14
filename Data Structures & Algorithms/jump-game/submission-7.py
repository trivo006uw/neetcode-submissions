class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # furthest = 0
        # for i in range(len(nums)):
        #     if i > furthest:
        #         return False
        #     furthest = max(furthest, i + nums[i])
            
        # if furthest >= len(nums) - 1:
        #         return True

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0