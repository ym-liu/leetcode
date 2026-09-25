class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m * n) - 1

        while left <= right:
            mid = (left + right) // 2
            i = mid // n
            j = mid % n

            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                right = mid - 1
            else:
                left = mid + 1

        return False
