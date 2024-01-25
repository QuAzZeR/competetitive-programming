class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        if text1 == text2:
            return l1
        answer = [[0]*(l2+1) for _ in range(l1+1)]
        print(answer)
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    answer[i][j] = answer[i-1][j-1]+1
                else:
                    answer[i][j] = max(answer[i-1][j], answer[i][j-1])
        print(answer)
        return answer[-1][-1]

print(Solution().longestCommonSubsequence("abcde", "abc"))
print(Solution().longestCommonSubsequence("abc", "abc"))
print(Solution().longestCommonSubsequence("abc", "def"))


