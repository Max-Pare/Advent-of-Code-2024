with open('./input.txt', 'r') as file:
    data = [line.split() for line in file.read().split('\n')]

class LevelUnsafeError(Exception):
    pass

def is_safe(line):
    line = [int(item) for item in line]
    def subcheck(_line, graced):
        last_direction = None
        last_val = None
        for index, val in enumerate(_line):
            try:
                if last_val is None:
                    last_val = val
                    continue
                diff = last_val - val
                abs_diff = abs(diff)
                last_val = val
                if abs_diff == 0 or abs_diff > 3: raise LevelUnsafeError()
                direction = diff > 0
                if last_direction is None: last_direction = direction
                if direction is not last_direction: raise LevelUnsafeError()
            except LevelUnsafeError:
                if graced: return False
                return index - 1
        return True
    result = subcheck(line, False)
    if type(result) is bool:
        if result:
            return result
    if type(result) is not int: raise ValueError
    del(line[result])
    result = subcheck(line, True)
    if type(result) is not bool: raise ValueError
    return result


safe_count = 0
for line in data[::]:
    if len(line) == 0: continue
    safe_count += int(is_safe(line))
print(safe_count)
#634