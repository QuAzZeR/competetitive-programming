from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        v = [int(i) for i in str(k)]
        if n <= 10:
            return [int(i) for i in str(int("".join([str(i) for i in num])) + k)]
        a = 0
        j = len(v) - 1
        i = n - 1
        while i >= 0:
            s = num[i] + a
            if j >= 0:
                s = num[i] + v[j] + a
            num[i] = s % 10
            a = s // 10
            j -= 1
            i -= 1
        if a != 0:
            if i < 0:
                num = [a] + num
            else:
                num[i] = num[i] + a
        return num


print(Solution().addToArrayForm([1, 2, 0, 0], 34))
print(Solution().addToArrayForm([2, 7, 4], 181))
print(Solution().addToArrayForm([2, 1, 5], 806))
print(Solution().addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1))
