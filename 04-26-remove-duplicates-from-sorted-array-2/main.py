class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 0
        for read in range(len(nums)):
            if write >= 2 and nums[read] == nums[write - 2]:
                continue
            nums[write] = nums[read]
            write += 1
        return write
