import copy
import re
from typing import final
import sys
#with open('./input.txt', 'r') as file:
#	disk_map = file.read()

disk_map = disk_map + '0'
decompressed = []
data_index = 0
for _i in range(0, len(disk_map), 2):
	decompressed += (([str(data_index)] * int(disk_map[_i])), ['.'] * int(disk_map[_i + 1]))
	data_index += 1
__PART_2__ = True
if not __PART_2__:
	_1d_data = [char for item in decompressed for char in item]
	data, empty = [],[]
	for _i in range(len(_1d_data)):
		if _1d_data[_i] == '.':
			empty.append(_i)
			continue
		data.append(_i)
	data_compact = copy.copy(_1d_data)
	for _j in range(len(empty)):
		data_compact[empty[_j]] = data_compact[data[-(_j + 1)]]
	data_compact = data_compact[0:len(data):] + ['.'] * (len(empty))
	total_p1 = sum([i * int(data_compact[i]) for i in range(len(data_compact)) if data_compact[i] != '.'])
	print(total_p1)
# ===========
# I give up