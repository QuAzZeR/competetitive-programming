from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        l = len(prices)
        for i in range(l):
            current = prices[i]
            discount = 0
            for k in range(i+1, l):
                if current >= prices[k]:
                    discount = prices[k]
                    break
            answer.append(current-discount)
        return answer

print(Solution().finalPrices([8,4,6,2,3]))
print(Solution().finalPrices([1,2,3,4,5]))
print(Solution().finalPrices([10,1,1,6]))
