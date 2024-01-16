from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        answer = 0
        for i in range(n):
            for j in range(1,len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    answer += 1
                    break
        return answer

print(Solution().minDeletionSize(["cba","daf","ghi"]))
print(Solution().minDeletionSize(["a","b"]))
print(Solution().minDeletionSize(["zyx", "wvu", "tsr"]))
