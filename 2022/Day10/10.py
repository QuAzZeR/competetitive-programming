answer = 0
with open('in', 'r') as f:
    rows = f.readlines()
    cycle = 0
    interesting_cycle = 20
    x = 1
    for row in rows:
        command = row.strip()
        cycle_use = 1
        current_x = x
        if 'addx' in command:
            cycle_use = 2
            value = int(command.split(' ')[-1])
            current_x += value

            # print(current_x, value, x)
        current_cycle = cycle + cycle_use

        if current_cycle >= interesting_cycle:
            print("M", interesting_cycle, cycle,
                  current_cycle, x, current_x, interesting_cycle * x)
            answer += interesting_cycle * x
            cycle = current_cycle
            x = current_x
            interesting_cycle += 40
        # elif current_cycle == interesting_cycle:
        #     cycle = current_cycle
        #     x = current_x
        #     print("E", interesting_cycle, cycle,
        #           current_cycle, x, current_x, interesting_cycle * x)
        #     answer += interesting_cycle * x
        #     interesting_cycle += 40
        else:
            cycle = current_cycle
            x = current_x
print(answer)
