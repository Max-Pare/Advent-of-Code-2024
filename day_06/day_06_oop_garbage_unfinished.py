import os

os.chdir(os.path.dirname(__file__))
with open('./input.txt', 'r') as file:
	data = file.read().split('\n')
GUARD_POS_CACHE = './cache.txt'
GUARD_SYMBOL = '^><v'
def find_guard(_d): # if input is changed the cache will be outdated until it is deleted manually, too fucking bad man
	if os.path.isfile(GUARD_POS_CACHE):
		with open(GUARD_POS_CACHE, 'r') as file:
			_c = file.read()
			if _c:
				if len(_temp := _c.split(',')) == 2:
					print('Loading guard position from cache.')
					return tuple([int(_t) for _t in _temp])
	for index, line in enumerate(_d):
		for char in line:
			if char in GUARD_SYMBOL:
				_pos = line.index(char), index
				with open(GUARD_POS_CACHE, 'w') as file:
					file.write(','.join(_pos))
				print('Guard position cached.')
				return int(_pos[0]), int(_pos[1])
	raise Exception('No guard found!')

def tuple_add(tup1, tup2):
	return tup1[0] + tup2[0], tup1[1] + tup2[1]

class Guard:
	def __init__(self, pos, state):
		self.GUARD_DIRECTIONS = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
		self.state = state
		self.pos = int(pos[0]), int(pos[1])

	def forward(self):
		self.pos = tuple_add(self.pos, self.GUARD_DIRECTIONS[self.state])

	def in_front(self):
		return self.GUARD_DIRECTIONS[self.state]

	def rotate(self):
		_temp = self.state
		self.state = self.GUARD_DIRECTIONS.keys()[list(self.GUARD_DIRECTIONS.keys()).index(self.state) + 1]
		print(f'Rotated "{_temp}" ----> "{self.state}"')

class World:
	def __init__(self, grid : list[str]):
		self._grid = grid
		self.max_x, self.max_y = len(self._grid[0]), len(self._grid)

	def _out_of_bounds(self, pos:tuple[int]):
		return pos[0] > self.max_x or pos[1] > self.max_y

	def get(self, pos:tuple[int]):
		if self._out_of_bounds(pos): return None
		return self._grid[pos[1]][pos[0]]

	def set(self, pos:tuple, char):
		if self._out_of_bounds(pos): raise IndexError('Tried to set OOB index to grid.')
		if _cur := self._grid[pos[1]][pos[0]] == char:
			return True
		self._grid[pos[1]][pos[0]] = char
		return False

OBSTACLES = '#'
GROUND = '.'
VISITED = 'X'
world = World(data)
_guard_pos = find_guard(data)
guard_state = world.get(_guard_pos)
guard = Guard(pos=_guard_pos, state=guard_state)
while True:
	while world.get(guard.in_front()) in OBSTACLES:
		guard.rotate()
	world.set(guard.pos, VISITED)
	guard.forward()
	break
#18:01 06/12/24: I need to stop this now, this is really terrible, why did I choose oop for this    