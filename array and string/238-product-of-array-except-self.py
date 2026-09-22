class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products_except_self = n * [None]

        # prefixes
        product = 1
        for i, num in enumerate(nums):
            products_except_self[i] = product
            product = product * num

        # suffixes
        product = 1
        for j, num in enumerate(nums[::-1]):
            products_except_self[n - j - 1] *= product
            product = product * num

        return products_except_self
