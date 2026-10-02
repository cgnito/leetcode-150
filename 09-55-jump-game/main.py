class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = nums[0]

        for i in range(len(nums)-1):
            if i > max_reach:
                return False
            max_reach = max(max_reach, nums[i] + i)

            if max_reach >= len(nums) -1:
                return True

        return False
