class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            num_s = str(num)
            digits = []
            for c in num_s:
                digits.append(int(c))
            if i == sum(digits):
                return i
        return -1
