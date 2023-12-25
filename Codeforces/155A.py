n = int(input())
score = [int(i) for i in input().split()]
c = 0
all_time_max = 0
all_time_min = 20000
for i in range(1,n):
    max_point = max(score[:i+1])
    min_point = min(score[:i+1])
    if max_point == score[i] and max_point != all_time_max:
        c += 1
    if min_point == score[i] and min_point != all_time_min:
        c += 1
    if all_time_max <  max_point:
        all_time_max = max_point
    if all_time_min > min_point:
        all_time_min = min_point
print (c)