from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ### First Solution
        # selected = Counter(sorted(nums, reverse=True)[:k])
        # answer = []
        # for i in nums:
        #     if i in selected and selected[i] > 0:
        #         selected[i] -= 1
        #         answer.append(i)
        # return answer

        ### Second Solution
        tuple_nums = [(i, nums[i]) for i in range(len(nums))]
        selected_tuple_nums = sorted(tuple_nums, key=lambda x: (-x[1], x[0]))[:k]
        return [i[1] for i in sorted(selected_tuple_nums, key=lambda x: (x[0]))]


print(Solution().maxSubsequence([2, 1, 3, 3], 2))
print(Solution().maxSubsequence([-1, -2, 3, 4], 3))
print(Solution().maxSubsequence([3, 4, 3, 3], 2))
