class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # key = num in nums
        # val = upper bound for a subsequence containing that num
        upper_dict = {}

        # key = num in nums
        # val = lower bound for a subsequence containing that num
        lower_dict = {}

        # populate dict
        for num in nums:
            if num in upper_dict:
                continue

            num_below = num - 1
            num_above = num + 1

            if num_above in upper_dict:
                upper_dict[num] = upper_dict[num_above]
            else:
                upper_dict[num] = num

            if num_below in lower_dict:
                lower_dict[num] = lower_dict[num_below]
            else:
                lower_dict[num] = num

            upper_dict[lower_dict[num]] = upper_dict[num]
            lower_dict[upper_dict[num]] = lower_dict[num]

        # now iterate to get biggest diff between num and upper
        max_subsequence = 0
        for num in upper_dict:
            subsequence = upper_dict[num] - num + 1
            if subsequence > max_subsequence:
                max_subsequence = subsequence

        return max_subsequence
