class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        min_str = list(str(num))
        max_str = list(str(num))
        n = len(num_str)
        max_index = 0
        for i in range(n):
            if num_str[i] != "9":
                max_index = i
                break
        for i in range(n):
            if min_str[i] == num_str[0]:
                min_str[i] = "0"

            if max_str[i] == num_str[max_index]:
                max_str[i] = "9"
        max_val = int("".join(max_str))
        min_val = int("".join(min_str))

        df = max_val - min_val
        return df


print(Solution().minMaxDifference(11891))
print(Solution().minMaxDifference(90))
