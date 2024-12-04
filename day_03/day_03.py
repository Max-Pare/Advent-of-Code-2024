import re
result = sum([int(a) * int(b) for a,b in
              [re.search(r'[0-9]{1,3},[0-9]{1,3}', item).group().split(',')
               for item in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', open('input.txt', 'r').read())]])
print(result)