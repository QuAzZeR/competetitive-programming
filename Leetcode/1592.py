class Solution:
    def reorderSpaces(self, text: str) -> str:
        space = 0
        for i in text:
            if i == " ":
                space += 1
        words = [i for i in text.split(" ") if i != ""]
        n = len(words)
        if n == 1 and space == 0:
            return words[0]
        if n == 1:
            return words[0] + " " * space

        n_space = space // (n - 1)
        answer = ""
        for i in range(n):
            answer += words[i]
            if i != n - 1:
                answer += " " * n_space
        answer += " " * (space - (n_space * (n - 1)))
        return answer


print(Solution().reorderSpaces("  this   is  a sentence "))
print(Solution().reorderSpaces(" practice   makes   perfect"))
print(Solution().reorderSpaces("  hello"))
