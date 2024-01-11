class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        for i in range(1,n+1):
            if sum(range(1,i+1)) == sum(range(i,n+1)):
                return i
        return -1
print(Solution().pivotInteger(8))
print(Solution().pivotInteger(1))
print(Solution().pivotInteger(4))
