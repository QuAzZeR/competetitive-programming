from itertools import accumulate


_ = int(input())
cnt = [0] * (10**6 + 10)
MAX = 10**6 + 1
for i in map(int, input().split(" ")):
    cnt[i] += 1
cnt = list(accumulate(cnt))
answer = 0
for i in range(1, MAX):
    d = cnt[i] - cnt[i - 1]
    if d != 0:
        for j in range(i, MAX, i):
            k = j // i
            answer += k * (cnt[min(MAX, i + j - 1)] - cnt[j - 1]) * d
    answer -= d * (d + 1) // 2

print(answer)
