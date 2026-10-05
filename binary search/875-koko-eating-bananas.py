class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)

        while lower < upper:
            mid = (upper + lower) // 2

            hours_needed = 0
            for pile in piles:
                hours_needed += -(-pile // mid)

            if hours_needed > h:
                lower = mid + 1
            else:
                upper = mid

        return lower
