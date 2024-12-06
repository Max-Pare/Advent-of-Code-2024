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
obstacle_char = '#'
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
while True:
	guard_pos = GUARD_START_POS
	world = copy.copy(WORLD_DEFAULT)
	facing_index = 0
	obstacles_hit = dict()
	last_obstacles = []
	if not _start_:
		itercount += 1
		if itercount > len(path_taken) - 1: break
		print(f'Starting iteration {itercount}')
		sleep(.2)
		world[path_taken[itercount]] = obstacle_char
	repeated_hits = 0
	while True:
		if _start_: path_taken.append(guard_pos)
		next_step = tuple_add(guard_pos, translations_clock[facing_index])
		in_front = world.get(next_step, -1)
		if in_front != '.':
			if in_front == -1:
				_start_ = False
				break
			if in_front != obstacle_char: raise ThatCantBeRightException('That ain\'t right man.', in_front)
			facing_index = facing_index + 1 if facing_index + 1 < len(translations_clock) else 0
			if not obstacles_hit.get(next_step, None):
				obstacles_hit[next_step] = 0
			obstacles_hit[next_step] += 1
			if next_step in last_obstacles:
				repeated_hits += 1
			else:
				repeated_hits = repeated_hits - 1 if repeated_hits - 1 >= 0 else 0
			print(repeated_hits)
			if repeated_hits > 5:
				infinite_loops += 1
				print(f'INFINITE LOOP DETECTED! ({infinite_loops})')
				break
			last_obstacles.append(next_step)
			if len(last_obstacles) > 4: last_obstacles.pop(0)
			print(f'Obstacle {next_step} hit {obstacles_hit[next_step]} times')
			continue
		guard_pos =  next_step
		sleep(.2)
print(infinite_loops)
# 5403
# 5404!!!!