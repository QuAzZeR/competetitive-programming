from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        d = {nums2[i]:i for i in range(len(nums2))}
        l = len(nums2)
        m = max(nums2)
        # if sorted(nums2,reverse=True) == nums2:
        #     return [-1]*len(nums1)

        for i in nums1:
            if d[i] == l - 1:
                answer.append(-1)
                continue
            elif i == m:
                answer.append(-1)
                continue
            n = m+1
            for j in range(d[i], l):
                if i < nums2[j]:
                    n = nums2[j]
                    break
            if n != m+1:
                answer.append(n)
            else:
                answer.append(-1)
        return answer

print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))
print(Solution().nextGreaterElement([2,4], [1,2,3,4]))
print(Solution().nextGreaterElement([1,4,5,2,4], [5,4,3,2,1]))
