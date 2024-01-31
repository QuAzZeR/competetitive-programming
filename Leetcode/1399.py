from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        answer = 0
        d = defaultdict(int)
        for i in range(1, n + 1):
            s = str(i)
            sum_n = sum([int(j) for j in s])
            d[sum_n] += 1

        m = max(d.values())
        for i in d:
            if d[i] == m:
                answer += 1
        return answer


print(Solution().countLargestGroup(13))
print(Solution().countLargestGroup(2))
print(Solution().countLargestGroup(24))
