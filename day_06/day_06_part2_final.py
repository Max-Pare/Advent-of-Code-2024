import copy
import os
import multiprocessing

from scipy.optimize import brute


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
start_pos = None
#guard_pos = (77, 59) # y x
if not start_pos:
	for index, line in enumerate(data):
		try:
			start_pos = index, line.index('^')
			break
		except ValueError:
			continue
if not start_pos: raise Exception()
world[start_pos] = '^'

def bruteforce():
	def single_iter(start, grid):
		facing_index = 0
		visited = set()
		guard_pos = start
		grid[start] = '.'
		while True:
			next_step = tuple_add(guard_pos, translations_clock[facing_index])
			in_front = grid.get(next_step, -1)
			if in_front == -1:
				return False
			if in_front in '.':
				guard_pos = next_step
				continue
			assert in_front == '#'
			pos_object = (guard_pos, translations_clock[facing_index])
			if pos_object in visited:
				return True
			visited.add(pos_object)
			facing_index = facing_index + 1 if facing_index + 1 < len(translations_clock) else 0

	print('Finding all starting points...')
	to_bruteforce = [item for item in world.keys() if world[item] == '.']
	total = 0
	print('Bruteforcing...')
	for point in to_bruteforce:
		_new_world = copy.deepcopy(world)
		_new_world[point] = '#'
		total += single_iter(start_pos, _new_world)
	print(total)
bruteforce()