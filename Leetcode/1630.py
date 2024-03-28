from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        answer = []
        m = len(l)
        for i in range(m):
            left = l[i]
            right = r[i]
            sub = sorted(nums[left : right + 1], reverse=True)
            diff = sub[1] - sub[0]
            is_correct = True
            for i in range(2, len(sub)):
                if diff != sub[i] - sub[i - 1]:
                    is_correct = False
            answer.append(is_correct)
        return answer


print(
    Solution().checkArithmeticSubarrays(
        nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]
    )
)
print(
    Solution().checkArithmeticSubarrays(
        nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
        l=[0, 1, 6, 4, 8, 7],
        r=[4, 4, 9, 7, 9, 10],
    )
)
