
def check_hang(_ban_co, i):
    return sum(_ban_co[i]) < 2

def check_cot(_ban_co, j):
    # for line in _ban_co:
    #     if line[j]:
    #         return False

    k = [x[j] for x in _ban_co]
    return sum(k) < 2

def check_cheo(_ban_co, i, j, _i, _j):
    k = [_ban_co[i][j]]
    while True:
        i += _i
        j += _j
        if i>=8 or j>=8 or i<0 or j<0:
            break
        k.append(_ban_co[i][j])
    return sum(k)<2

def Try(_ban_co):
    for i in range(0, 8):
        if not check_hang(_ban_co, i):
            return False
    for j in range(0,8):
        if not check_cot(_ban_co, j):
            return False
    for i in range(0, 8):
        if not check_cheo(_ban_co, i, 0, 1, 1):
            return False

    for i in range(0, 8):
        if not check_cheo(_ban_co, i, 7, -1, 1):
            return False
    for j in range(0, 8):
        if not check_cheo(_ban_co, 0, j, 1, 1):
            return False

    for j in range(0, 8):
        if not check_cheo(_ban_co, 0, j, -1, 1):
            return False
    return True

def xep_co(__ban_co, i):
    print("Buoc", i)
    for line in __ban_co:
        print(line)



    if i == 8:
        print('ket qua')
        for line in __ban_co:
            print(line)
        return True

    if Try(__ban_co):
        for j in range(0, 8):
            _ban_co = []
            for line in __ban_co:
                _ban_co.append(line[:])
            _ban_co[i][j] = 1
            if xep_co(_ban_co, i+1):
                return True

    else:
        return False


ban_co = []
for i in range(0, 8):
    ban_co.append([0,0,0,0,0,0,0,0])
xep_co(ban_co,0)
