import copy

testinput = '190: 10 19\n'\
'3267: 81 40 27\n'\
'83: 17 5\n'\
'156: 15 6\n'\
'7290: 6 8 6 15\n'\
'161011: 16 10 13\n'\
'192: 17 8 14\n'\
'21037: 9 7 18 13\n'\
'292: 11 6 16 20'
import itertools
_raw_data = testinput.split('\n')
with open('./input.txt', 'r') as file:
	_raw_data = file.read().split('\n')
OPS = '*+'

def try_int(string:str):
	try:
		int(string)
		return True
	except ValueError:
		return False

total_valid = {}
for equation_raw in _raw_data[:]: # eval() fucking sucks, it interprets '121+27' as '121 * 2 + 7' fuck you, you fucking assholes
	target = equation_raw.split(':')[0]
	numbers = equation_raw.split(':')[1].split()
	combos = [item for item in itertools.product(OPS, repeat=len(numbers) - 1)]
	operations = []
	for combo in combos:
		cur = []
		for i, num in enumerate(numbers):
			cur.append(num)
			if i < len(combo): cur.append(combo[i])
		operations.append(cur)
	for operation in operations:
		done = False
		current = None
		total = 0
		op = None
		for val in operation[::]:
			if val in '-+=*/':
				op = val
				continue
			if try_int(val):
				if not current:
					current = val
					continue
				if op:
					current = eval(current+op+val)
					current = str(current)
					op = None
			total = int(current)

		if total == int(target):
			total_valid[(hash(''.join([val for val in operation if try_int(val)])))] = total
print(sum([val for val in total_valid.values()]))

'''
for equation_raw in _raw_data[1:2]: # eval() fucking sucks, it interprets '121+27' as '121 * 2 + 7' fuck you, you fucking assholes
	target = equation_raw.split(':')[0]
	numbers = equation_raw.split(':')[1].split()
	combos = [item for item in itertools.product(operators, repeat=len(numbers) - 1)]
	operations = []
	for combo in combos:
		current = []
		for i, num in enumerate(numbers):
			current.append(num)
			if i < len(combo): current.append(combo[i])
		operations.append(current)
	for operation in operations:
		print(operation)
		_t = ''.join(operation[:3])
		print(_t)
		current_total = eval(_t)
		for i in range(len(operation))[3::2]:
			to_eval = f'{current_total}{operation[i]}{operation[i + 1]}'
			print(to_eval)
			current_total += eval(to_eval)
			print(current_total)
'''