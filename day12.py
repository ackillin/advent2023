import re
import itertools

board, nums = zip(*[line.strip().split() for line in open('test2.txt').readlines()])
#print(board)
nums = [list(map(int,num.split(','))) for num in nums]
#print(nums)

# Idea(?): Store all possible good / bad in list.
def get_perms(line, nums):
    conf_good = [x.span()[0] for x in re.finditer('\.',line)]
    conf_bad = [x.span()[0] for x in re.finditer('#', line)]
    mystery = [x.span()[0] for x in re.finditer('\?',line)]
    print(conf_good, conf_bad,mystery)
    possible = 
    perms = 0
    for num in nums:
        

print(get_perms(board[0],nums[0]))
