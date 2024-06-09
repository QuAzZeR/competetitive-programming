class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        child = 0
        direction = 1
        for i in range(k):
            child += direction
            if child == 0:
                direction = 1
            if child == n - 1:
                direction = -1
        return child

print(Solution().numberOfChild(3,5))
print(Solution().numberOfChild(5,6))
print(Solution().numberOfChild(4,2))
