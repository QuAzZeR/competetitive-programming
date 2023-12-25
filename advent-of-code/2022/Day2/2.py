with open('i', 'r') as f:
    rows = f.readlines()
    score = 0
    score_map = {
        'A': {
            'X': 3,
            'Y': 1,
            'Z':2,
            },
        'B': {
            'X': 1,
            'Y': 2,
            'Z': 3
            },
        'C': {
            'X': 2,
            'Y': 3,
            'Z': 1
            }
,}
    calculate = {
            'AX': 0,
            'AY': 3,
        'AZ': 6,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 0,
        'CY': 3,
        'CZ': 6,
            }

    for row in rows:
        r = row.strip()
        print(r)
        a,b = r.split(' ')
        score += score_map[a][b] + calculate[f'{a}{b}']

    print(score)



