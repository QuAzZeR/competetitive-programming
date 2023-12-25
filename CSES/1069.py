s = input()
current = s[0]
c = 1
m = 1
for i in range(1,len(s)):
    if current != s[i]:
        current = s[i]
        c=1
    else:
        c += 1
        if c > m:
            m = c

print(m)
