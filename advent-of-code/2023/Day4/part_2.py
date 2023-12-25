import sys
import math
def solve(lines):
    answer = 0
    count = 1
    game_count = len(lines)
    instance_count = {i+1: 1 for i in range(game_count)}
    for line in lines:
        first, second = line.strip().split(':')[-1].split('|')
        first = [int(x) for x in  first.strip().split(' ') if x != '']
        second = [int(x) for x in second.strip().split(' ') if x != '']
        intersect = list(set(first) & set(second))
        win = len(intersect)
        if len(intersect) > 0:
            for i in range(count+1, count+win+1):
                if i < game_count+1:
                    instance_count[i] += instance_count[count]
        count += 1
    answer = sum(instance_count.values())
    return answer

lines = open(sys.argv[1]).readlines()
print(solve(lines))
