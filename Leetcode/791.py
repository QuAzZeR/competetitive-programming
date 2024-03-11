class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {chr(i): 1000 for i in range(97, 123)}
        for j in range(len(order)):
            d[order[j]] = j
        answer = sorted(s, key=lambda x: d[x])
        return "".join(answer)


print(Solution().customSortString("cba", "abcd"))
print(Solution().customSortString("bcafg", "abcd"))
