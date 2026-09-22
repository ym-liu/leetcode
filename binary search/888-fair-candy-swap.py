class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # 1. need to know diff in # candies -> O(n)
        # 2.a. can brute force: go thru each of Alice's boxes & compare with each of Bob's boxes -> O(n^2)
        # 2.b. alternatively, maybe sort Bob's boxes -> O(n log n)
        #      and then do same as brute force, but can use binary search -> O(n log n)

        # 1. DIFFERENCE IN CANDIES
        difference = sum(aliceSizes) - sum(bobSizes)

        # 2. SORT BOB's BOXES
        bobSizes.sort()

        # 2. FOR EACH OF ALICE'S BOXES', BINARY SEARCH FOR DIFFERENCE IN BOB'S BOXES
        for aliceSize in aliceSizes:
            low = 0
            high = len(bobSizes) - 1

            # difference / 2 = aliceSize - bobSize
            # because if one gives the other 1 candy then the diff is actually +2
            target = aliceSize - (difference / 2)

            while low <= high:
                mid = (low + high) // 2
                bobSize = bobSizes[mid]

                if bobSize == target:
                    return [aliceSize, bobSize]

                # want to look for smaller bobSize
                elif bobSize > target:
                    high = mid - 1

                # want to look for bigger bobSize
                else:
                    low = mid + 1
