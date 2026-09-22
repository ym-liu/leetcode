class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_nonzero_index = 0
        n = len(nums)

        for i in range(n):
            if nums[i] != 0:
                nums[last_nonzero_index] = nums[i]
                last_nonzero_index += 1

        for j in range(last_nonzero_index, n):
            nums[j] = 0
