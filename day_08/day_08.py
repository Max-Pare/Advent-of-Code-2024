import math

testdata = '............'\
'........0...'\
'.....0......'\
'.......0....'\
'....0.......'\
'......A.....'\
'............'\
'............'\
'........A...'\
'.........A..'\
'............'\
'............'.split('\n')
MAX_X, MAX_Y = len(testdata[0]), len(testdata)
testdata = {(x,y):testdata[y][x] for y in range(len(testdata)) for x in range(len(testdata[0]))}

class Vector2:
	def __init__(self, vec:tuple[int,int]): #(x,y)
		if len(vec) != 2 or any(type(_v) != int for _v in vec): raise ValueError('Vector requires tuple(int,int) values')
		self._vec = vec

	@property
	def vec(self):
		return self._vec

	def __getitem__(self, item):
		return self._vec[item]

	@staticmethod
	def negate(v):
		return Vector2((v[0] * - 1, v[1] * -1))

	@staticmethod
	def add(v1,v2):
		return Vector2((v1[0] + v2[0], v1[0] + v2[1]))

	@staticmethod
	def mult(v1,v2):
		return Vector2((v1[0] * v2[0], v1[0] * v2[1]))

	@staticmethod
	def div(v1,v2):
		return Vector2((int(v1[0] / v2[0]), int(v1[0] / v2[1])))

	@staticmethod
	def sub(v1,v2):
		return Vector2((v1[0] - v2[0], v1[1] - v2[1]))

	@staticmethod
	def distance(v1,v2):
		x1, y1 = v1
		x2, y2 = v2
		dx = x2 - x1
		dy = y2 - y1
		distance = math.sqrt(dx * dx + dy * dy)
		return int(distance)

	@staticmethod
	def points_on_line(v1, v2, max_x=MAX_X, max_y=MAX_Y):
		points = set()
		_offset = Vector2.sub(v1, v2)
		_current_pos = v1
		points.add(v1)
		_direction = True
		while True:
			print(_offset)
			print(_current_pos)
			print(_direction)
			if _current_pos[0] > max_x or _current_pos[1] > max_y:
				if not _direction: break
				_direction = False
				_current_pos = v1
			_current_pos = Vector2.add(_current_pos, Vector2.mult(_offset, (_direction, _direction)))
			points.add(_current_pos)
		return points

	@staticmethod
	def direction(v1,v2):
		return Vector2.add(v1,v2)

	def __repr__(self):
		return str(self.vec)

print(Vector2.points_on_line((2,1),(5,4)))