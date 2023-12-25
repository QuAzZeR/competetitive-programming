n = int(input())
sum_value = sum([int(i) for i in input().split(' ')])

print(int(n*(n+1)/2) - sum_value)
