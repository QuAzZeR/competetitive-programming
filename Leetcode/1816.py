class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split(' ')[0:k])
print(Solution().truncateSentence("Hello how are you Contestant", 4))
print(Solution().truncateSentence("What is the solution to this problem", 4))
print(Solution().truncateSentence("chopper is not a tanuki", 5))
