from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        print(d)
        answer = 0
        is_odd_exist = 0
        for i in d:
            if d[i] % 2 != 0:
                is_odd_exist = 1
            if d[i] >= 2:
                answer += d[i] // 2 * 2

        return answer + is_odd_exist


print(Solution().longestPalindrome("abccccdd"))
print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("bb"))
