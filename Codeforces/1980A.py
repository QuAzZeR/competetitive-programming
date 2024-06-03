from collections import Counter


def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    answer = 0
    n, m = i_map()
    a = input()
    d = Counter(a)
    for i in ["A", "B", "C", "D", "E", "F", "G"]:
        if i in d:
            answer += 0 if d[i] > m else m - d[i]
        else:
            answer += m

    return answer


t = i_in()


for _ in range(t):
    print(solve())
