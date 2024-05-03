class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]
        l1 = len(v1)
        l2 = len(v2)
        m = min(l1, l2)
        for i in range(m):
            if v1[i] < v2[i]:
                return -1
            if v1[i] > v2[i]:
                return 1
        if l1 > l2:
            for i in range(m, l1):
                if v1[i] != 0:
                    return 1
        elif l1 < l2:
            for i in range(m, l2):
                if v2[i] != 0:
                    return -1
        return 0


print(Solution().compareVersion("1.01", "1.001"))
print(Solution().compareVersion("1.0", "1.0.0"))
print(Solution().compareVersion("0.1", "1.0"))
