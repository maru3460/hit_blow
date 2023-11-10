import copy
import random

poses = []#possibles
init_num = 3#見つかっていない数字の数
init_nums = [i for i in range(10)]#質問していない数字
run = True

def cul_poses(poses):
    rtn = 0
    for i in range(len(poses)):
        rtn += len(poses[i][0]) * len(poses[i][1]) * len(poses[i][2])
    return rtn

def gene_num(poses):#数字の生成
    global init_num
    global init_nums
    rtn = []
    if init_num > 0 and len(init_nums) > 3:
        tmp = random.choice(range(len(init_nums)))
        rtn.append(init_nums[tmp])
        init_nums.pop(tmp)
        tmp = random.choice(range(len(init_nums)))
        rtn.append(init_nums[tmp])
        init_nums.pop(tmp)
        tmp = random.choice(range(len(init_nums)))
        rtn.append(init_nums[tmp])
        init_nums.pop(tmp)
    elif init_num <= 1:
        if len(init_nums) == 1:
            if init_num == 1:
                one_decided(poses, init_nums[0])
                init_num -= 1
            elif init_num == 0:
                one_remove(poses, init_nums[0])
                init_num -= 1
            else:
                print(f'{init_nums} {init_num}')
                print('error:len(init_nums), init_num')
                exit(0)
        init_nums = []
        tmp = random.choice(range(len(poses)))
        tmp_run = True
        while(tmp_run):
            tmp_run = False
            x = poses[tmp][0][random.choice(range(len(poses[tmp][0])))]
            y = poses[tmp][1][random.choice(range(len(poses[tmp][1])))]
            if x == y:
                tmp_run = True
            z = poses[tmp][2][random.choice(range(len(poses[tmp][2])))]
            if y == z or z == x:
                tmp_run = True
        rtn.append(x)
        rtn.append(y)
        rtn.append(z)
    else:
        print(f'{init_num}')
        print('error:init_num')
        exit(0)
    return rtn

def one_decided(poses, n):#残り一個確定
    tmp = [i for i in range(10)]
    tmp.remove(n)
    pos = [[[n], copy.deepcopy(tmp), copy.deepcopy(tmp)], [copy.deepcopy(tmp), [n], copy.deepcopy(tmp)], [copy.deepcopy(tmp), copy.deepcopy(tmp), [n]]]
    itgr_pos(poses, pos)

def one_remove(poses, n):#残り一個消去
    tmp = [i for i in range(10)]
    tmp.remove(n)
    pos = [[copy.deepcopy(tmp), copy.deepcopy(tmp), copy.deepcopy(tmp)]]
    itgr_pos(poses, pos)

def io(test_num, poses):#inout
    print(f'{test_num[0]}{test_num[1]}{test_num[2]}を入力してください')
    print(f'poses: {cul_poses(poses)}')
    hit = int(input('hit:'))
    if hit == 'end':
        exit()
    blow = int(input('blow:'))
    return [hit, blow]

def gene_pos(hit, blow, x, y, z):#pos生成
    global init_num
    nums = [i for i in range(10)]
    tmp = copy.deepcopy(nums)
    tmp.remove(x)
    tmp.remove(y)
    tmp.remove(z)
    if hit == 0 and blow == 0:
        return [[copy.deepcopy(tmp), copy.deepcopy(tmp), copy.deepcopy(tmp)]]
    elif hit == 1 and blow == 0:
        init_num -= 1
        return [[[x], copy.deepcopy(tmp), copy.deepcopy(tmp)], [copy.deepcopy(tmp), [y], copy.deepcopy(tmp)], [copy.deepcopy(tmp), copy.deepcopy(tmp), [z]]]
    elif hit == 0 and blow == 1:
        init_num -= 1
        return [[[y, z], copy.deepcopy(tmp), copy.deepcopy(tmp)], [copy.deepcopy(tmp), [x, z], copy.deepcopy(tmp)], [copy.deepcopy(tmp), copy.deepcopy(tmp), [x, y]]]
    elif hit == 2 and blow == 0:
        init_num -= 2
        return [[[x], [y], copy.deepcopy(tmp)], [copy.deepcopy(tmp), [y], [z]], [[x], copy.deepcopy(tmp), [z]]]
    elif hit == 1 and blow == 1:
        init_num -= 2
        return [[[x], [z], copy.deepcopy(tmp)], [[x], copy.deepcopy(tmp), [y]], [[z], [y], copy.deepcopy(tmp)], [copy.deepcopy(tmp), [y], [x]], [[y], copy.deepcopy(tmp), [z]], [copy.deepcopy(tmp), [x], [z]]]
    elif hit == 0 and blow == 2:
        init_num -= 2
        tmp_rtn = []
        tmp_rtn.append([[y], [x], copy.deepcopy(tmp)])
        tmp_rtn.append([[y], copy.deepcopy(tmp), [x]])
        tmp_rtn.append([copy.deepcopy(tmp), [x], [y]])
        tmp_rtn.append([[y], [z], copy.deepcopy(tmp)])
        tmp_rtn.append([[z], copy.deepcopy(tmp), [y]])
        tmp_rtn.append([copy.deepcopy(tmp), [z], [y]])
        tmp_rtn.append([[z], [x], copy.deepcopy(tmp)])
        tmp_rtn.append([[z], copy.deepcopy(tmp), [x]])
        tmp_rtn.append([copy.deepcopy(tmp), [z], [x]])
        return tmp_rtn
    elif hit == 3 and blow == 0:
        init_num -= 3
        return True
    elif hit == 1 and blow == 2:
        init_num -= 3
        return [[[x], [z], [y]], [[z], [y], [x]], [[y], [x], [z]]]
    elif hit == 0 and blow == 3:
        init_num -= 3
        return [[[y], [z], [x]], [[z], [x], [y]]]
    else:
        print(f'{hit} {blow}')
        print('error:hit, blow')
        exit(0)

def itgr_pos(poses, pos):#生成されたposとposesの統合
    if len(poses) == 0:
        tmp_poses = copy.deepcopy(pos)
    else:
        tmp_poses = []
        for i in range(len(poses)):
            for j in range(len(pos)):
                tmp = pos_pos(poses[i], pos[j])
                if tmp != False:
                    tmp_poses.append(tmp)
    return tmp_poses

def pos_pos(pos1, pos2):#posとposからposを生成
    rtn = []

    tmp = list(set(pos1[0]) & set(pos2[0]))
    if len(tmp) > 0:
        rtn.append(tmp)
    else:
        return False
    tmp = list(set(pos1[1]) & set(pos2[1]))
    if len(tmp) > 0:
        rtn.append(tmp)
    else:
        return False
    tmp = list(set(pos1[2]) & set(pos2[2]))
    if len(tmp) > 0:
        rtn.append(tmp)
    else:
        return False
    
    return rtn

while(run):
    test_num = gene_num(poses)
    HitBlow = io(test_num, poses)
    pos = gene_pos(HitBlow[0], HitBlow[1], test_num[0], test_num[1], test_num[2])
    if pos == True:
        print('正解！')
        run = False
    else:
        poses = itgr_pos(poses, pos)
    print()
