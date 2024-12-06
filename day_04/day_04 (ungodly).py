import collections

def scan(data):
    def findxmas(string):
        return string.count(TARGET) + string.count(TARGET[::-1])
        #return len(re.findall(f'{TARGET}', string)) + len(re.findall(f'{TARGET[::-1]}', string))

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
    def diag__(data):
        data_d = {(y,x):data[y][x] for y in range(len(data)) for x in range(len(data[0]))}
        parents = {}
        max_y, max_x = len(data) - 1, len(data[0]) - 1
        for y in range(len(data)):
            for x in range(len(data[0])):
                results = {'R': [], 'L':[]}
                if (x - 1 < 0) or (x + 1 > max_x) or (y - 1 < 0) or (y + 1 > max_y):
                    parents[(y,x)] = {'R':[data[y][x]], 'L':[data[y][x]]}
                    continue
                #top left > bottom right
                if parents.get((y - x, 0), ''): parents[(y - x, 0)]['R'].append(data[y][x])
                # top right > bottom left
                if parents.get((y - x, 9), ''): parents[(y - x, 9)]['L'].append(data[y][x])
                if parents.get((0, x + y), ''): parents[(0, x + y)]['L'].append(data[y][x])
        total = 0
        for key, value in parents.items():
            print(key, value)
            total += findxmas(''.join(value['R'])) + findxmas(''.join(value['L']))
        return total
    def diag_(data, dir_='R'): # works(?)
        total = 0
        try:
            direction = {'R':1, 'L':-1}[dir_]
        except KeyError:
            raise KeyError('diag() takes either L or R')
        if direction == 1:
            checked = set()
            for row_i in range(len(data)):
                for col_i in range(len(data[0])):
                    found = [data[row_i][col_i]]
                    _id = str(row_i) + str(col_i)
                    if _id in checked: continue
                    checked.add(_id)
                    for leftover in range(1, len(data[0]) - col_i + 1):
                        x,y = row_i + leftover, col_i + leftover
                        if any((z > len(data) - 1 for z in (x,y))):
                            continue
                        found.append(data[x][y])
                        checked.add(str(x) + str(y))
                    _checkedlist = list(checked)
                    if collections.Counter(_checkedlist) != collections.Counter(checked):
                        raise ValueError("Duplicates found")
                    total += findxmas(''.join(found))
            return total
        else:
            checked = set()
            tempcounter = 0
            for row_i in range(len(data)):
                for col_i in range(len(data[0]) - 1, 0, -1):
                    found = [data[row_i][col_i]]
                    _id = str(row_i) + str(col_i)
                    if _id in checked: continue
                    checked.add(_id)
                    for leftover in range(1, col_i + 1):
                        x,y = row_i + leftover, col_i - leftover
                        __id = str(x) + str(y)
                        if __id in checked: break
                        if any(z > len(data) - 1 or z < 0 for z in (x,y)):
                            continue
                        checked.add(__id)
                        found.append(data[x][y])
                        checked.add(str(x) + str(y))
                        tempcounter += 1
                    _checkedlist = list(checked)
                    if collections.Counter(_checkedlist) != collections.Counter(checked):
                        raise ValueError("Duplicates found")
                    if len(found) < len(TARGET): continue
                    total += findxmas(''.join(found))
            print(f'{tempcounter} iterations, data length is {len(data)}x{len(data[0])} ({len(data)*len(data[0])})')
            return total
    diagcount = diag(data)
    vercount = ver(data)
    horcount = hor(data)
    return diagcount + vercount + horcount
TARGET = 'XMAS'
total = 0
modes = {'ver', 'hor', 'diagR', 'diagL'}
#_data = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA"\
#        "\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX".split('\n')
with open('input.txt','r') as file:
    _data = file.read().split('\n')
print(scan(_data))
#1008
#1860
#1856
#1972
#2327
#2344 !!!