class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1[0] != s2[0] or s2[0] != s3[0] or s1[0] != s3[0]:
            return -1
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        m = min([l1, l2, l3])
        for i in range(m):
            if s1[i] != s2[i] or s2[i] != s3[i] or s1[i] != s3[i]:
                return l1 - i + l2 - i + l3 - i

        return l1 - m + l2 - m + l3 - m


print(Solution().findMinimumOperations("abc", "abb", "ab"))
print(Solution().findMinimumOperations("dac", "bac", "cac"))
