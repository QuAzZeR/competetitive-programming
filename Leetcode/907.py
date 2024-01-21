from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        answer = sum(arr) + min(arr)
        n = len(arr)
        for i in range(2, n):
            for i in  range
            answer += arr[i] *
        return answer


print(Solution().sumSubarrayMins([3,1,2,4]))
print(Solution().sumSubarrayMins([11,81,94,43,3]))
