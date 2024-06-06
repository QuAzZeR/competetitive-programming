from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        for i in range(n):
            if hand[i] == -1:
                continue
            val = hand[i]
            count = 0
            for j in range(i, n):
                if val == hand[j]:
                    hand[j] = -1
                    val += 1
                    count += 1
                if count == groupSize:
                    break
            if count != groupSize:
                return False
        return True


print(Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
print(Solution().isNStraightHand([1, 2, 3, 4, 5], 4))

print(Solution().isNStraightHand([1, 2, 3, 3, 4, 4, 5, 6], 4))
print(Solution().isNStraightHand([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
print(Solution().isNStraightHand([1, 2, 3, 4], 3))
