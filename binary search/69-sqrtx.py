class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x

        while low <= high:
            mid = (low + high) // 2
            square = mid**2

            if square == x or ((mid + 1) ** 2 > x and square < x):
                return mid
            elif square < x:
                low = mid + 1
            else:  # square > x
                high = mid - 1

        return -1
