from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        a = sorted(arr)
        answer = [[a[i], a[i+1]] for i in range(len(a)-1)]
        m = 10**5
        for i in answer:
            if m > i[1] - i[0]:
                m = i[1] - i[0]
        return [i for i in answer if i[1]-i[0] == m]

print(Solution().minimumAbsDifference([4,2,1,3]))
print(Solution().minimumAbsDifference([1,3,6,10,15]))
print(Solution().minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
