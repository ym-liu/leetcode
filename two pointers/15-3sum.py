class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i]:  # skip duplicates
                continue

            two_sum_target = 0 - num

            # then it just becomes a two sum II problem!
            left = i + 1
            right = len(nums) - 1

            while left < right:
                lr_sum = nums[left] + nums[right]

                if lr_sum == two_sum_target:
                    triplet = [num, nums[left], nums[right]]
                    left += 1
                    right -= 1
                    if answer and triplet == answer[-1]:  # skip duplicates
                        continue
                    answer.append(triplet)

                elif lr_sum > two_sum_target:
                    right -= 1
                else:
                    left += 1

        return answer
