class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        answer = 0
        l = len(word)
        for i in range(l):
            is_contain_letter = False
            for j in range(i + 5, l + 1):
                d = {
                    "a": 0,
                    "e": 0,
                    "i": 0,
                    "o": 0,
                    "u": 0,
                }
                s = word[i:j]
                for c in s:
                    if c not in d:
                        is_contain_letter = True
                        break
                    d[c] += 1
                if is_contain_letter:
                    break
                if (
                    d["a"] > 0
                    and d["e"] > 0
                    and d["i"] > 0
                    and d["o"] > 0
                    and d["u"] > 0
                ):
                    answer += 1
        return answer


print(Solution().countVowelSubstrings("aeiouu"))
print(Solution().countVowelSubstrings("unicornarihan"))
print(Solution().countVowelSubstrings("cuaieuouac"))
