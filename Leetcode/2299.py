import re


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if len(re.findall(r"[a-z]+", password)) == 0:
            return False
        if len(re.findall(r"[A-Z]+", password)) == 0:
            return False
        if len(re.findall(r"[0-9]+", password)) == 0:
            return False
        if len(re.findall(r"[!@#$%^&*()+-]+", password)) == 0:
            return False
        for i in range(1, len(password)):
            if password[i] == password[i - 1]:
                return False
        return True


print(Solution().strongPasswordCheckerII("IloveLe3tcode!"))
print(Solution().strongPasswordCheckerII("Me+You--IsMyDream"))
print(Solution().strongPasswordCheckerII("1aB!"))
