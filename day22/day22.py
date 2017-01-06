#coding: utf
import numpy, copy

def read_file(filename):
    index = 0
    infos_list = []
    infos_dic = {}
    for line in open(filename, 'r'):
        index += 1
        if index >= 3:
            line = line.strip('\n')
            infos = line.split(' ')
            while('' in infos):
                infos.remove('')
            infos_list.append(infos)
        else:
            pass
    for info in infos_list:
        for i in range(1, 4):
            if 'T' in info[i]:
                info[i] = info[i].strip('T')
                # print info[i]
                info[i] = int(info[i])
            else:
                print 'unit is not T'
                raw_input()
                
        infos_dic[info[0]] = [info[1], info[2], info[3], info[4]] 
    return infos_dic
    
def find_pair_nb(dic):
    nb_viable = 0
    for nodeA in dic.keys():
        if dic[nodeA][1] == 0:
            continue
        for nodeB in dic.keys():
            if nodeB == nodeA:
                pass
            else:
                if dic[nodeA][1] <= dic[nodeB][2]:
                    # raw_input()
                    nb_viable += 1
                else:
                    pass
    return nb_viable
    
# def make_map(dic):
    # map = []
    # global dimension_x
    # global dimension_y
    
    # for i in range(0, dimension_x + 1):
        # new_column = []
        # for j in range(0, dimension_y + 1):
            # new_column.append((dic[(i, j)][1], dic[(i, j)][2]))
        # map.append(new_column)
    # return map

# def new_dic(dic):
    # new_dic = {}
    # for key in dic.keys():
        # words = key.split('-')
        # x_value = int(words[-2][1:])
        # y_value = int(words[-1][1:])
        # new_dic[(x_value, y_value)] = dic[key]
    # return new_dic      

# def find_pair(dic):
    # list_pair = []
    # for nodeA in dic.keys():
        # for nodeB in dic.keys():
            # if nodeB == nodeA:
                # pass
            # else:
                # if dic[nodeA][1] <= dic[nodeB][2]:
                    # list_pair.append((dic[nodeA], dic[nodeB]))
                # else:
                    # pass
    # return list_pair
    
# def shortest_path(map, list_pair):
    # nb_steps = 0
    # global dimension_x

    # for i in range(0, dimension_x):
        # nb_steps += bfs(map, dimension_x - 1 - i, 0, list_pair)
        # nb_steps += 1
    # return nb_steps
    
# def bfs(map, i, j, list_pair):
    # global dimension_x
    # global dimension_y
    # stack = [((i, j), [map[i][j]])]
    
    # while(stack):
        # current_path = stack.pop(0)
        # print len(stack)
        # raw_input()
        # x, y = current_path[0]
        # initial_path = current_path[1]
        
        # if len(initial_path) >= 2 and (initial_path[-2], initial_path[-1]) in list_pair:
            # return len(initial_path)
        # else:
            # pass
        
        # if len(initial_path) >= 2:
            # if x - 1 >= 0 and (x - 1, y) != path[-2]:
                # path = copy.copy(initial_path)
                # path.append(map[x - 1][y])
                # stack.append(((x - 1, y), path))
            # if x + 1 <= dimension_x and (x + 1, y) != path[-2]:
                # path = copy.copy(initial_path)
                # path.append(map[x + 1][y])
                # stack.append(((x + 1, y), path))
            # if y - 1 >= 0 and (x, y - 1) != path[-2]:
                # path = copy.copy(initial_path)
                # path.append(map[x][y - 1])
                # stack.append(((x, y - 1), path))
            # if y + 1 <= dimension_y and (x, y + 1) != path[-2]:
                # path = copy.copy(initial_path)
                # path.append(map[x][y + 1])
                # stack.append(((x, y + 1), path))
        # else:
            # if x - 1 >= 0:
                # path = copy.copy(initial_path)
                # path.append(map[x - 1][y])
                # stack.append(((x - 1, y), path))
            # if x + 1 <= dimension_x:
                # path = copy.copy(initial_path)
                # path.append(map[x + 1][y])
                # stack.append(((x + 1, y), path))
            # if y - 1 >= 0:
                # path = copy.copy(initial_path)
                # path.append(map[x][y - 1])
                # stack.append(((x, y - 1), path))
            # if y + 1 <= dimension_y:
                # path = copy.copy(initial_path)
                # path.append(map[x][y + 1])
                # stack.append(((x, y + 1), path))
                
if __name__ == '__main__':
    infos_dic = read_file('input.txt')
    #****************part1**************
    # print  read_file('input.txt')
    # print find_pair_nb(infos_dic)
    #****************part2**************
    # global dimension_x
    # global dimension_y
    # dimension_x = 37
    # dimension_y = 25
    
    # infos_dic = new_dic(infos_dic)
    # my_map = make_map(infos_dic)
    # print numpy.array(my_map)
    for i in range(0, 38):
        if my_map[i][13][0] < 100:
            print i
            
    # 我去第二部分用正常的最短路径算法很难，直接找规律，还是挺有意思的题目，在y = 13的时候除了x = 0
    # 其他x上的used巨大，所以必须要从x = 0 绕一下，还是挺有意思的
    
    # raw_input()
    # list_pair = find_pair(infos_dic)
    # print shortest_path(my_map, list_pair)
    # print my_map[37][0]
    
    print '\n'
    print 'All done baby!!'