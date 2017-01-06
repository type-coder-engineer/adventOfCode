# coding: utf-8
import hashlib
import copy
import bfs
import sys
import time
sys.setrecursionlimit(1000)

def search_path(current_path, current_pos, path_list):
    # current_pos = det_pos(current_path)
    current_choice = get_direction(current_path, current_pos)
    # if current_path == 'ihgpwlahDRRULDUDDDURR': #LUDRD
        # print current_pos
        # print current_choice
        # raw_input()
    if len(current_choice) == 0:
        # print 'dead end'
        return
    else:
        if len(current_choice) == 1:
            current_path = guide_path(current_choice[0], current_pos, current_path)
            if current_pos == [3,3]:
                path_list.append(current_path)
                return 
            else:
                search_path(current_path, current_pos, path_list)  
        else: 
            # print 'plenty ways'
            initial_path = current_path
            initial_pos = (current_pos[0], current_pos[1])
            # print initial_pos, ' with ', initial_path
            for choice in current_choice:
                current_path = initial_path
                # current_pos1 = det_pos(current_path)
                current_pos = [initial_pos[0], initial_pos[1]]
                # if current_pos != current_pos1:
                    # print current_path
                    # raw_input()
                current_path = guide_path(choice, current_pos, current_path)
                if current_pos == [3,3]:
                    path_list.append(current_path)
                    continue  # 我去这里一个bug我搞了两天，一开始我没写continue 而写的return，
                    # 然而这样不管for有没有完成就直接返回上一个节点去了。。。注意for中几个分支都是
                    #同一深度的，画图的时候不要画到下一个深度去！！
                else:
                    search_path(current_path, current_pos, path_list)
                # current_path = initial_path
    return path_list

def det_pos(path):
    path_add = path[8:]
    pos = [0,0]
    for one in path_add:
        if one == 'U':
            pos[0] -= 1
        if one == 'D':
            pos[0] += 1
        if one == 'L':
            pos[1] -= 1
        if one == 'R':
            pos[1] += 1 
    return pos    
                 
def guide_path(choice, current_pos, current_path):
    if choice == 'up':
        current_path += 'U'
        current_pos[0] -= 1
    if choice == 'down':
        current_path += 'D'
        current_pos[0] += 1
    if choice == 'left':
        current_path += 'L'
        current_pos[1] -= 1
    if choice == 'right':
        current_path += 'R'
        current_pos[1] += 1
    return current_path    
 
def get_direction(string, current_pos):
    md5 = hashlib.md5(string).hexdigest() 
    mystring = md5[0:4]
    option = ['b', 'c', 'd', 'e', 'f']
    directions = []
    if mystring[0] in option:
        if current_pos[0] > 0:
            directions.append('up')
    if mystring[1] in option:
        if current_pos[0] < 3:
            directions.append('down')
    if mystring[2] in option:
        if current_pos[1] > 0:
            directions.append('left')
    if mystring[3] in option:
        if current_pos[1] < 3:
            directions.append('right')
    return directions
        
def shortest_path(list):
    path_dic = {}
    for path in list:
        path_dic[path] = len(path)
    distances = path_dic.values()
    distances.sort()
    for path, distance in path_dic.items():
        if distance == distances[0]:
            return path[8:]

def longest_path(list):
    path_dic = {}
    for path in list:
        path_dic[path] = len(path[8:])
    distances = path_dic.values()
    distances.sort()
    return distances[-1]
    # for path, distance in path_dic.items():
        # if distance == longest:
            # return len(path[8:])
    # return distances[-1]

    
if __name__ == '__main__':
    #*************part1*************************    
    input = 'bwnlcvfs'
    # test = 'ihgpwlah'
   # print hashlib.md5(test).hexdigest() 
    initial = [0,0]
    path_list = []
    # global index
    start = int(round(time.time() * 1000))
    list = search_path(input, initial, path_list)
    end = int(round(time.time() * 1000))
    print end - start  
    # 实验可得如果是要找到所有的路径这个方法和bfs的速度差不多
    # 但是如果只想找最短路径还必须要用bfs, 试了一下bfs只花了0ms。。。。
    # print shortest_path(list)
    #*************part2*************************   
    # debug方法不好，应该早点用这种比较不同的output然后选择最简单的研究问题的方法
    # list_bfs = bfs.bfs(test)
    # diff = []
    # for one in list_bfs:
        # if one in list:
            # pass
        # else:
            # diff.append(one)
    # diff.sort()
    # print diff
    # for one in diff:
        # print one
    # print longest_path(list)
    
    print '\n'
    print 'All done baby!!'