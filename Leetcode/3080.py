from typing import List


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        len_nums = len(nums)
        masked = {}
        masked_count = 0
        answer = []
        s = sum(nums)
        new_nums = sorted(
            [(nums[i], i) for i in range(len_nums)], key=lambda x: (x[0], x[1])
        )
        j = 0
        for i, k in queries:
            if i not in masked:
                s -= nums[i]
                masked[i] = 1
            if len(masked) == len_nums:
                break
            if j >= len_nums:
                break
            c = 0
            while j < len_nums:
                if new_nums[j][1] in masked:
                    j += 1
                    continue
                if c >= k:
                    break
                s -= new_nums[j][0]
                masked[new_nums[j][1]] = 1
                c += 1
                j += 1

            answer.append(s)
        return answer + [0] * (len(queries) - len(answer))


print(Solution().unmarkedSumArray([1, 2, 2, 1, 2, 3, 1], [[1, 2], [3, 3], [4, 2]]))
print(Solution().unmarkedSumArray([1, 4, 2, 3], [[0, 1]]))
