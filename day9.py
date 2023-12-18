import re
from pprint import pprint


def other_method(listy):
    diffs = [b-a for a,b in zip(listy, listy[1:])]
    return listy[-1] + other_method(diffs) if listy else 0


def get_root(listy):
    roots = []
    for x in range(len(listy)-1):
        diff = listy[x+1] - listy[x]
        roots.append(diff)
    if sum(roots) == 0 or roots == []:
        return [roots]
    else:
        return [roots] + get_root(roots)

diff = 0
[for line in roots.reverse()]
def extrapolate(last_num, roots):
    roots.reverse()
    diff = 0
    for line in roots:
        diff += line[-1]
    return last_num + diff


nums = [ list(map(int,re.findall('-?\d+',line))) for line in open('txt9.txt') ]

for dir in 1,-1:
    listy = []
    for num in nums:
        num = num[::dir]
        roto = get_root(num)
        listy.append(extrapolate(num[-1], roto))
    print(f'part {dir}:', sum(listy))
