# password: 149387-20161210-e396e238
# coding:utf

    # 先计算x和y方向上的距离然后再算出总的，调用了确定方向的函数
def calcul_distance(path):
    direction = 0
    distance_x = distance_y = 0
    for i in range(0, len(path)):
        hint = path[i]
        direction = det_direction(hint, direction)
        if direction == 0:
            distance_y += int(hint[1:])
        elif direction == 1:
            distance_x += int(hint[1:])
        elif direction == 2:
            distance_y -= int(hint[1:])
        elif direction == 3:
            distance_x -= int(hint[1:])
        else:
            print 'Something wrong with the calcul_distance'
            return
            
    distance = abs(distance_x) + abs(distance_y)
    return distance

    # 记录路径进行比较
def find_location(path):
    direction = 0
    distance_x = distance_y = 0
    locations = [(0,0)]
    for i in range(0, len(path)):
        hint = path[i]
        direction = det_direction(hint, direction)
        if direction == 0:
            for i in range(1, int(hint[1:]) + 1):
                location = (distance_x, distance_y + i)
                if location in locations:
                    print location
                    return abs(distance_x) + abs(distance_y + i)
                else:
                    locations.append(location)
            distance_y += int(hint[1:])
        elif direction == 1:
            for i in range(1, int(hint[1:]) + 1):
                location = (distance_x + i, distance_y)
                if location in locations:
                    print location
                    return abs(distance_x + i) + abs(distance_y)
                else:
                    locations.append(location)
            distance_x += int(hint[1:])
        elif direction == 2:
            for i in range(1, int(hint[1:]) + 1):
                location = (distance_x, distance_y - i)
                if location in locations:
                    print location
                    return abs(distance_x) + abs(distance_y - i)
                else:
                    locations.append(location)
            distance_y -= int(hint[1:])
        elif direction == 3:
            for i in range(1, int(hint[1:]) + 1):
                location = (distance_x - i, distance_y)
                if location in locations:
                    print location
                    return abs(distance_x - i) + abs(distance_y)
                else:
                    locations.append(location)
            distance_x -= int(hint[1:])
        else:
            print 'Something wrong with the find_location'
            return    
    
    print 'Found no possible locations......'
    return 
    
    # 计算当前的方向，用0,1,2,3表示北，东，南，西，调用了turn_left和turn_right函数
def det_direction(hint, direction):
    if hint[:1] == 'L':
        direction = turn_left(direction)
    elif hint[:1] == 'R':
        direction = turn_right(direction)
    else:
        print 'Something wrong with the det_direction'
        return
    return direction
    
def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

def turn_right(direction):
    direction += 1
    if direction == 4:
        direction = 0
    return direction

    # 读取指示文件
def read_hint(filename):
    path = []
    try:
        for line in open(filename):
            hints = line.split(',')
        for i in range(0, len(hints)):
            hints[i] = hints[i].strip(' ')
        path = hints
        return path
    except:
        print 'Something wrong with the read_hint'
        return
        
if __name__ == '__main__':
    path = read_hint('puzzle1.txt')
# *************part1*******************
    # distance = calcul_distance(path)
    # print distance
#*************part2********************
    distance = find_location(path)
    print distance
    
    print '\n'
    print 'All done baby!'