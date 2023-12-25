def get_current(x, current):
    z = current % 40
    if z >= x and z <= x+2:
        return '#'
    return '.'


answer = 0
m = []
with open('in', 'r') as f:
    rows = f.readlines()
    cycle = 0
    interesting_cycle = 20
    x = 1
    current_row = ''

    for row in rows:
        command = row.strip()
        cycle_use = 1
        current_x = x
        if 'addx' in command:
            cycle_use = 2
            value = int(command.split(' ')[-1])
            current_x += value
            if (cycle+1) % 40 == 0:
                current_row += get_current(x, cycle+1)
                m.append(current_row)
                current_row = ''
            else:
                current_row += get_current(x, cycle+1)

            if (cycle+2) % 40 == 0:
                current_row += get_current(x, cycle+2)
                m.append(current_row)
                current_row = ''
            else:
                current_row += get_current(x, cycle+2)
        if 'noop' in command:
            if (cycle+1) % 40 == 0:
                current_row += get_current(x, cycle+1)
                m.append(current_row)
                current_row = ''
            else:
                current_row += get_current(x, cycle+1)

        cycle += cycle_use
        x = current_x
        print(cycle, x)
        print(current_row)
        # print(current_x, value, x)
        # elif current_cycle == interesting_cycle:
        #     cycle = current_cycle
        #     x = current_x
        #     print("E", interesting_cycle, cycle,
        #           current_cycle, x, current_x, interesting_cycle * x)
        #     answer += interesting_cycle * x
        #     interesting_cycle += 40

print('\n'.join(m))
