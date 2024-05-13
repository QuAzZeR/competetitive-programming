class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        if numOnes >= k:
            return k
        if numOnes + numZeros >= k:
            return numOnes
        return numOnes - (k - numOnes - numZeros)


print(Solution().kItemsWithMaximumSum(3, 2, 0, 2))
print(Solution().kItemsWithMaximumSum(3, 2, 0, 4))
print(Solution().kItemsWithMaximumSum(6, 6, 6, 13))
