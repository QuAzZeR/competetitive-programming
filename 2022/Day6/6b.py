x = input()
l = len(x)
for i in range(13,l):
    current = x[i-13: i+1]
    print(current)
    if len(set(current)) == 14:
        print(i+1)
        break
