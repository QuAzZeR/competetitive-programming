from typing import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        answer = deque()
        order_deck = sorted(deck, reverse=True)
        for card in order_deck:
            if len(answer) > 1:
                answer.rotate(1)
            answer.appendleft(card)
        return list(answer)


print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
print(Solution().deckRevealedIncreasing([1, 1000]))
