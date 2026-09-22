from collections import Counter


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_counter = Counter(arr)

        for i in arr:

            if (i == 0 and arr_counter[0] >= 2) or (i != 0 and arr_counter[i * 2] >= 1):
                return True

        return False
