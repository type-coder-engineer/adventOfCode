# coding:utf

#calcul the moving in part 1
def get_code(mymap, hints):
    position1 = 1
    position2 = 1
    code = []
    for hint in hints:
        for one in hint:
            if one == 'U':
                position1 = move(position1, -1)
            elif one == 'D':
                position1 = move(position1, 1)
            elif one == 'L':
                position2 = move(position2, -1)
            elif one == 'R':
                position2 = move(position2, 1)
            else:
                print 'Something wrong with the get_code....'
                return
        code.append(mymap[position1][position2]) 
    return code

    #calcul the moving in part 2
def get_code_part2(mymap, hints):
    position = [2, 0]
    code = []
    for hint in hints:
        for one in hint:
            if one == 'U':
                position = move_v(position[0], position[1], -1)
                # print position
            elif one == 'D':
                position = move_v(position[0], position[1], 1)
                # print position
            elif one == 'L':
                position = move_h(position[1], position[0], -1)
                # print position
            elif one == 'R':
                position = move_h(position[1], position[0], 1)
                # print position
            else:
                print 'Something wrong with the get_code....'
                return
        # print position
        # print '**************'
        code.append(mymap[position[0]][position[1]]) 
    return code    
    
# calcul the moving within the restrains
def move(position, step):
    position += step
    if position > 2:
        position = 2
    elif position < 0:
        position = 0
    return position  

    #  # the function of moving on colomn
def move_v(position_change, position_condition, step):
    position = [position_change, position_condition]
    freedom = free(position_change, position_condition)
    # print freedom
    position[0] += step
    if position[0] > (2 + freedom):
        position[0] = 2 + freedom
    elif position[0] < 2 - freedom:
        position[0] = 2 - freedom
    else:
        if step < 0 and (position[0] == 2 or position[0] == 3):
            position[1] += 1
        elif step < 0 and (position[0] == 0 or position[0] == 1):
            position[1] -= 1
        elif step > 0 and (position[0] == 1 or position[0] == 2):
            position[1] += 1
        elif step > 0 and (position[0] == 3 or position[0] == 4):
            position[1] -= 1
            
    return position

    # calcul the freedom, which means the possbility of moving in certain row and colomn
def free(position_change, position_condition):
    # print position_change
    # print position_condition
    if (abs(abs(position_change - 2) - 1) == position_condition) or (abs(abs(position_change - 2) - 1) == position_condition - 2):
        freedom = 1
    elif abs(position_change - 2) + position_condition + 2 == 4:
        freedom = 2
    elif (position_condition == 0) or (position_condition == 4):
        freedom = 0
    else:
        print 'Wrong'
        return
    return freedom
    
    # the function of moving on row
def move_h(position_change, position_condition, step):
    position_change += step
    position = [position_condition, position_change]
    freedom = 2 - abs(2 - position[0]) 
    if position[1] > (2 * freedom):
        position[1] = 2 * freedom
    elif position[1] < 0:
        position[1] = 0
    return position
    
if __name__ == '__main__':
    hints = []
    hints.append('DLDRDDDLULDRRLUDDLDUURDRDUULDRDDRRLDLLUUDDLLRLRDRUURLUDURDDRURLUDDUULUURLLRRRRUDULUDLULLUURRLLRRURRUDUUURRLUUUDURDLLLDULDRLRDDDUDDUURLRRRURULLUDDUULDRRRDDLRLUDDRRDLRDURLRURUDDUULDDUUDDURRLUURRULRRLDLULLRLRUULDUDDLLLRDDULRUDURRDUUDUUDDUULULURDLUDRURDLUUDRDUURDDDRDRLDLDRURRLLRURURLLULLRRUULRRRRDLDULDDLRRRULRURRDURUDUUULDUUDRLDDLDUDDRULLUDUULRRRDRRDRDULDLURDDURLRUDLURLUDDDRLLURUUUUUUURUULDUUDDRLULRUDURRDLDUULLRLULLURDDDDDLRRDLRLLDDUDRRRDDURDLRRUDDUDLRRRDDURULRURRRLDRDUDLD')
    hints.append('LRRDUDUUUDRRURRDUUULULUDDLLDRRRUDDUULRRDRUDRLLRLRULRRDUUDRLDURUDLLLDRRDLRLUUDRUDRRRUDRRRULDRRLLRDDDLLRDDRULRLLRUDRLLLULDLDDRDRUUUUUULURLLRUDRDRLLULLRUUURRDRULULUDLDURRUUDURLLUDRDLDDULUDLRDDRLRLURULDRURRRRURRDDUDRULUUUDDDRULRULDLLURUUULRDDLRUURLRLDLUULLURDRDDDUDDDRLDRDLLDRDDDDURLUUULDDRURULUDDURDRDRLULDULURDUURDRLLUUUULRULUUDRLLDDRRURUURLDLLRRRDLRURDDLDLDRLRRDLDURULDDLULRRRUUDLRDUURDURLURDDLDLRURLLLDRDULDDRUDDULDDRRLDLRDRDLDUUDLUULRLUDUUDUUUULDURULRRUDULURLRLDRLULLLDUDLLLRUDURDDDURLDDLRLRRDLUDLDDDDLULDRLDUUULDRRDDLRUULDLULUUURUDDRLDDDULRUDRURUURUUURRULRURDURLLRLLUULUULURDRLLUDDLU')
    hints.append('LLDURDUDRLURUDRLRLUDDRRURDULULDDUDUULRRLRLRRDRDRDURRLRLURRLRUDULLUULLURUDDRLDDDRURLUUDLDURRDURDDLUULRDURRUUURLRRURRDRDRDURRRLULLDRUDLRUDURDRDDLLULLULRRUDULDDRDRRDLLLDLURLRDRDLUDDRLDDLDRULDURLLRLDRDLUDDDDLDUUDRLLRRRRLDDRRLRLURLLRLLUULLDUUDLRDRRRDRDLLDULLDRLDDUDRDDRURRDDLRDLRRUUDRRRRDURUULDRDDURLURRRRURRDRRULULURULUUUDRRRLDLLLDDRULRUDDURDRLDDRDLULLLRURUDRLRDDLDLRRRUURDURLDURRUUDDLRDRUUUURDLRLULRUUDRLDLULLULUURURDULUDUDRRRLLRLURLLDLRRURURRUDLUDDDDRDUDUDUUUULLDRDLLLLUUUUDRLRLUDURLLUDRUUDLLURUULDDDDULUUURLLDL')
    hints.append('DLULLRDLRRLLLDLRRURRDRURDRUUULDDRLURURRDLRRULUUDDRLRRLDULRRUUDUULDDDUDLLDLURDRLLULLUUULLDURDRRRDDLRDUDRRRLRLDRRLRLULDDUDURRRLDLRULDULDDUDDRULDLDRDRDDRUDRUDURRRRUUDUDRLDURLDLRRUURRDDUDLLDUDRRURRLRRRRRLDUDDRLLLURUDRRUDRLRDUDUUUUUDURULLDUUDLRUUULDUUURURLUUDULDURUDDDLRRRDDRRDLRULLLRDDRLRLUULDUUULLLLDLRURLRRDURRLDLLLDURDLLUDDDLLDDURDDULURDRRRDDDLDDURRULUUDDLULLURULUULDLDDLUDRURURULUDDULRDRLDRRRUUUURUULDRLRRURRLULULURLLDRLRLURULRDDDULRDDLUR')
    hints.append('RURRULLRRDLDUDDRRULUDLURLRRDDRDULLLUUDDDRDDRRULLLDRLRUULRRUDLDLLLRLLULDRLDDDLLDDULLDRLULUUUURRRLLDRLDLDLDDLUDULRDDLLRLLLULLUDDRDDUUUUDLDLRRDDRDLUDURRUURUURDULLLLLULRRLDRLRDLUURDUUDLDRURURLLDRRRLLLLRDLDURRLRRLLRUUDDUULLRLUDLRRRRRURUDDURULURRUULRDDULUUDUUDDRDDDDDUUUDDDRRLDDRRDDUUULDURLDULURDRDLLURDULRUDRUULUULLRRRRLRUUDDUDLDURURLRRRULRDRRUDDRDDRLRRRLRURRRUULULLLUULLLULLUDLRDLDURRURDLDLRDUULDRLLRRLDUDDUULULR')
    # hints.append('R')
    # hints.append('DDD')
    # hints.append('RUUU')
    #*************part1*************************    
    # mymap = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # code = get_code(mymap, hints)
    # print code
    #*************part2*************************      
    mymap2 = [[1], [2, 3, 4], [5, 6, 7, 8, 9], ['A', 'B', 'C'], ['D']]
    code = get_code_part2(mymap2, hints)
    print code 
    
    print '\n'
    print 'All done baby!!'
        