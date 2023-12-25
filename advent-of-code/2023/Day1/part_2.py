import re
import sys
m = {
'one': '1',
'two': '2',
'three': '3',
'four': '4',
'five': '5',
'six': '6',
'seven': '7',
'eight': '8',
'nine': '9'

}
def solve(lines):
    s = 0
    for line in lines:
        c = [i for i in line if i >= '1' and i <='9']
        value = 0 
        if len(c) >= 2:
            value = int(f'{c[0]}{c[-1]}')
        else:
            value = int(f'{c[0]}{c[0]}')
        s += value

    return s

def convert(text):
    new_text = ''
    i = 0
    while i <len(text):
        c = False
        for k in m:
            if k == text[i:i + len(k)]:
                c = True
                new_text += m[k]
        if not c:
            new_text += text[i]
        i += 1
    return new_text
        
with open(sys.argv[1], 'r') as f:
    lines = f.read()
    lines = convert(lines)
    lines = re.sub(r'[a-zA-Z]', '', lines).split('\n')[:-1]
    print(lines)
    print(solve(lines))

