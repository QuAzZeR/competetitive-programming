class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""
            i = 0
            while i < len(s):
                print("S", s[i : i + k])
                new_s += str(sum(list(map(int, s[i : i + k]))))
                print(">>>>", new_s)
                i += k
            s = new_s
            print(">>", s)
        return s


print(Solution().digitSum("11111222223", 3))
print(Solution().digitSum("00000000", 3))
print(Solution().digitSum("1234", 2))
