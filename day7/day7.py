# coding: utf

def read_input(filename):
    data_list = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        outside = ''
        inside = ''
        index = -1
        flag_inside = 0
        while(1):
            index += 1
            if index >= len(line):
                break
            if line[index] == '[':
                flag_inside = 1
                outside += ' ' 
                continue
            if line[index] == ']':
                flag_inside = 0
                inside += ' ' # 注意如果没有这个空格的话可能隔着[]的4个字母可以是ABBA的
                continue
            if flag_inside == 0:
                outside += line[index]
            else:
                inside += line[index]
        
        mylist_add = [outside, inside]
        data_list.append(mylist_add)
    return data_list

def get_nb(input):
    nb = 0
    for one in input:
        if det_TLS(one[0]) and not det_TLS(one[1]):
            nb += 1
        else:
            pass
    return nb

def get_nb_part2(input):
    nb = 0
    for one in input:
        mylist = det_SSL(one[0])
        if len(mylist) != 0:
            new_list = []
            for string in mylist:
                new = string[1:] + string[1]
                new_list.append(new)
            for new in new_list:
                if new in one[1]:
                    nb += 1
                    break
                else:
                    pass
        else:
            pass
    return nb
    
def det_TLS(string):
    if len(string) < 4:
        return False
    else:
        for i in range(0, len(string) - 3):
            if string[i] == string[i + 3] and string[i + 1] == string[i + 2] and string[i] != string[i + 1]:
                # print string[i:i+4]
                return True
            else:
                pass
        return False

def det_SSL(string):
    list_SSL = []
    if len(string) < 3:
        return False
    else:
        for i in range(0, len(string) - 2):
            if string[i] == string[i + 2] and string[i] != string[i + 1] and string[i] != ' ' and string[i + 1] != ' ':
                list_SSL.append(string[i:i + 3])
            else:
                pass
        return list_SSL
        
if __name__ == '__main__':
    #*************part1*************************    
    # input = read_input('input.txt')
    # print get_nb(input)
    #*************part2*************************      
    input = read_input('input.txt')
    print get_nb_part2(input)

    print '\n'
    print 'All done baby!!'