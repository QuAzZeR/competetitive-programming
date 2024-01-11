from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = 0
        l = len(arr)
        for i in range(l):
            for j in range(i+1, l):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1, l):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        answer += 1

        return answer

print(Solution().countGoodTriplets([3,0,1,1,9,7], 7, 2, 3))
print(Solution().countGoodTriplets([1,1,2,2,3], 0, 0, 1))
