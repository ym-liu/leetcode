class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for word in strs:
            word_freq_array = 26 * [0]
            for char in word:
                word_freq_array[ord(char) - ord("a")] += 1

            anagrams_dict[tuple(word_freq_array)].append(word)

        return list(anagrams_dict.values())
