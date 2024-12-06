from math import floor

with open('./input.txt','r') as file:
    r_, u_ = file.read().split('\n\n')
    r_ = r_.split('\n')
    u_ = u_.split('\n')
    updates_unsorted = [u__.split(',') for u__ in u_]
    rules = {}
    for r__ in r_:
        r0,r1 = r__.split('|')
        if not rules.get(r0): rules[r0] = []
        rules[r0].append(r1)

updates_sorted = []
good_mid = 0
bad_mid = 0
MAX_ITERS = 32
for update in updates_unsorted[:]:
    last_iter_good = True
    iters = 0
    while iters < MAX_ITERS:
        print(f'ITER [{iters}]')
        print(update)
        current_update_good = True
        for i in range(len(update)):
            if i + 1 > len(update) - 1:
                continue
            pair = update[i], update[i + 1] # idea stolen from reddit because I have no idea how to solve this
            if r := rules.get(pair[0], None):
                if pair[1] in r:
                    print(f'{pair} is correct')
                    continue
            if r := rules.get(pair[1], None):
                if pair[0] in r:
                    print(f'{pair} needs to be swapped')
                    current_update_good = False
                    update[i], update[i + 1] = pair[1], pair[0]
                    continue
            print(f'No rules found for {pair}')
        print(update)
        middle = int(update[floor((len(update) - 1) / 2)]) # input updates will always be odd
        print(middle)
        print('_____________________________________________')
        if last_iter_good and current_update_good:
            good_mid += middle
            break
        if not last_iter_good and current_update_good:
            bad_mid += middle
            break
        print('_____________________________________________')
        last_iter_good = False
        iters += 1
# problem_solved = any(Good? No. Fast? No. Memory efficient? This is python (No). Edge case safe? No. Does it work. YES)
print(good_mid, bad_mid)