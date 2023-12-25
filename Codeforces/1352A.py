t = int(input())
for _ in range(t):
    x = input()[::-1]
    c = 0
    round = {}
    for i in range(len(x)):
        value = int(x[i]) * 10**i
        if value != 0:
            round[value] = 1
    print(len(round))
    print(' '.join([str(i) for i in round.keys()]))