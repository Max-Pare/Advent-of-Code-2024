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
OBSTACLE_CHAR = '#0'
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
WORLD_DEFAULT = copy.copy(world)
_start_ = True
path_taken = []
infinite_loops = 0
itercount = 0
SPEED = .0
open('output_visualization.txt', 'w').close()
original_data = [[char for char in line] for line in data]
while True:
	print()
	guard_pos = GUARD_START_POS
	world = copy.deepcopy(WORLD_DEFAULT)
	facing_index = 0
	obstacles_hit = dict()
	obstacle_history = []
	_visual_world = copy.deepcopy(original_data)
	if not _start_:
		itercount += 1
		if itercount > len(path_taken) - 1: break
		print(f'{itercount} out of {len(path_taken)} paths attempted')
		sleep(SPEED)
		world[path_taken[itercount]] = OBSTACLE_CHAR[0]
		print(_visual_world)
		print(path_taken[itercount])
		_visual_world[path_taken[itercount][0]][path_taken[itercount][1]] = OBSTACLE_CHAR[1]
	while True:
		if _start_: path_taken.append(guard_pos)
		next_step = tuple_add(guard_pos, translations_clock[facing_index])
		in_front = world.get(next_step, -1)
		if in_front != '.':
			if in_front == -1:
				if not _start_: print('No infinite loop')
				_start_ = False
				break
			if in_front not in OBSTACLE_CHAR: raise ThatCantBeRightException('That ain\'t right man.', in_front)
			facing_index = facing_index + 1 if facing_index + 1 < len(translations_clock) else 0
			if not obstacles_hit.get(next_step, None):
				obstacles_hit[next_step] = 0
			obstacles_hit[next_step] += 1
			obstacle_history.append((next_step, obstacles_hit[next_step]))
			if len(obstacle_history) > 4: obstacle_history.pop(0)
			if all(_ob[1] >= 6 for _ob in obstacle_history):
				infinite_loops += 1
				print('INFINITE LOOP DETECTED!')
				with open('output_visualization.txt', 'a') as file:
					file.write('\n'.join([''.join(line) for line in _visual_world]) + '\n\n')
				break
			print(f'Obstacle {next_step} hit {obstacles_hit[next_step]} times')
			continue
		guard_pos =  next_step
		sleep(SPEED / 10)
print(infinite_loops)
# 5403
# 5404!!!!