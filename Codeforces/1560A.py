t = int(input())
seq = []
c = 1
while True:
    if len(seq) > 1000:
        break
    if c %3 != 0 and str(c)[-1] != '3':
        seq.append(c)
    c+=1
for i in range(t):
    print(seq[int(input())-1])