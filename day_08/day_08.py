import math

with open('input.txt','r') as file:
	grid_raw = file.read().split('\n')
MAX_X, MAX_Y = len(grid_raw[0]) - 1, len(grid_raw) - 1
grid_d = {(x, y): grid_raw[y][x] for y in range(len(grid_raw)) for x in range(len(grid_raw[0]))}

def get_sign(val):
	return 1 if val == abs(val) else - 1

class Vector2:

	@staticmethod
	def negate(v):
		return v[0] * - 1, v[1] * -1

	@staticmethod
	def add(v1:tuple[int,int], v2:tuple[int,int]):
		return v1[0] + v2[0], v1[1] + v2[1]

	@staticmethod
	def mult(v1:tuple[int,int], v2:tuple[int,int]):
		return v1[0] * v2[0], v1[0] * v2[1]

	@staticmethod
	def div(v1:tuple[int,int], v2:tuple[int,int]):
		return int(v1[0] / v2[0]), int(v1[0] / v2[1])

	@staticmethod
	def sub(v1:tuple[int,int], v2:tuple[int,int]):
		return v1[0] - v2[0], v1[1] - v2[1]

	@staticmethod
	def flip_sign(v1):
		return v1[0] * (get_sign(v1[0]) * -1), v1[1] * (get_sign(v1[1]) * -1)

	@staticmethod
	def distance(v1:tuple[int,int], v2:tuple[int,int]):
		x1, y1 = v1
		x2, y2 = v2
		dx = x2 - x1
		dy = y2 - y1
		distance = math.sqrt(dx * dx + dy * dy)
		return int(distance)

	@staticmethod
	def abs(v):
		return abs(v[0]), abs(v[1])

	@staticmethod
	def in_bounds(v, max_x=MAX_X, max_y=MAX_Y):
		return not(v[0] > max_x or v[0] < 0 or v[1] < 0 or v[1] > max_y)

	@staticmethod
	def put_antinodes(v1:tuple[int,int], v2:tuple[int,int], max_x=MAX_X, max_y=MAX_Y, infinite=False):
		start_offset = Vector2.sub(v1,v2)
		_offset = start_offset
		if infinite and _offset[0] == _offset[1]: _offset = (1,1)
		results = []
		counter = 0
		while True:
			_current = [Vector2.add(v1, _offset), Vector2.add(v1, Vector2.negate(_offset)),
			          Vector2.add(v2, _offset), Vector2.add(v2, Vector2.negate(_offset))]
			if all(not Vector2.in_bounds(_elem) for _elem in _current): break # probably makes infinite loop in some cases, too bad!
			results += _current
			if not infinite: break
			_offset = Vector2.add(_offset, start_offset)
		return [p for p in set(results)
		        if p and Vector2.in_bounds(p, max_x,max_y)
		        and (p != v1 or infinite)
		        and (p != v2 or  infinite)]

	@staticmethod
	def direction(v1, v2):
		return Vector2.add(v1, v2)


antinodes = []
antennas = set()
for p0, char0 in grid_d.items():
	if char0 == '.':
		continue
	for p1, char1 in grid_d.items():
		if (p0 == p1) or (char1 in '.#') or (char0 != char1): continue
		antennas.add(p0)
		antennas.add(p1)
		a_nodes = Vector2.put_antinodes(p0, p1, infinite=True)
		antinodes += a_nodes


antinodes = set(antinodes)
print(len(antinodes), 'antinodes')
_visual = [[grid_raw[y][x] for x in range(len(grid_raw[0]))] for y in range(len(grid_raw))]
for x,y in antinodes:
	_visual[y][x] = '#'
with open('./visual.txt','w') as file:
	file.write(''.join('\n'.join([' '.join(row) for row in _visual])))