import re
def p1_oneliner(): # python mfs be like but it's pythonic!
    result = sum([int(a) * int(b) for a,b in
                  [re.search(r'[0-9]{1,3},[0-9]{1,3}', item).group().split(',')
                   for item in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', open('input.txt', 'r').read())]])
    print(result)

def main():
    data = open('input.txt', 'r').read()
    found = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', data)
    result = 0
    do = True
    for item in found:
        if item[:3] == 'mul':
            if not do: continue
            sp = re.search(r'[0-9]{1,3},[0-9]{1,3}', item).group().split(',')
            result += int(sp[0]) * int(sp[1])
        if item[:3] == 'don':
            do = False
        else:
            do = True
        continue
    print(result)
main()