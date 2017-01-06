# coding: utf-8
import sys
# sys.setrecursionlimit(25) # 这个是设置递归深度的，不过这道题最深就是21，所以不用额外改limit

# 第一部分一开始为了填满增长string
def make_longer(string):
    length = 272
    while(1):
        if len(string) >= length:
            break
        copy = ''
        for i in range(0, len(string)):
            copy += string[-i - 1]
        new_copy = ''
        for i in range(0, len(copy)):
            if copy[i] == '0':
                new_copy += '1'
            else:
                new_copy += '0'
        string += ('0' + new_copy)
    return string[0: length]
    
# 第一部分缩短string直到位数为奇数
def make_shorter(string):
    while(1):
        if len(string) % 2 != 0:
            break
        new = ''
        for i in range(0, len(string), 2):
            if string[i] == string[i + 1]:
                new += '1'
            else:
                new += '0'
        string = new
    return string

# def test():
    # test = 35651584.0
    # nb = 0
    # while(1):
        # if test % 2 != 0:
            # break
        # test /= 2
        # nb += 1
    # print test
    # return nb

    # 得到夹在input和input变化形式中的0和1的string，为了之后用index来找出原始string中是0还是1
def string_0and1():
    string = '0'
    for i in range(0, 21):
        to_add = ''
        for i in range(0, len(string)):
            if string[-i - 1] == '1':
                to_add += '0'
            else:
                to_add += '1'
        string += ('0' + to_add)
        # print string
    return string

    # 得到input的变化形式
def copy(mystring):
    new = ''
    for i in range(0, len(mystring)):
        if mystring[-i - 1] == '1':
            new += '0'
        else:
            new += '1'
    return new
 
# 二叉树递归，用index1和index2来表示在string中的位置，当两个index相差1的时候就是相邻的两个数，也就是二叉树的末端，然后就可以异或比较了 
def find_code(index1, index2, string, string_copy, added):
    if abs(index2 - index1) == 1:
        return generate_next_depth(det_bit(index1, string, string_copy, added), det_bit(index2, string, string_copy, added))
    else:
        median = (index1 + index2 + 1) / 2 - 1
        # print index1
        # print median
        # print index2
        # raw_input()
        bit1 = find_code(index1, median, string, string_copy, added)
        bit2 = find_code(median + 1, index2, string, string_copy, added) # 注意一开始忘了+1了，导致递归出错
    return generate_next_depth(bit1, bit2)

# 实现异或    
def generate_next_depth(bit1, bit2):
    if bit1 == bit2:
        return '1'
    else:
        return '0'

# 通过index找到原始string中的0或1
def det_bit(input, string, string_copy, added):
    rest = input % 18
    multi = input // 18
    if multi % 2 == 0:
        string_to_search = string + added[multi]
    else:
        string_to_search = string_copy + added[multi]
    return string_to_search[rest]
    
if __name__ == '__main__':
    #*************part1*************************    
    string_input = '10111100110001111'
    string_input_copy = copy(string_input)
    # print string_input_copy
    # print len(string_input_copy)
    # output = make_longer(input)
    # print make_shorter(output)
    # print five_same('sssssdfashflehie', 's')
    # print triple('eddd')
    #*************part2*************************      
    string_0and1 = string_0and1()
    
    string_code = ''
    for i in range(0,17):
        string_code += find_code(i*2**21, (i + 1)*2**21 - 1, string_input, string_input_copy, string_0and1)
        print len(string_code)
        print string_code
        print '******************'
    print string_code
    
    print '\n'
    print 'All done baby!!'