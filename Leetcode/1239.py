from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.m = 0
        self.a = arr
        self.dfs(0, '')
        return self.m
    def dfs(self, index, chars):
        is_unique = len(set(chars)) == len(chars)

        if is_unique:
            self.m = max(self.m, len(chars))
        if index == len(self.a) or not is_unique:
            return

        for i in range(index, len(self.a)):
            self.dfs(i+1, chars + self.a[i])

print(Solution().maxLength(["un","iq","ue"]))
print(Solution().maxLength(["cha","r","act","ers"]))
print(Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
print(Solution().maxLength(["aa","bb"]))
print(Solution().maxLength(["a", "abc", "d", "de", "def"]))
print(Solution().maxLength(["ab","cd","cde","cdef","efg","fgh","abxyz"]))
