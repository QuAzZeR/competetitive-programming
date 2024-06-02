def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    answer = 0
    x = input()
    if x in "codeforces":
        return "Yes"
    return "No"


t = i_in()


for _ in range(t):
    print(solve())
