import collections

def part1(data):
    def findxmas(string):
        return string.count(TARGET) + string.count(TARGET[::-1])
        #return len(re.findall(f'{TARGET}', string)) + len(re.findall(f'{TARGET[::-1]}', string)) # why would I do this

    def ver(data):
        verline = []
        for x in range(len(data[0])):
            line = []
            for y in range(len(data)):
                line.append(data[y][x])
            verline.append(line)
        return sum([findxmas(''.join(sub)) for sub in verline])

    def hor(data):
        return sum([findxmas(line) for line in data])

    def diag(data):
        max_x = len(data[0]) - 1
        max_y = len(data) - 1
        left_to_right = set([(y,x) for y in range(len(data)) for x in range(len(data[0])) if y == 0 or x == 0])
        right_to_left = set([(y,x) for y in range(len(data)) for x in range(len(data[0])) if y == 0 or x == max_x])
        found = []
        for y, x in left_to_right:
            next_y, next_x = y + 1, x + 1
            collected = [data[y][x]]
            while next_y <= max_y and next_x <= max_x:
                collected.append(data[next_y][next_x])
                next_x += 1
                next_y += 1
            if collected: found.append(''.join(collected))
        for y, x in right_to_left:
            next_y, next_x = y + 1, x - 1
            collected = [data[y][x]]
            while next_y <= max_y and next_x >= 0:
                collected.append(data[next_y][next_x])
                next_x += -1
                next_y += 1
            if collected: found.append(''.join(collected))
        total = 0
        for f in found:
            total += findxmas(f)
        return total
    return diag(data) + ver(data) + hor(data)
def part2(data):
    def findstr(string, target):
        return target in string or target[::-1] in string
    data_d = {(y,x):data[y][x] for y in range(len(data)) for x in range(len(data[0]))}
    clocks = ((-1,1),(1,-1)), ((-1,-1),(1,1))
    crosses = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            char = data[y][x]
            if char != "A": continue
            cross = []
            for clock in clocks:
                cross.append([data_d.get((y + clock[0][0],x + clock[0][1]), ''),
                              'A',
                              data_d.get((y + clock[1][0], x + clock[1][1]), '')])
            crosses.append(cross)
    total = 0
    for cross in crosses:
        if all([findstr(''.join(item), 'MAS') for item in cross]): total+=1
    print(total)


TARGET = 'XMAS'
total = 0
#_data = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA"\
#        "\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX".split('\n')
with open('input.txt','r') as file:
    _data = file.read().split('\n')
#print(part1(_data))
print(part2(_data))
