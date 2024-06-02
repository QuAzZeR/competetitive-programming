class Solution:
    def minimumChairs(self, s: str) -> int:
        answer = 0
        chair = 0
        for i in s:
            if i == "E":
                chair += 1
            else:
                chair -= 1
            answer = max(answer, chair)

        return answer


print(Solution().minimumChairs("EEEEEEE"))
print(Solution().minimumChairs("ELELEEL"))
print(Solution().minimumChairs("ELEELEELLL"))
