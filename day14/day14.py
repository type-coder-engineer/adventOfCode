# coding: utf
import hashlib

def get_code():
    list_keys = []
    id = 'yjdafjpo'
    # id = 'jlmsuwbz'
    # id = 'abc'
    index = 0
    while(1):
        string_index = str(index)
        puzzle = id + string_index
        # print puzzle
        output = md5_2017(puzzle)
        # print output
        # raw_input()
        target = triple(output)
        # print target
        # print '************'
        # print index
        if target != '':
            # print output
            # print target,target,target
            for i in range(1, 1001):
                myindex = index + i
                # print myindex
                # raw_input()
                string_index1 = str(myindex)
                puzzle1 = id + string_index1
                output1 = md5_2017(puzzle1)
                if five_same(output1, target):
                    list_keys.append(index)
                    # print output
                    print index
                    # print output1
                    # print myindex
                    print len(list_keys)
                    print '*************'
                    # raw_input()
                    break
                else: 
                    pass
            # raw_input()
        else:
            pass
        index += 1
        if len(list_keys) >= 64:
            return list_keys[63]           
 
def md5_2017(string): # part2
    for i in range(0, 2017):
        string = hashlib.md5(string).hexdigest() 
    return string
    
def triple(string):
    for i in range(0, len(string) - 2):
        if string[i] == string[i + 1] and string[i] == string[i + 2]:
            return string[i]
            # if i == 0:
                # if string[i] != string[i + 3]:
                    # return string[i]
            # elif i == len(string) - 3:
                # if string[i] != string[i - 1]:
                    # return string[i]
            # else:
                # if string[i] != string[i - 1] and string[i] != string[i + 3]:
                    # return string[i]
           
    return ''
    
def five_same(string, letter):
    for i in range(0, len(string) - 4):
        if string[i] == letter and string[i] == string[i + 1] and string[i] == string[i + 2] and string[i] == string[i + 3] and string[i] == string[i + 4]:
            return True
    return False    

if __name__ == '__main__':
    #*************part1*************************    
    # print MD5.main_md5('abc22728') 
    print get_code()
    # print five_same('sssssdfashflehie', 's')
    # print triple(hashlib.md5('abc22728').hexdigest())
    #*************part2*************************      
    
    print '\n'
    print 'All done baby!!'