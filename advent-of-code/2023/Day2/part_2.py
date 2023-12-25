import sys


def solve(games):
    answer = 0 
    for i in range(len(games)):
        _, game = games[i].strip().split(':')

        sets = game.strip().split(';')
        max_red = 0
        max_green = 0
        max_blue = 0
        for s in sets:
            cubes = s.strip().split(',')
            for cube in cubes:
                no, color = cube.strip().split(' ')
                no = int(no)
                if color == 'red':
                    if no > max_red:
                        max_red = no
                    
                elif color == 'blue':
                    if no > max_blue:
                        max_blue = no
                elif color == 'green':
                    if no > max_green:
                        max_green = no
        answer += max_red * max_blue * max_green
    return answer
games = open(sys.argv[1]).readlines()
print(solve(games))

