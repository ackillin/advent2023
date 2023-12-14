#Go back and finish
import re
import numpy as np
import itertools

board = [line.strip() for line in open('test.txt').readlines()]
stars = []
[ [stars.append((row,x.span()[0])) for x in re.finditer('#',line)] for row, line in enumerate(board)]

x_cord, y_cord = zip(*[(x,y) for x, line in enumerate(open('test.txt'))
                  for y, c in enumerate(line) if c == '#'])


new_board = np.array([list(x) for x in board])
columns = [counter for counter, col in enumerate(new_board.T) if not re.search('#',str(col))]
rows = [count for count,x in enumerate(new_board) if not re.search('#',str(x))]

mars = [(x,y_cord[counter]) for counter, x in enumerate(x_cord)]
print(mars == stars)
# Change this for the different parts
num_to_add = 1
#num_to_add = 1_000_000

for col in columns:
    for counter, star in enumerate(stars):
        if star[1] > col:
            stars[counter] = (star[0], star[1] + num_to_add)
for row in rows:
    for counter, star in enumerate(stars):
        if star[0] > row:
            stars[counter] = (star[0] + num_to_add, star[1])

def distance(stars, *swags):
    dist = []
    print(len(stars))
    for star, star2 in itertools.combinations(stars,2):
        dist.append(abs(star2[0] - star[0]) + abs(star2[1] - star[1]))
    return dist


def diff_approach(listy):
    # This is the stolen approach
    total = 0
    for x in listy:
        for x in range(x):
            total += (2,1)[x in listy]  # True or false, equivalent to 2 if true 1 if false
    return sum(abs(a-b) for a in listy for b in listy)
    listy = [sum( (2,1) [x in listy] for x in range(x) ) for x in listy]
    return sum(abs(a-b) for a in listy for b in listy) // 2


print(diff_approach(x_cord))
print(diff_approach(y_cord))
print(sum([diff_approach(x_cord),diff_approach(y_cord)]))
res = distance(stars)
print(len(res))
print(sum(res))
