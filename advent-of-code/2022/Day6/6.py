x = input()
l = len(x)
for i in range(3,l):
    current = x[i-3: i+1]
    print(current)
    if len(set(current)) == 4:
        print(i+1)
        break
