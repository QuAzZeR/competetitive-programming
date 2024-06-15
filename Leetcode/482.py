class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        answer = []
        l = [i for i in s if i != "-"][::-1]
        n = len(l)
        for i in range(0, n, k):
            answer.append(l[i : i + k])
        return "-".join(["".join(i) for i in answer]).upper()[::-1]


print(Solution().licenseKeyFormatting(s="5F3Z-2e-9-w", k=4))
print(Solution().licenseKeyFormatting(s="2-5g-3-J", k=2))
