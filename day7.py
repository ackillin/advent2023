import re
from pprint import pprint
import sys
sys.setrecursionlimit(5000)

conv = {'A':14,'K':13,'Q':12,'J':11,'T':10}
def get_score(hand):
    #Get
    lol = {}
    for x in hand:
        if lol.get(x):
            lol[x]+=1
        else:
            lol[x]=1
    high_card = max(lol.values())
    value_to_add = conv[hand[0]] if hand[0].isdigit() == False else int(hand[0])
    m = 0
    # Sets a score for each card
    for i in list(lol.values()):
        if i != 0 and i != high_card:
            value_to_add -= 20
    return high_card * 200 + value_to_add


def get_score_part2(hand):
    conv = {'A':14,'K':13,'Q':12,'J':1,'T':10}
    lol = {}
    for x in hand:
        if lol.get(x):
            lol[x]+=1
        else:
            lol[x] = 1
    num_to_add = 0
    if lol.get('J'):
        num_to_add = lol['J']
        for x in lol.keys():
            lol[x] +=num_to_add
        lol['J'] -= num_to_add
    high_card = max(lol.values())
    value_to_add  = conv[hand[0]] if hand[0].isdigit() == False else int(hand[0])

    for i in list(lol.values()):
        if i != num_to_add and i != high_card:
            value_to_add -=20
    return high_card * 200 + value_to_add

#{Hand: (Bet, Score)}
dicty = {}
with open('txt7.txt') as file:
    for line in file:
        line = line.strip().split(' ')
        score = get_score_part2(line[0])
        dicty[line[0]] = (line[1], score)
#pprint(dicty)

def convert(a):
    return int(a) if a.isdigit() else conv[a]


def compare_two(hand1, hand2) -> bool:
    #Returns a boolean value, true if hand 1 is bigger
    for x,i in zip(hand1,hand2):
        if x == i:
            continue
        x = convert(x)
        i = convert(i)
        return x > i



def confirm_sorted(listy):
    get_hand = lambda a: list(a.keys())[0]
    for counter, hand_bet_score in enumerate(listy):
        if counter == len(listy)-1:
            break
        if list(hand_bet_score.values())[0][1] < list(listy[counter+1].values())[0][1]:
            pass
        elif compare_two(get_hand(listy[counter]), get_hand(listy[counter+1])):
            listy[counter], listy[counter+1] = listy[counter+1], listy[counter]
            listy = confirm_sorted(listy)
    return listy


listy = [{'23456': ('10', 202)}]
for hand, bet_score in dicty.items():
    #Find index
    for counter, value in enumerate(listy):
        this_hand_value = list(value.values())[0][1]
        if bet_score[1] > this_hand_value:
            listy.insert(counter, {hand:bet_score})
            break

        elif bet_score[1] == this_hand_value:
            if compare_two(hand, list(value.keys())[0]):
                listy.insert(counter, {hand:bet_score})
                break
            else:
                listy.insert(counter+1, {hand:bet_score})
                break

listy.pop(-1)
listy.reverse()
listy = confirm_sorted(listy)  # This takes a really really long time
total = 0
for counter, hand_bet_score in enumerate(listy):
    value = int(list(hand_bet_score.values())[0][0])
    #print(value, (counter+1) * value)
    total += (counter+1) * value

print(total)
