class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters) - 1
        low = 0
        high = n

        while low <= high:
            mid = (low + high) // 2

            if letters[mid] == target:

                # while-loop in case repeating characters in a row,
                # e.g., letters=[c,c,c,c,c], target=c
                while letters[mid] == target:
                    if mid >= n:
                        return letters[0]
                    mid += 1
                return letters[mid]

            elif letters[mid] < target:

                # if target DNE in letters list
                if mid < n and letters[mid + 1] > target:
                    return letters[mid + 1]

                low = mid + 1

            else:  # letters[mid] > target
                high = mid - 1

        return letters[0]
