import re


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ln = len(name)
        lt = len(typed)
        if len(set(name)) == 1 and len(set(typed)) == 1 and name[0] == typed[0]:
            return True
        if ln == lt and name != typed:
            return name == typed
        condition = "".join([f"{i}+" for i in name])
        return len(re.findall(f"^{condition}$", typed)) != 0

print(Solution().isLongPressedName("alex", "aalexxxxxx"))
print(Solution().isLongPressedName("saeed", "ssaaedd"))
print(Solution().isLongPressedName("rick", "kric"))
print(Solution().isLongPressedName("alex", "aaleexa"))
