n = int(input())

def solve(): 
    s = input()
    for i in range(n-1):
        if s[i] == 'a' and s[i+1] == 'b':
            return "Yes"
        if s[i] == 'b' and s[i+1] == 'a':
            return "Yes"
    return "No"
print(solve())
