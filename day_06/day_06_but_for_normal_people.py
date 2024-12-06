import copy
import os
from time import sleep


class ThatCantBeRightException(Exception):
	pass

def tuple_add(tup1, tup2):
	return tup1[0] + tup2[0], tup1[1] + tup2[1]

os.chdir(os.path.dirname(__file__))
with open('./testinput.txt', 'r') as file:
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
WORLD_DEFAULT = copy.deepcopy(world)
_start_ = True
path_taken = []
infinite_loops = 0
itercount = 0
SPEED = .0
open('output_visualization.txt', 'w').close()
original_data = [[char for char in line] for line in data]
MAX_STREAK = 7
while True:
	print()
	guard_pos = GUARD_START_POS
	world = copy.deepcopy(WORLD_DEFAULT)
	facing_index = 0
	obstacles_hit = dict()
	obstacle_history = []
	#_visual_world = copy.deepcopy(original_data)
	obstacle_snapshot = []
	re_hit_streak = 0
	path_taken = list(set(path_taken))
	if not _start_:
		itercount += 1
		if itercount > len(path_taken) - 1: break
		print(f'{itercount} out of {len(path_taken)} paths attempted')
		world[path_taken[itercount]] = OBSTACLE_CHAR
		#_visual_world[path_taken[itercount][0]][path_taken[itercount][1]] = OBSTACLE_CHAR[1]
	while True:
		if _start_: path_taken.append(guard_pos)
		if itercount == 40 and True is False:
			with open('output_visualization.txt', 'w') as file:
				_visual_world = original_data
				for key, value in world.items():
					original_data[key[0]][key[1]] = value
				original_data[guard_pos[0]][guard_pos[1]] = '^'
				file.write('\n'.join([''.join(line) for line in _visual_world]) + '\n\n')
				exit()
		next_step = tuple_add(guard_pos, translations_clock[facing_index])
		in_front = world.get(next_step, -1)
		if in_front != '.':
			if in_front == -1:
				_start_ = False
				break
			if in_front not in OBSTACLE_CHAR: raise ThatCantBeRightException('That ain\'t right man.', in_front)
			facing_index = facing_index + 1 if facing_index + 1 < len(translations_clock) else 0
			if next_step in obstacle_history:
				#print('+1 streak')
				re_hit_streak += 1
			else:
				re_hit_streak = 0
			if re_hit_streak >= MAX_STREAK:
				print('- - - - - INFINITE LOOP DETECTED - - - - -')
				infinite_loops += 1
				break
				with open('output_visualization.txt', 'a') as file:
					_visual_world = original_data
					for key, value in world.items():
						original_data[key[0]][key[1]] = value
					original_data[GUARD_START_POS[0]][GUARD_START_POS[1]] = '^'
					original_data[path_taken[itercount][0]][path_taken[itercount][1]] = '0'
					file.write('\n'.join([''.join(line) for line in _visual_world]) + '\n\n')
				break
			obstacle_history.append(next_step)
			if len(obstacle_history) > MAX_STREAK: obstacle_history.pop(0)
			continue
		guard_pos =  next_step
print(infinite_loops)
# 5403
# 5404!!!!