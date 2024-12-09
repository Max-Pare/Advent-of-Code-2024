import copy

disk_map = '2333133121414131402'
with open('./input.txt', 'r') as file:
	disk_map = file.read()

disk_map = ''.join(disk_map[::] + '0')
decompressed = []
data_index = 0
for i in range(0, len(disk_map), 2):
	decompressed += [str(data_index)] * int(disk_map[i]) + ['.'] * int(disk_map[i + 1])
	data_index += 1
data, empty = [],[]
for i in range(len(decompressed)):
	if decompressed[i] == '.':
		empty.append(i)
		continue
	data.append(i)
defragged = copy.copy(decompressed)
for j in range(len(empty)):
	defragged[empty[j]] = decompressed[data[-(j + 1)]]
defragged = defragged[0:len(data):] + ['.'] * (len(empty))
total = sum([i * int(defragged[i]) for i in range(len(defragged)) if defragged[i] != '.'])
print(total)