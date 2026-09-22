# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n

        while True:
            mid = (low + high) // 2
            i = guess(mid)

            if i == -1:
                high = mid - 1
            elif i == 1:
                low = mid + 1
            else:  # i == 0
                return mid
