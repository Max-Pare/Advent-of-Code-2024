import math

grid_raw = '............\n' \
           '........0...\n' \
           '.....0......\n' \
           '.......0....\n' \
           '....0.......\n' \
           '......A.....\n' \
           '............\n' \
           '............\n' \
           '........A...\n' \
           '.........A..\n' \
           '............\n' \
           '............'.split('\n')
MAX_X, MAX_Y = len(grid_raw[0]) - 1, len(grid_raw) - 1
grid_d = {(x, y): grid_raw[y][x] for y in range(len(grid_raw)) for x in range(len(grid_raw[0]))}


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
	def normalize(v):
		if v[0] == v[1]: return 1, 1
		if v[0] < v[1]: return 1, v[1] - (v[0] - 1)
		if v[1] < v[0]: return  v[0] - (v[1] - 1), 1
		return None

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
	def in_bounds(v, max_x, max_y):
		return not(v[0] > max_x or v[0] < 0)
	@staticmethod
	def points_on_line(v1:tuple[int,int], v2:tuple[int,int], max_x=MAX_X, max_y=MAX_Y):
		points = set()
		_offset = Vector2.normalize(Vector2.abs(Vector2.sub(v1,v2)))
		points.add(v1)
		_current_pos = v1
		flip = False
		while True:
			points.add(_current_pos)
			_current_pos = Vector2.add(_current_pos, _offset)
			if (_current_pos[0] > max_x or _current_pos[0] < 0) or (_current_pos[1] > max_y or _current_pos[1] < 0):
				if flip: break
				_current_pos = v1
				_offset = Vector2.negate(_offset)
				flip = True
		return list(points)

	@staticmethod
	def find_antinodes(v1:tuple[int,int], v2:tuple[int,int], max_x=MAX_X, max_y=MAX_Y):
		_offset = Vector2.normalize(Vector2.abs(Vector2.sub(v1,v2)))
		points = [Vector2.add(v1, _offset), Vector2.add(v1, Vector2.negate(_offset)),
		          Vector2.add(v2, _offset), Vector2.add(v2, Vector2.negate(_offset))]
		return [p for p in points if p and all(not c_ < 0 for c_ in p) and p != v1 and p != v2]

	@staticmethod
	def direction(v1, v2):
		return Vector2.add(v1, v2)

antinodes = []
for point0, char0 in grid_d.items():
	for point1, char1 in grid_d.items():
		if (point0 == point1) or (char0 == '.' or char1 == '.') or (char0 != char1): continue
		antinodes += Vector2.find_antinodes(point0, point1)

antinodes = set(antinodes)
print(antinodes)
print(len(antinodes))
'''_visual = [grid_d[y][x] for y in range(len(grid_raw)) for x in range(len(grid_raw[0]))]
for antinode in antinodes:
	_visual[][]'''