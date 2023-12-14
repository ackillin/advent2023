import re

def get_input(file_name):
    with open(file_name,'r') as file:
        for line in file:
            yield line

def summary(data):
    total = 0
    red_limit = 12
    blue_limit = 14
    green_limit = 13
    pattern = '(\d* red)|(\d* blue)|(\d* green)'
    for line in data:
        #First half is game id, second is game
        line = line.split(':')
        for game in line[1].split(';'):
            red = re.sub('\D*', '', str(re.search(pattern,game).group(1)))
            blue = re.sub('\D*' , '', str(re.search(pattern,game).group(2)))
            green = re.sub('\D*', '', str(re.search(pattern,game).group(3)))
            print(game)
            print("red",red, "blue",blue,"green", green)
            if red != "":
                if int(red) > red_limit:
                    print("red broke")
                    break
            if blue != "":
                if int(blue) > blue_limit:
                    print('blue broke')
                    break
            if green != "":
                if int(green) > green_limit:
                    print('green broke')
                    break
        print('worked')
        total += int(re.sub('\D*','',line[0]))
    return total

def summary2(data):
    total = 0
    red_limit = 12
    blue_limit = 14
    green_limit = 13

    for line in data:
        broke = False
        line = line.split(':')
        for game in line[1].split(';'):
            for pull in game.split(','):
                number = int(re.sub('\D+','',pull))
                print(pull)
                if 'red' in pull:
                    if number > red_limit:
                        broke = True
                if 'blue' in pull:
                    if number > blue_limit:
                        broke = True
                if 'green' in pull:
                    if number > green_limit:
                        broke = True
        if broke == False:
            total+= int(re.sub('\D+','',line[0]))
    return total

def summary3(data):
    total = 0

    for line in data:
        red_max = 1
        blue_max = 1
        green_max = 1
        line = line.split(':')
        for game in line[1].split(';'):
            for pull in game.split(','):
                number = int(re.sub('\D+','',pull))
                if 'red' in pull:
                    if number > red_max:
                        red_max = number
                if 'blue' in pull:
                    if number > blue_max:
                        blue_max = number
                if 'green' in pull:
                    if number > green_max:
                        green_max = number
        total+= (red_max * blue_max * green_max)
    return total


if __name__ == '__main__':
    test = list(get_input('txt2.txt'))
    #print(summary(test))
    print(summary3(test))
