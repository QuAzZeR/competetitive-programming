from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        answer = 0
        d = defaultdict(int)
        for i in range(lowLimit, highLimit +1):
            box = sum([int(j) for j in str(i)])
            d[box] += 1
            if d[box] > answer:
                answer = d[box]
        print(d)
        return answer

print(Solution().countBalls(1,10))
print(Solution().countBalls(5,15))
print(Solution().countBalls(19,28))
