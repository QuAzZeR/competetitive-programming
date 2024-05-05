from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = [i for i in nums if i % 2 != 0]
        even = [i for i in nums if i % 2 == 0]
        answer = []
        for i in range(len(nums) // 2):
            answer.append(even[i])
            answer.append(odd[i])
        return answer


print(Solution().sortArrayByParityII([4, 2, 5, 7]))
print(Solution().sortArrayByParityII([2, 3]))
