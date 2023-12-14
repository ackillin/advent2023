import re
from pprint import pprint
import numpy as np

board = [[]]
[board[-1].append(line.strip()) if line != '\n' else board.append([]) for line in open('test2.txt').readlines()]
pprint(board)
board = np.array(board)
#pprint(board[0].T)
#pprint(board[0])
def find_row(sets):
    print('start set')
    values = set()
    col_board = []
    for line in sets:
        most_likely = {}
        total = len(line)
        for x in range(2,total):
            #Checking if its a mirror at any point
            for t in range(total-x):
                compare = line[t+x:t+x+x]
                compare = compare[::-1]
                #print(x,compare)
                if line[t:t+x] == compare:
                    most_likely[t+x] = most_likely[t+x]+1 if most_likely.get(t+x) else 1
        col_board.append(most_likely)
        values.add(max(most_likely, key=most_likely.get))
    print(values)
    pprint(col_board)
    if len(values) == 1:
        return list(values)[0]
    rev = col_board[::-1]
    pprint(rev)
    start = -1
    for counter, col in enumerate(col_board):
        if col == rev[counter]:
            print('hit')
            start = counter
        else:
            start = -1
    print(start)
    return start + 1


print([find_row(sets) for sets in board[:]])

#print([find_row(sets.T) for sets in board[:]])
