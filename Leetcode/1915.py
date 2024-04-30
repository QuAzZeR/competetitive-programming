class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        p = 0
        answer = 0
        count[0] = 1
        for c in word:
            c_index = ord(c) - ord("a")
            p ^= 1 << c_index
            answer += count[p]
            for i in range(10):
                answer += count[p ^ (1 << i)]
            count[p] += 1
        return answer


print(Solution().wonderfulSubstrings("aba"))
print(Solution().wonderfulSubstrings("aabb"))
print(Solution().wonderfulSubstrings("he"))
