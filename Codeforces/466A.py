n, m, a, b = (int(i) for i in input().split())
s = 0
t = m * a
while n > 0:
    if n >= m and t >= b:
        s += b
        n -= m
    elif n >= m and t < b:
        s += t
        n -= m
    elif n <= m and n * a <= b:
        s += n * a
        n -= n
    elif n <= m and n * a > b:
        s += b
        n -= n
print(s)
