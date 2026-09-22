class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # ----- PREPROCESSING -----
        # Each index num represents integer in nums
        #   False if integer doesn't exist in list
        #   True if integer exists in list
        nums_is_exist = [False] * (n + 1)

        for num in nums:
            nums_is_exist[num] = True

        # ----- SCAN FOR FALSE -----
        for i in range(n + 1):
            if not nums_is_exist[i]:
                return i

        return -1
