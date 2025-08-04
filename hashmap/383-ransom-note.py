from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # create dict from magazine string
        # where each key is unique char
        # and val is num of occurrences of that char
        dictionary = defaultdict(int)
        for c in magazine:
            dictionary[c] += 1

        # iterate through ransomNote, check if char exists in dict
        # decrement num of occurences left if exists in dict
        for c in ransomNote:
            if dictionary[c] == 0:
                return False
            dictionary[c] -= 1

        return True
