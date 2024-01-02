class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = sum([i for i in range(1,n+1) if i%m != 0])
        num2 = sum([i for i in range(1,n+1) if i%m == 0])
        return num1 - num2
print(Solution().differenceOfSums(10,3))
print(Solution().differenceOfSums(5,6))
print(Solution().differenceOfSums(5,1))
