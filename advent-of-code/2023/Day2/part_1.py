import sys


max_red = 12
max_green = 13
max_blue = 14
def solve(games):
    answer = 0 
    for i in range(len(games)):
        _, game = games[i].strip().split(':')

        sets = game.strip().split(';')
        check = True
        for s in sets:
            cubes = s.strip().split(',')
            for cube in cubes:
                no, color = cube.strip().split(' ')
                no = int(no)
                if color == 'red':
                    if no > max_red:
                        check = False
                        break
                    
                elif color == 'blue':
                    if no > max_blue:
                        check = False
                        break
                elif color == 'green':
                    if no > max_green:
                        check = False
                        break
            if not check:
                break
        if check:
            answer += i+1
    return answer
games = open(sys.argv[1]).readlines()
print(solve(games))
