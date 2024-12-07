import itertools
import multiprocessing
from time import sleep
import random
from numpy import array_split

with open('./input.txt', 'r') as file:
	_raw_data = file.read().split('\n')
OPS = ['*', '+', '||']

def try_int(string:str):
	try:
		int(string)
		return True
	except ValueError:
		return False
NUM_THREADS = 12

def worker(data, _collector):
	print(f'Will process {len(data)} equations.')
	total_valid_regular = {}
	total_valid_elephant = {}
	max_counter = int(40000 + (5000 * (1 + random.random())))
	for eq_ind, equation_raw in enumerate(data):
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
		counter = 0
		for i, operation in enumerate(operations):
			counter += 1
			if counter > max_counter:
				counter = 0
				print(f'Processing operation {i} of {len(operations)}, equation {eq_ind} out of {len(data)}')
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
						else:
							current = eval(current + op + val)
						current = str(current)
						op = None
				total = int(current)
			if total == int(target):
				if '|' in operation:
					total_valid_elephant[(hash(''.join([val for val in operation if try_int(val)])))] = total
				else:
					total_valid_regular[(hash(''.join([val for val in operation if try_int(val)])))] = total
				break
	_collector.put(
		sum([val for val in total_valid_regular.values()]) + sum([val for val in total_valid_elephant.values()]))
	print('Done')
	exit(0)

def main(_raw_data_):
	_groups = array_split(_raw_data_, NUM_THREADS)
	collector = multiprocessing.Queue()
	procs = [multiprocessing.Process(target=worker, args=(group,collector)) for group in _groups]
	results = []
	for proc in procs:
		proc.start()
	for proc in procs:
		results.append(collector.get())
	for proc in procs:
		proc.join()
	while any(proc.is_alive() for proc in procs):
		sleep(.1)
	print(sum(results))

if __name__ == '__main__':
	main(_raw_data)