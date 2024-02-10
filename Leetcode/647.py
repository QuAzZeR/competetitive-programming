class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        l = len(s)
        for i in range(l):
            for j in range(l):
                x = s[i : j + 1]
                if x == "":
                    continue
                if x == x[::-1]:
                    answer += 1

        return answer


print(Solution().countSubstrings("abc"))
print(Solution().countSubstrings("aaa"))
