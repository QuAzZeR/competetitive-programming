class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        answer = 0
        left = 0
        right = 0
        window_cost = 0
        while right < len(t):
            window_cost += abs(ord(s[right]) - ord(t[right]))
            while window_cost > maxCost:
                window_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            answer = max(answer, right - left + 1)
            right += 1
        return answer


print(Solution().equalSubstring("abcd", "bcdf", 3))
print(Solution().equalSubstring("abcd", "cdef", 3))
print(Solution().equalSubstring("abcd", "acde", 0))
