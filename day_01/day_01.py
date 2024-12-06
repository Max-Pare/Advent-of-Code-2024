with open('./input.txt', 'r') as file:
    data = [item.split() for item in file.read().strip().split('\n')]
list1, list2 = [], []
for item in data:
    list1.append(int(item[0]))
    list2.append(int(item[1]))
list1 = sorted(list1)
list2 = sorted(list2)

print(len(list1), len(list2))


def part1(l1, l2):
    result = 0
    for i in range(len(l1)):
        result += abs(l1[i] - l2[i])
    print(result)

def part2(l1, l2):
    result = 0
    for item in l1:
        result += item * l2.count(item)
    print(result)

#part1(list1, list2)
part2(list1, list2)