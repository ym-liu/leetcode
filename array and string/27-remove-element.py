class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # index of last array element to switch with
        switchIdx = len(nums) - 1

        # iterate through nums array
        for i in range(len(nums)):

            # if we find val to remove, switch with last array element that isn't ==val
            if nums[i] == val:

                # if last element ==val, decrement idx until !=val
                while nums[switchIdx] == val and switchIdx >= i:
                    switchIdx -= 1

                # if no more array elements to switch with
                if switchIdx < i:
                    break

                # switch in-place
                nums[i] = nums[switchIdx]
                switchIdx -= 1

        # return num of elements != val
        return switchIdx + 1
