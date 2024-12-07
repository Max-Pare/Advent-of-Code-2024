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
OPS = ['*', '+', '||']

def try_int(string:str):
	try:
		int(string)
		return True
	except ValueError:
		return False

total_valid_regular = {}
total_valid_elephant = {}
print(f'Will process {len(_raw_data)} equations.')
for eq_ind, equation_raw in enumerate(_raw_data): # eval() fucking sucks, it interprets '121+27' as '121 * 2 + 7' f*ck you # EDIT: this is false
	target = equation_raw.split(':')[0]
	numbers = equation_raw.split(':')[1].split()
	combos = [item for item in itertools.product(OPS, repeat=len(numbers) - 1)]
	operations = []
	for combo in combos:
		cur = []
		for j, num in enumerate(numbers):
			cur.append(num)
			if j < len(combo): cur.append(combo[j])
		operations.append(cur)
	print(f'Starting equation {eq_ind} out of {len(_raw_data)}')
	for i, operation in enumerate(operations):
		#print(f'Done {i} out of {len(operations)} operations')
		done = False
		current = None
		total = 0
		op = None
		for val in operation[::]:
			if val in OPS:
				op = val
				continue
			if try_int(val):
				if not current:
					current = val
					continue
				if op:
					if op == '||':
						current = current + val
						op = None
						#print(operation)
					else:
						current = eval(current+op+val)
					current = str(current)
					op = None
			total = int(current)
		if total == int(target):
			if '|' in operation:
				total_valid_elephant[(hash(''.join([val for val in operation if try_int(val)])))] = total
			else:
				total_valid_regular[(hash(''.join([val for val in operation if try_int(val)])))] = total
print(sum([val for val in total_valid_regular.values()]) + sum([val for val in total_valid_elephant.values()]))

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