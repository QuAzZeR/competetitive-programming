x = int(input())
df = 0
for i in range(30,-1,-1):
    c = 2**i
    if c < x:
       print(c,x)
       df = x-c
       break
print(df+1)
