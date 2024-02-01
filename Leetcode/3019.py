class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        answer = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                answer += 1
        return answer


print(Solution().countKeyChanges("aAbBcC"))
print(Solution().countKeyChanges("AaAaAaaA"))
