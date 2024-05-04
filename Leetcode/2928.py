class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        answer = 0
        for i in range(0, limit + 1):
            for j in range(0, limit + 1):
                for k in range(0, limit + 1):
                    if i + j + k == n:
                        answer += 1
        return answer


print(Solution().distributeCandies(5, 2))
print(Solution().distributeCandies(3, 3))
