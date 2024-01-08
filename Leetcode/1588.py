from typing import List
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        answer = sum(arr)
        for i in range(3, len(arr)+1, +2):
            for j in range(len(arr)-i+1):
                answer += sum(arr[j:j+i])
        return answer
print(Solution().sumOddLengthSubarrays([1,4,2,5,3]))
print(Solution().sumOddLengthSubarrays([1,2]))
print(Solution().sumOddLengthSubarrays([10,11,12]))

