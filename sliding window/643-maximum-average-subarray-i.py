class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        current_sum = sum(nums[left:right])
        max_avg = current_sum / k

        while right < len(nums):
            current_sum = current_sum - nums[left] + nums[right]
            max_avg = max(max_avg, current_sum / k)
            right += 1
            left += 1

        return max_avg
