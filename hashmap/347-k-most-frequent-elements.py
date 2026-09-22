class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = defaultdict(int)
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        k_most_freq = []

        for num in nums:
            nums_freq[num] += 1

        for num in nums_freq:
            freq_buckets[nums_freq[num]].append(num)

        for bucket in freq_buckets[::-1]:
            if bucket != []:
                k_most_freq.extend(bucket)
            if len(k_most_freq) == k:
                break

        return k_most_freq
