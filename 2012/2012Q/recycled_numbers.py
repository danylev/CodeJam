import sys
from collections import deque

from shared.stdread import read_input

def same_number(x,y):
    quu = deque(str(x))
    checked = str(y)
    for step in range(len(quu)):
        if ''.join(quu) == checked:
            return True
        else:
            temp = quu.pop()
            quu.appendleft(temp)
    return False

def pair_generator(x,y):
    for upper_bound in range(x,y+1):
        for lower_bound in range(x,upper_bound):
            yield lower_bound,upper_bound

if __name__ == '__main__':
    meta = read_input(sys.stdin)
    for i,line in enumerate(meta[1]):
        x,y = line.replace('\n','').split()
        counter = 0
        for pair in pair_generator(int(x), int(y)):
            if same_number(pair[0],pair[1]):
                counter += 1
        print(f'Case #{i+1}: ' + str(counter), end='\n')

