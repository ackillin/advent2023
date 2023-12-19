import re
from pprint import pprint
import numpy as np

board = [[]]
[board[-1].append(line.strip()) if line != '\n' else board.append([]) for line in open('test2.txt').readlines()]


def find_col(col_board):
    rev = col_board[::-1]
    start = -1
    for counter, col in enumerate(col_board):
            if col == rev[counter]:
                start = counter + 1
    return start * 100


#This is my cooked answer
def find_row(sets, counter = 2):
    #print('start set')
    values = set()
    col_board = []
    #Checker
    for line in sets:
        most_likely = {}
        total = len(line)
        for x in range(1,total+1):
            #Checking if its a mirror at any point
            for t in range(total):
                compare = line[t+x:t+x+x]
                compare = compare[::-1]
                #print(x,compare)
                if line[t:t+x] == compare:
                    most_likely[t+x] = most_likely[t+x]+1 if most_likely.get(t+x) else 1
        col_board.append(most_likely)
        try:
            values.add(max(most_likely, key=most_likely.get))
        except:
            values.add(0)
    if len(values) == 1:
        return list(values)[0] if counter % 2 == 0 else list(values)[0] * 100
    if counter > 4:
        print('no match found')
        #pprint(sets)
        return -1_000_000
    return find_row([*zip(*sets)],counter+1)
    #Old code, found a better method
    rev = col_board[::-1]
    start = -1
    if len(sets) % 2 == 0:
        #Cut off the top so its now
        return max(find_col(col_board[0:]), find_col(col_board[:-1]))
    else:
        #Only works for odd # of lines
        return find_col(col_board)


def other_method2(sets):
    for i in range(len(sets)):
        for l,m in zip(sets[i-1::-1], sets[i:]):
            if sum(c != d for c, d in zip(l,m)) == 1:
                return i
        #if sum( u != d for l,m in zip(sets[i-1::-1], sets[i:]) for u,d in zip(l,m)) == 1:
        #    return i  # Match
    else:
        return 0  # Not a match


def other_method(sets):
    for i in range(len(sets)):
        if sum(c != d for l,m in zip(sets[i-1::-1], sets[i:]) for c,d in zip(l,m)) == 1:
            return i
    else: return 0

# Checks for columns then rows
print( sum(100 * other_method2(sets) + other_method2([*zip(*sets)])  for sets in board) )

#print(sum([find_row(sets) for sets in board[:]]))
#too high: 77048
#too low: 7466
