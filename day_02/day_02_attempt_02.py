import copy

from jinja2.runtime import TemplateReference


class UnsafeException(Exception):
    pass

with open('./input.txt', 'r') as file:
    data = [[int(item) for item in line.split()] for line in file.read().split('\n')]

# 7 6 4 2 1
def subcheck_recursive(rep, strict:bool):
    lastdir = None
    for index, val in enumerate(rep[:]):
        if index == 0: continue
        try:
            last_val = rep[index - 1]
            diff = last_val - val
            absdiff = abs(diff)
            if absdiff not in safediff:
                raise UnsafeException(f"{last_val} - {val} ({absdiff}) not in {safediff}")
            direction = diff > 0
            if lastdir is None:
                lastdir = direction
                continue
            if direction is not lastdir:
                raise UnsafeException(str(direction) + " is not " + str(lastdir))
        except UnsafeException as e:
            print(str(e), end='')
            if strict:
                print(", can't try again, FAILING!")
                print()
                return False
            print(" but we can try again!")
            print(f"Removing {rep[index]} from {rep}")
            newrep = copy.deepcopy(rep)
            del newrep[index]
            print(f"New rep is {newrep}")
            return subcheck_recursive(newrep, True)
    return True

def subcheck(rep, strict:bool):
    lastdir = None
    for index, val in enumerate(rep[:]):
        if index == 0: continue
        try:
            last_val = rep[index - 1]
            diff = last_val - val
            absdiff = abs(diff)
            if absdiff not in safediff:
                raise UnsafeException(f"{last_val} - {val} ({absdiff}) not in {safediff}")
            direction = diff > 0
            if lastdir is None:
                lastdir = direction
                continue
            if direction is not lastdir:
                raise UnsafeException(str(direction) + " is not " + str(lastdir))
        except UnsafeException as e:
            print(str(e), end='\n')
            if strict: return False
            for i in range(len(rep)):
                newrep = copy.deepcopy(rep)
                del newrep[i]
                if subcheck(newrep, True): return True
            return False
    return True

safe_count = 0
safediff = {1, 2, 3}
for report in data[:]:
    safe_count += int(subcheck(report, False))
print(safe_count)

#634