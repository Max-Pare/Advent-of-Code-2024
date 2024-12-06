import copy
import os
from idlelib.pyparse import trans
from time import sleep


class ThatCantBeRightException(Exception):
	pass

def tuple_add(tup1, tup2):
	return tup1[0] + tup2[0], tup1[1] + tup2[1]

os.chdir(os.path.dirname(__file__))
with open('./input.txt', 'r') as file:
	data = file.read().split('\n')
world = {(y,x): data[y][x] for y in range(len(data)) for x in range(len(data[0]))}
translations_clock = [(-1, 0), (0, 1), (1, 0), (0, -1)]
OBSTACLE_CHAR = '#'
visited_char = 'X'
guard_pos = None
#guard_pos = (77, 59) # y x
if not guard_pos:
	for index, line in enumerate(data):
		try:
			guard_pos = index, line.index('^')
			break
		except ValueError:
			continue
if not guard_pos: raise Exception()
world[guard_pos] = '.'
GUARD_START_POS = guard_pos
_start_ = True
path_taken = []
infinite_loops = 0
itercount = 0
SPEED = .0
open('output_visualization.txt', 'w').close()
original_data = [[char for char in line] for line in data]
MAX_STREAK = 7
while True:
	guard_pos = GUARD_START_POS
	new_world = copy.deepcopy(world)
	facing_index = 0
	if not _start_:
		path_taken = list(set(path_taken))
		itercount += 1
		if itercount > len(path_taken) - 1: break
		#print(f'{itercount} out of {len(path_taken)} starts attempted')
		new_world[path_taken[itercount]] = OBSTACLE_CHAR
	visited = set()

	while True:
		if _start_: path_taken.append(guard_pos)
		next_step = tuple_add(guard_pos, translations_clock[facing_index])
		in_front = new_world.get(next_step, -1)
		if in_front != '.':
			if in_front == -1:
				_start_ = False
				break
			if in_front not in OBSTACLE_CHAR: raise ThatCantBeRightException('That ain\'t right man.', in_front)
			#aaa
			_obj = (guard_pos, translations_clock[facing_index])
			if _obj in visited:
				infinite_loops += 1
				break
			visited.add(_obj)
			facing_index = facing_index + 1 if facing_index + 1 < len(translations_clock) else 0
			continue
		guard_pos =  next_step
print(infinite_loops)
# 5403
# 5404!!!!

# 1984 !!! bruteforce; took like 4 minutes