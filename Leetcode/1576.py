class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        ls = list(s)
        if n == 1 and s[0] == "?":
            return "a"

        def get_chr(val1, val2):
            for i in range(97, 123):
                c = chr(i)
                if c != val1 and c != val2:
                    return c
            return "a"

        for i in range(0, n):
            if ls[i] == "?":
                if i == 0:
                    if ls[i + 1] != "?":
                        ls[i] = get_chr(ls[i + 1], ls[i + 1])
                    else:
                        ls[i] = get_chr("b", "b")
                elif i == n - 1:
                    ls[i] = get_chr(ls[i - 1], ls[i - 1])
                else:
                    if ls[i + 1] != "?":
                        ls[i] = get_chr(ls[i - 1], ls[i + 1])
                    else:
                        ls[i] = get_chr(ls[i - 1], ls[i - 1])

        return "".join(ls)


print(Solution().modifyString("?zs"))
print(Solution().modifyString("ubv?w"))
