class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(i) for i in n])

print(Solution().minPartitions("32"))
print(Solution().minPartitions("82734"))
print(Solution().minPartitions("27346209830709182346"))
