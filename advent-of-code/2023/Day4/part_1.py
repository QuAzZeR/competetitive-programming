import sys
import math

def solve(lines):
    answer = 0
    for line in lines:
        first, second = line.strip().split(':')[-1].split('|')
        first = [int(x) for x in  first.strip().split(' ') if x != '']
        second = [int(x) for x in second.strip().split(' ') if x != '']
        intersect = list(set(first) & set(second))
        if len(intersect) > 0:
            point = 2**(len(intersect) - 1)
            answer += point


    return answer

lines = open(sys.argv[1]).readlines()
print(solve(lines))
