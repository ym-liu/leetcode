class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs_dict = {}

        for i, num in enumerate(nums):
            if num in diffs_dict:
                return [diffs_dict[num], i]
            diffs_dict[target - num] = i

        return None
