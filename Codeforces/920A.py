T = int(input())
for _ in range(T):
    w = 0
    h = 0
    xx,yy= map(lambda x: int(x), input().split())
    for i in range(3):
        x,y = map(lambda x: int(x), input().split())
        if y != yy:
            h = abs(y-yy)
        if x != xx:
            w = abs(x-xx)
    print(h*w)
