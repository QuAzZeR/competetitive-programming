from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.answer = []
        d = {i: len(i) for i in wordDict}

        n = len(s)
        words = set(wordDict)

        def dfs(index):
            sub_str = []
            if index == n:
                sub_str.append("")
            for i in range(index + 1, n + 1):
                prefix = s[index:i]
                if prefix in words:
                    suffixes = dfs(i)
                    for suffix in suffixes:
                        sub_str.append(prefix + ("" if suffix == "" else " ") + suffix)

            return sub_str

        return dfs(0)


print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(
    Solution().wordBreak(
        "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
    )
)
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
