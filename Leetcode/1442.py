from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        answer = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                a = 0
                for k in range(i,j):
                    a ^= arr[k]

                b = 0
                for k in range(j,n):
                    b ^= arr[k]
                    if a == b:
                        answer += 1
        return answer

print(Solution().countTriplets([2,3,1,6,7]))
print(Solution().countTriplets([1,1,1,1,1]))
