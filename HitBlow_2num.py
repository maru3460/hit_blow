import copy
import random

poses = []#possibles
init_num = 2#見つかっていない数字の数
init_nums = [i for i in range(10)]#質問していない数字
run = True

def gene_num(poses, init_num, init_nums):#数字の生成
    rtn = []
    if init_num > 0:
        tmp = random.choice(range(len(init_nums)))
        rtn.append(init_nums[tmp])
        init_nums.pop(tmp)
        tmp = random.choice(range(len(init_nums)))
        rtn.append(init_nums[tmp])
        init_nums.pop(tmp)
    elif init_num <= 0:
        tmp = random.choice(range(len(poses)))
        tmp_run = True
        while(tmp_run):
            tmp_run = False
            x = poses[tmp][0][random.choice(range(len(poses[tmp][0])))]
            y = poses[tmp][1][random.choice(range(len(poses[tmp][1])))]
            if x == y:
                tmp_run = True
        rtn.append(x)
        rtn.append(y)
    else:
        print('error')
        exit(0)
    return rtn

def io(test_num):#inout
    print(f'{test_num[0]}{test_num[1]}を入力してください')
    hit = int(input('hit:'))
    blow = int(input('blow:'))
    return [hit, blow]

def gene_pos(hit, blow, x, y):#pos生成
    global init_num
    nums = [i for i in range(10)]
    if hit == 0 and blow == 0:
        tmp = copy.deepcopy(nums)
        tmp.remove(x)
        tmp.remove(y)
        return [[copy.deepcopy(tmp), copy.deepcopy(tmp)], [copy.deepcopy(tmp), copy.deepcopy(tmp)]]
    elif hit == 1:
        init_num -= 1
        tmp = copy.deepcopy(nums)
        tmp.remove(x)
        tmp.remove(y)
        return [[[x], copy.deepcopy(tmp)], [copy.deepcopy(tmp), [y]]]
    elif blow == 1:
        init_num -= 1
        tmp = copy.deepcopy(nums)
        tmp.remove(x)
        tmp.remove(y)
        return [[[y], copy.deepcopy(tmp)], [copy.deepcopy(tmp), [x]]]
    elif hit == 2:
        init_num -= 2
        return True
    else:
        print('error')
        exit(0)

def itgr_pos(poses, pos):#生成されたposとposesの統合
    if len(poses) == 0:
        tmp_poses = copy.deepcopy(pos)
    else:
        delete = []
        tmp_poses = []
        for i in range(len(poses)):
            for j in range(len(pos)):
                tmp = pos_pos(poses[i], pos[j])
                tmp_poses.append(tmp)
                if tmp == False:
                    delete.append(2 * i + j)
        delete.reverse()
        for i in delete:
            tmp_poses.pop(i)
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
    
    return rtn

while(run):
    test_num = gene_num(poses, init_num, init_nums)
    hb = io(test_num)
    pos = gene_pos(hb[0], hb[1], test_num[0], test_num[1])
    if pos == True:
        print('正解！')
        run = False
    else:
        poses = itgr_pos(poses, pos)
    
    print()