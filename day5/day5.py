# coding=utf-8  
import MD5

def decode():
    password = ['8','c','-','5','d','1','a','b']
    my_range = ['0','1','2','3','4','5','6','7']
    nb_found = 7
    index = 24000000
    id = 'ffykfhsq' # given info
    while(1):
        string_index = str(index)
        puzzle = id + string_index
        output = MD5.main_md5(puzzle)
        print output
        if len(output) < 6:
            index += 1
            continue
        else:    
            flag_found = 1
            for i in range(0, 5):
                if output[i] != '0':
                    flag_found = 0
                    break
            if flag_found == 0:
                index += 1
                print index
                print nb_found
                print password
                continue
            else:
                if output[5] in my_range:
                    if password[int(output[5])] == '-':
                        password[int(output[5])] = output[6]
                        nb_found += 1
                        print password
                    else:
                        pass
                else:
                    pass
                # print '*******************************'
                index += 1
        if nb_found == 8:
            return password

if __name__ == '__main__':
    #*************part1*************************    
    print decode()
    #*************part2*************************      
# 算到27000000多次终于算出来结果了。。。
    
    print '\n'
    print 'All done baby!!'