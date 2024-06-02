def i_in():
    return int(input())


def solve():
    answer = "Division "
    x = i_in()
    if 1900 <= x:
        answer += "1"
    elif 1600 <= x:
        answer += "2"
    elif 1400 <= x:
        answer += "3"
    elif 1399 >= x:
        answer += "4"
    return answer


t = i_in()


for _ in range(t):
    print(solve())
