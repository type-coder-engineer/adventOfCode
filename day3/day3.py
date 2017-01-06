# coding: utf

#注意这个数据不是很好，中间的空格有两个和三个，所以要有一个条件来去除列表中的''项
def read_input(filename):
    triangles = []
    for line in open(filename):
        line = line.strip(' ')
        line = line.strip('\n')
        triangle = line.split(' ')
        final = []
        for one in triangle:
            if one != '':
                final.append(int(one.strip(' ')))
            else:
                pass
        triangles.append(final)
    return triangles

def read_input_part2(filename):
    triangles = []
    tri1 = []
    tri2 = []
    tri3 = []
    flag = 0
    for line in open(filename):
        flag += 1
        line = line.strip(' ')
        line = line.strip('\n')
        triangle = line.split(' ')
        for one in triangle:
            if one != '':
                if flag % 3 == 1:
                    tri1.append(int(one.strip(' ')))
                elif flag % 3 == 2:
                    tri2.append(int(one.strip(' ')))
                elif flag % 3 == 0:
                    tri3.append(int(one.strip(' ')))
            else:
                pass
        if flag % 3 == 0: 
            triangles.append([tri1[0], tri2[0], tri3[0]])
            triangles.append([tri1[1], tri2[1], tri3[1]])
            triangles.append([tri1[2], tri2[2], tri3[2]])
            tri1 = []
            tri2 = []
            tri3 = []
    return triangles    
    
    # 注意这个不行，因为条件应该是小于等于
def det_triangle1(triangle):
    if triangle[0] + triangle[1] < triangle[2]:
        return False
    elif triangle[1] + triangle[2] < triangle[0]:
        return False
    elif triangle[2] + triangle[0] < triangle[1]:
        return False
    else:
        return True

def det_triangle2(triangle):        
    triangle.sort()
    if triangle[0] + triangle[1] > triangle[2]:
        return True
    else:
        return False
        
def nb_triangles(input):
    nb = 0
    list1 = []
    list2 = []
    # 注意初始化的时候不能list1 = list2，因为这样两个list就相当于是一个了。一定要记得list的赋值是引用！！
    for i  in range(0, len(input)):
        if det_triangle2(input[i]):
            list2.append(input[i])
            nb += 1
    return nb
    # print len(list1)
    # print len(list2)
    # print nb
    # for one in list1:
        # if one in list2:
            # continue
        # else:
            # return one
        
if __name__ == '__main__':
    #*************part1*************************    
    # input = read_input('input.txt')
    # print nb_triangles(input)
    #*************part2*************************      
    input = read_input_part2('input.txt')
    print nb_triangles(input)
    
    print '\n'
    print 'All done baby!!'