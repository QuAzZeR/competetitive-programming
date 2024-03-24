class Solution:
    def minOperations(self, k: int) -> int:
        operation = None
        if k == 1:
            return 0
        for i in range(1, k):
            c = 0
            if k % i == 0:
                c = i - 1 + k // i - 1
            else:
                c = i - 1 + k // i
            if operation is None:
                operation = c
            if c < operation:
                operation = c

            print(i, i - 1, k // i, c, operation)
        return operation


print(Solution().minOperations(11))
print(Solution().minOperations(1))
