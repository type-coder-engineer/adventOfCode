# coding: utf
import numpy

def det_type(position):
    global id
    sum = 0
    x = int(position[0])
    y = int(position[1])
    formule = x*x + 3*x + 2*x*y + y + y*y + id
    bi = bin(formule)
    for one in bi:
        if one == '1':
            sum += 1
    if sum % 2 == 0:
        return '.'
    else:
        return '#'

def get_map():
    global map_dimension
    list = []
    for i in range(0, map_dimension):
        column = []
        for j in range(0, map_dimension):
            column.append(det_type([i,j]))
        list.append(column)
    return list

    #用map_list 生成一个包含各个点之间距离的list，注意不能过去的#就用99999代替即可
def make_list_dijkstra(list, dimension):
    list_distance = []
    new_dimension = dimension ** 2
    for k in range(0, new_dimension):
        row = []
        for i in range(0, len(list)):
            for j in range(0, len(list)):
                index = i * dimension + j
                if k == index:
                    row.append(0)
                else:
                    if up_down_left_right(k, dimension, i, j):
                        if list[i][j] == '.':
                            row.append(1)
                        else:
                            row.append(99999)
                    else:
                        row.append(99999)
        list_distance.append(row)
    print 'list of distance ready'
    return list_distance
    
    # 确定上下左右是 . 还是 #      
def up_down_left_right(k, dimension, i, j):            
    row = k // dimension
    column = k % dimension
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
def search_path_dijkstra(list, depart, destination):
    distance = list[depart]
    distance_dic = {}
    for i in range(0, len(distance)):
        if distance[i] != 0:
            distance_dic[i] = distance[i]
            
    while(len(distance_dic) > 0):
        print len(distance_dic) 
        possible_relax = distance_dic.values()
        possible_relax.sort()
        relax_value = possible_relax[0]
        for key, value in distance_dic.items():
            if value == relax_value:
                relax_key = key
                del distance_dic[key]
                break
        # print relax_key
        for i in range(0, len(list[relax_key])):
            if i == depart:
                continue
            else:
                if list[relax_key][i] + relax_value < list[depart][i]:
                    list[depart][i] = list[relax_key][i] + relax_value
                    distance_dic[i] = list[relax_key][i] + relax_value
                    # print i, list[relax_key][i] + relax_value
                    # raw_input()
    
    print '*****************************'
    return list[depart][destination]    

    # part2 用fbs比较适合，因为不是搜索最短路径而是50步内最大范围，所以应该使用广度优先算法
def search_bfs(list):
    stack = [((1,1), ' ')]
    diff_locations = {}
    
    while(stack):
        pos, path = stack.pop(0)
        steps = len(path) - 1
        print steps
        if steps > 50:
            return len(diff_locations)
        diff_locations[pos] = path
        x,y = pos
        
        if x - 1 >= 0 and list[x - 1][y] == '.' and path[-1] != 'R':
            stack.append([(x - 1, y), path + 'L'])
        if x + 1 < map_dimension and list[x +1][y] == '.' and path[-1] != 'L':
            stack.append([(x + 1, y), path + 'R'])
        if y - 1 >= 0 and list[x][y - 1] == '.' and path[-1] != 'D':
            stack.append([(x, y - 1), path + 'U'])
        if y + 1 < map_dimension and list[x][y + 1] == '.' and path[-1] != 'U':
            stack.append([(x, y + 1), path + 'D'])    
     
if __name__ == '__main__':
    #*************part1*************************    
    global map_dimension
    global id
    id = 1358
    map_dimension = 60
    map_list = get_map()
    # print search_path_dijkstra(make_list_dijkstra(map_list, map_dimension), 61, 1899)
    #*************part2*************************      
    print '*************************'
    print search_bfs(map_list)
    
    print '\n'
    print 'All done baby!!'