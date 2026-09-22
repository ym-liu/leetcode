class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = {}  # s[i]: freq

        # build char frequency hashmap
        for c in s:
            if c in char_freq:
                char_freq[c] += 1
            else:
                char_freq[c] = 1

        # if t has letter s doesnt
        for d in t:
            if d in char_freq:
                char_freq[d] -= 1
                if char_freq[d] == 0:
                    char_freq.pop(d)
            else:
                return False

        # is s has letters t doesnt
        if char_freq:
            return False

        return True
