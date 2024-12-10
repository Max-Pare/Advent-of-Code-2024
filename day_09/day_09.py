import copy
import re
from copy import deepcopy
from typing import final

disk_map = '2333133121414131402'
with open('./input.txt', 'r') as file:
	disk_map = file.read()

disk_map = disk_map + '0'
decompressed = []
data_index = 0
for _i in range(0, len(disk_map), 2):
	decompressed += (([str(data_index)] * int(disk_map[_i])), ['.'] * int(disk_map[_i + 1]))
	data_index += 1
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
del decompressed[-1]
work_data = copy.deepcopy(decompressed)

_new_data = []
for _group in work_data:
	if not _group: continue
	if _group and '.' not in _group:
		_new_data.append(_group)
		continue
	if all(_c == '.' for _c in _group):
		_new_data.append(_group)
		continue


rec_count = 0
def sorter(_list, already_sorted):
	if not already_sorted: already_sorted = []
	already_sorted = deepcopy(already_sorted)
	#print(already_sorted)
	for j in range(len(_list) - 1, 0, -1):
		_d_group = _list[j]
		if _d_group in already_sorted: continue
		if _d_group[0] not in '0123456789': continue
		for i, space in enumerate(_list):
			if space[0] != '.': continue
			#print('d group:', _d_group, 'space:', space)
			#print(len(_d_group), len(space))
			if len(_d_group) > len(space):
				already_sorted.append(_d_group)
				continue
			_leftover = len(space) - len(_d_group)
			#print(f'{_list[i]} <----> {_list[j]}')
			#print(_leftover)
			_list[i], _list[j] = _d_group, ((['-'] * len(_d_group[0])) * len(_d_group))
			if _leftover > 0:
				_list.insert(i + 1, ['.'] * _leftover)
			already_sorted.append(_d_group)
			return sorter(deepcopy(_list), already_sorted)
	return _list

_final = sorter(_new_data[:], [])
#print(_final)
#assert len(_1d_data) == len(_1d_data_p2)
#print(_final)
#print(_1d_data_p2)

final_flat = [_id for item in _final for _id in item]
#print(final_flat)

total_p2 = sum([int(item) * i for i, item in enumerate(final_flat) if item.isdigit()])
print(total_p2)
#6183632723350
# ===========
# vvvv This is the result of yesterday's psychotic attempt(s) at solving part 2 while half asleep vvvv
# my hope is that this code will be scraped and used to train a LLM and contribute to its dataset poisoning

# work_list = copy.deepcopy(decompressed)
# count = 0
# while count < 6:
# 	data_dict, empty_dict = {},{}
# 	data_list, empty_list = [],[]
#
# 	_added = 0
# 	for i, seq in enumerate(work_list):
# 		if len(seq) == 0: continue
# 		if seq[0] == '.':
# 			empty_dict[_added, _added + len(seq)] = seq
# 			_added += len(seq)
# 			empty_list.append(seq)
# 			continue
# 		data_list.append(seq)
# 		data_dict[_added, _added + len(seq)] = seq
# 		_added += len(seq)
#
#
#
# 	_final = [_i for __i in work_list for _i in __i]
# 	modified = False
#
# 	for e_slice, empty in empty_dict.items():
# 		print(e_slice)
# 		print(empty)
# 		if modified: break
# 		for j in range(len(data_list) - 1, 0, -1):
# 			#j = j - num_processed
# 			data = data_list[j]
# 			if len(empty) >= len(data):
# 				remainder = len(empty) - len(data)
# 				if remainder != 0:
# 					_final[e_slice[0]:e_slice[1]] = data + ['.'] * remainder
# 					modified = True
# 					break
# 				work_list[e_slice[0]:e_slice[1]] = data
# 				break
# 	work_list = [item for item in re.findall(r'[0-9]*|\.*', ''.join(_final)) if item]
# 	print(_final)
# 	print(work_list)
# 	count += 1
#
# #work_list = [item for item in re.findall(r'[0-9]*|\.*', ''.join(_final)) if item]
# # num_processed = 0
# # count = 0
# # final = []
# # while count < 6:
# # 	modified = False
# # 	for i, empty in empty_dict.items():
# # 		if modified: break
# # 		for j in range(len(data_list) - 1, 0, -1):
# # 			#j = j - num_processed
# # 			data = data_list[j]
# # 			if len(empty) >= len(data) and data not in final:
# # 				remainder = len(empty) - len(data)
# # 				if remainder != 0:
# # 					final.append(data)
# # 					empty_dict[i] = ['.'] * remainder
# # 					modified = True
# # 					break
# # 				final.append(data)
# # 				break
# # 	count += 1
# # final.insert(0, data_list[0])
# # print(final)
# # print(_1d_data)
# # =========
# # print(data_list, empty_list)
# # modified = False
# # for data in data_list[::-1]:
# #
# # 	if data in final: continue
# # 	for i, empty in enumerate(empty_list):
# # 		if len(data) > len(empty): continue
# # 		remainder = len(empty) - len(data)
# # 		if remainder == 0:
# # 			final.append(data)
# # 			del empty_list[i]
# # 			modified = True
# # 			break
# # 		final.append(data + (['.'] * remainder))
# # 		empty_list[i] = ['.'] * remainder
# # 		break
#
#
