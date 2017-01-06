# coding: utf-8

def det_row(input):
    list_row = [input]
    for i in range(0, 399999):
        print i
        new = ''
        for j in range(0, len(list_row[i])):    
            if j == 0:
                if rules('', list_row[i][j], list_row[i][j + 1]):
                    new += '^'
                else:
                    new += '.'
            elif j == (len(list_row[i]) - 1):
                if rules(list_row[i][j - 1], list_row[i][j], ''):
                    new += '^'
                else:
                    new += '.'
            else:
                if rules(list_row[i][j - 1], list_row[i][j], list_row[i][j + 1]):
                    new += '^'
                else:
                    new += '.'
        # print new
        list_row.append(new)
    return list_row
    
def rules(left, center, right):
    if left == '^' and center =='^' and right != '^':
        return True
    elif left != '^' and center =='^' and right == '^':
        return True
    elif left == '^' and center != '^' and right != '^':
        return True
    elif left != '^' and center != '^' and right == '^':
        return True
    else:
        return False
    

def count_safe(list):
    # print list
    nb = 0
    for row in list:
        for one in row:
            if one == '.':
                nb += 1
    return nb    
    
    
if __name__ == '__main__':
    #*************part1*************************    
    input = '^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.'
    list = det_row(input)
    print count_safe(list)
    #*************part2*************************      
    
    print '\n'
    print 'All done baby!!'