# coding:utf 
# import time
import itertools
import os
import numpy

def read_input(filename):
    map = []
    for line in open(filename):
        new = []
        line = line.strip('\n')
        for one in line:
            new.append(one)
        map.append(new)
    return map
    
def find_position(map):
    postions_to_find = {}
    for row in range(0, len(map)):
        for column in range(0, len(map[row])):
            if is_nb(map[row][column]):
                postions_to_find[int(map[row][column])] = (row, column)
            else:
                pass
    return postions_to_find

def is_nb(string):
    try:
        int(string)
        return True
    except:
        return False

    #用map_list 生成一个包含各个点之间距离的list，注意不能过去的#就用99999代替即可
def make_list_dijkstra(map):
    map_distance = []
    nb_row = len(map)
    nb_column = len(map[1])
    new_dimension = nb_row * nb_column
    for k in range(0, new_dimension):
        row = []
        for i in range(0, nb_row):
            for j in range(0, nb_column):
                index = i * nb_column + j
                if k == index:
                    row.append(0)
                else:
                    if up_down_left_right(k, nb_column, i, j):
                        if map[i][j] != '#':
                            row.append(1)
                        else:
                            row.append(99999)
                    else:
                        row.append(99999)
        map_distance.append(row)
    print 'list of distance ready'
    return map_distance
    
    # 确定上下左右是 . 还是 #      
def up_down_left_right(k, nb_column, i, j):            
    row = k // nb_column
    column = k % nb_column
    if i == row - 1 and j == column:
        return True
    elif i == row + 1 and j == column:
        return True
    elif i == row and j == column - 1:
        return True
    elif i == row and j == column + 1:
        return True
    else:
        return False
 
 # dijkstra的主要算法，relax即使松弛法，一直要到出发点每个column都松弛
 # 注意这里我们可以使用这个算法因为没有负方向的距离，所有距离都是正的
 #另外，如果第一部分要用广度优先算法要算死掉，很可能最后就内存不足死机了。。。
def search_path_dijkstra(map, depart, destination):
    distance = map[depart]
    distance_dic = {}
    for i in range(0, len(distance)):
        if distance[i] != 0:
            distance_dic[i] = distance[i]
            
    while(len(distance_dic) > 0):
        # print len(distance_dic) 
        possible_relax = distance_dic.values()
        possible_relax.sort()
        relax_value = possible_relax[0]
        for key, value in distance_dic.items():
            if value == relax_value:
                relax_key = key
                del distance_dic[key]
                break
        # print relax_key
        for i in range(0, len(map[relax_key])):
            if i == depart:
                continue
            else:
                if map[relax_key][i] + relax_value < map[depart][i]:
                    map[depart][i] = map[relax_key][i] + relax_value
                    distance_dic[i] = map[relax_key][i] + relax_value
                    # print i, list[relax_key][i] + relax_value
                    # raw_input()
    
    # print '*****************************'
    return map[depart][destination]     

    # 得到0到7一共8个地点两两之间的最短距离然后进行计算，这里因为出发点定了，所以只要C72 = 21次计算即可
def get_distance_every_two(targets, map, map_distance):
    if os.path.isfile('dis_distance.txt'):
        return load_file('dis_distance.txt')
    else:
        dic_distance = {}
        print 'Begin the process to get every two position distance...'
        for index1 in targets.keys():
            for index2 in targets.keys():
                key = (index1, index2) # 注意dic中的key不能是list格式，所以需要一个tuple和list的转换
                if index1 == index2:
                    dic_distance[key] = 0
                else:
                    list_key = list(key)
                    list_key.sort()
                    key = tuple(list_key)
                    if key in dic_distance:
                        continue
                    else:
                        target1 = targets[index1][0] * len(map[1]) + targets[index1][1]
                        target2 = targets[index2][0] * len(map[1]) + targets[index2][1]        
                        steps = search_path_dijkstra(map_distance, target1, target2)
                        dic_distance[key] = steps
                print 'Position No.%d and No.%d is ok' %(index1, index2)
        print 'Already got every two position distance'
        save_file('dis_distance.txt', dic_distance)
        # print dic_distance
        return dic_distance

    # 将两两之间的距离再放到一个8*8的矩阵中
def make_targets_map(dic, targets):
    print 'Begin to make a map of distance bewteen every two targets...'
    dim = len(targets)
    targets_map = [[0 for col in range(dim)] for row in range(dim)]
    for i in range(dim):
        for j in range(dim):
            index = [i, j]
            index.sort()
            index = tuple(index)
            for key in dic.keys():
                if key == index:
                    targets_map[i][j] = dic[key]
    print numpy.array(targets_map)
    return targets_map
    
    # 遍历每个可能的组合然后用一个dic保存最短的路径
def search_shortest_path(targets_map):
    print 'Begin to search for the shortest path'
    shortest = {}
    all_path = list(itertools.permutations([1,2,3,4,5,6,7], 7)) # 这个可以得到有序的排列，也就是一个有5040个tuple的list，强大！！
    count = 0
    for path in all_path:
        count += 1
        print count
        distance = 0
        path_list = list(path)
        path_list.insert(0, 0)
        path_list.append(0) # part2
        for index in range(1, len(path_list)):
            distance += targets_map[path_list[index - 1]][path_list[index]]
        if len(shortest) == 0:
            shortest[path] = distance
        else:
            for value in shortest.values():
                if value < distance:
                    break
                elif value == distance:
                    shortest[path] = distance
                    break
                else:
                    shortest.clear()
                    shortest[path] = distance
                    break
    return shortest
        
# 可以用pypy先快速得到一个结果save起来，然后再用python作为解释器来load这个结果
def save_file(filename, content):
    target = open(filename, 'w')
    target.write(str(content))
    target.close()
    
def load_file(filename):
    target = open(filename, 'r')
    content = target.readline()
    return eval(content) # 碉堡了，用eval直接返回一个去掉string的对象！！
    
if __name__ == '__main__':
    #***********part1*************
    map = read_input('input.txt')
    targets = find_position(map)
    # print targets
    map_distance = make_list_dijkstra(map)
    dic_distance = get_distance_every_two(targets, map, map_distance)
    # print dic_distance
    targets_map = make_targets_map(dic_distance, targets)
    path = search_shortest_path(targets_map)
    print '***********************'
    for key in path.keys():
        print 'one path is:', key
        print 'it took %d steps' %path[key]
        print '\n'
    # print shortest_path(dic_order, list_order, map, map_distance)
    # start = int(round(time.time()))
    # print search_path_dijkstra(map_distance, target1, target2)
    # end = int(round(time.time()))
    # print 'It took', end - start, ' s to finish one search'
    # about 45 seconds for one search pour python, 
    #***********part2*************
    
    print '\n'
    print 'All done baby !!'