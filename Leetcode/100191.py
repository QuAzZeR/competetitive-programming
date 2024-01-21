class Solution:
    def minimumPushes(self, word: str) -> int:
        w = len(word)
        count = 1
        answer = 0
        while w > 0:
            if w>=8:
                answer += 8*count
                count += 1
                w -= 8
            else:
                answer += w * count
                w -= w%8
                count += 1
        return answer

print(Solution().minimumPushes("abcde"))
print(Solution().minimumPushes("xycdefghij"))
