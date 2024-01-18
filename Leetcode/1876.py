class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(3, len(s)+1):
            sub = s[i-3:i]
            if len(set(sub))  == 3:
                answer += 1
        return answer
print(Solution().countGoodSubstrings("xyzzaz"))
print(Solution().countGoodSubstrings("aababcabc"))
