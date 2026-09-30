class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = 0
        start = 0
        unique_chars = dict()

        for i, c in enumerate(s):
            if c in unique_chars and unique_chars[c] >= start:
                max_substring = max(max_substring, i - start)
                start = unique_chars[c] + 1

            unique_chars[c] = i

        return max(max_substring, len(s) - start)
